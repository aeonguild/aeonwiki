from cache import get_csv
from collections import deque
from statistics import median
from math import exp, log

last_block = {
    'timestamp' : 0,
    'block_count_24h' : 0,
    'block_difficulty' : 0.1,
    'block_height' : 0,
    'block_reward' : 0,
    'block_size_cum' : 0,
    'block_size_30d' : 0,
    'fee_24h' : 0,
    'fee_24h_usd' : 0,
    'inflation_1Y' : 0,
    'inputs' : 0,
    'marketcap' : 0,
    'marketcap_btc' : 0,
    'marketcap_xmr' : 0,
    'miner_revenue_1Y': 0,
    'miner_revenue_30d' : 0,
    'nonce_dist' : 1,
    'nonce' : 1,
    'outputs' : 0,
    'outputs_inputs' : 0,
    'price' : 0,
    'price_btc' : 0,
    'price_xmr' : 0,
    'supply_circulating' : 0,
    'supply_locked' : 0,
    'supply_total' : 0,
    'tx_24h' : 0,
    'version' : "0.0",
    'volume_30d' : 0,
    'volume_usd_30d' : 0,
    'volume_btc_30d' : 0
}

def get_block_data():
    #setup output list with keys as first element
    output = [[i] for i in list(last_block.keys())]
    
    #import data from csv
    blocks = get_csv("blocks")[::-1]
    price = get_csv("price")[::-1]
    price_btc = get_csv("price_btc")[::-1]
    price_xmr = get_csv("price_xmr")[::-1]
    
    #initiate price
    p = price.pop()    
    last_block['price'] = p[1]
    p_btc = price_btc.pop()    
    last_block['btc_price'] = p_btc[1]
    p_xmr = price_xmr.pop()    
    last_block['xmr_price'] = p_xmr[1]
    
    
    #stacks for fast processing
    day = deque([])
    month = deque([])
    year = deque([])
    nonces = deque([])
    
    #nonce uniformity constants
    #there are 2160 nonces and 2160 bins
    max_nonce=2**32
    bin_size = int((max_nonce)/(360*3))
    #we count how many nonces are in each bin
    bin_count = [0 for i in range((2**32)//(bin_size)+1)]
    #the number of bins with exactly 1 nonce should be about 1/e
    singleton_bins = 0
    locked_txs=[]
    
    #block reward over 1y
    reward_1y = 0
    
    while blocks:
        #block data
        x = blocks.pop()
        if blocks and len(blocks)%int(blocks[0][1]/100)==0:
            print(int(x[1]))

        #locked_txs
        if len(x[10])>0:
            locked_txs = locked_txs + [list(y) for y in x[10]]
            last_block['supply_locked'] += sum([y[0] for y in x[10]])
        new_locked_txs = []
        while locked_txs:
            tx = locked_txs.pop()
            if tx[1] > 500000000 and tx[1] < x[0]:
                last_block['supply_locked'] -= tx[0]
            elif tx[1] == 1:
                last_block['supply_locked'] -= tx[0]
            elif tx[1]< last_block['timestamp']:
                tx[1] = int(tx[1] - 1)
                new_locked_txs.append(tx)
            else:
                new_locked_txs.append(tx)
        locked_txs=new_locked_txs
            
        #no calculation data
        last_block['timestamp'] = x[0]
        last_block['block_height'] = int(x[1])
        last_block['version'] = str(int(x[8]))+"."+str(int(x[9]))
        last_block['block_reward'] = x[3]
        last_block['supply_total'] += x[3]
        last_block['supply_circulating'] = last_block['supply_total']-last_block['supply_locked']
        last_block['block_size_cum'] += x[6]
        last_block['block_difficulty'] = x[2]
        
        #price
        while p[0] < x[0] and price:
            p = price.pop()
            last_block['price'] = p[1]
            
        #btc_price
        while p_btc[0] < x[0] and price_btc:
            p_btc = price_btc.pop()
            last_block['price_btc'] = p_btc[1]
            
        #xmr_price
        while p_xmr[0] < x[0] and price_xmr:
            p_xmr = price_xmr.pop()
            last_block['price_xmr'] = p_xmr[1]
            
        #24h stats
        day.append([x[0],x[4],x[5],x[11],x[12]])
        last_block['block_count_24h'] += 1
        last_block['tx_24h'] += x[4]
        last_block['fee_24h'] += x[5]
        last_block['inputs'] += x[11]
        last_block['outputs'] += x[12]
        last_block['outputs_inputs'] += (x[12]-x[11])
        
        #remove old data
        while day[0][0] < x[0] - 24*60*60:
            head = day.popleft()
            last_block['block_count_24h'] -= 1
            last_block['tx_24h'] -= head[1]
            last_block['fee_24h'] -= head[2]
            last_block['inputs'] -= head[3]
            last_block['outputs'] -= head[4]
            
        last_block['fee_24h_usd'] = last_block['fee_24h']*last_block['price']
        
        #month stats
        month.append([x[0],x[3],x[5],x[6],x[13],last_block['price_btc'],last_block['price']])
        last_block['miner_revenue_30d'] += (x[3]+x[5])*last_block['price']
        last_block['volume_30d'] += x[13]/(1.0*10**12)
        last_block['volume_usd_30d'] += x[13]*last_block['price']/(1.0*10**12)
        last_block['volume_btc_30d'] += x[13]*last_block['price_btc']/(1.0*10**12)
        last_block['block_size_30d'] += x[6]
        
        #remove old data
        while month[0][0] < x[0] - 30*24*60*60:
            head = month.popleft()
            last_block['miner_revenue_30d'] -= (head[1]+head[2])*head[6]
            last_block['volume_30d'] -= head[4]/(1.0*10**12)
            last_block['volume_usd_30d'] -= head[4]*head[6]/(1.0*10**12)
            last_block['volume_btc_30d'] -= head[4]*head[5]/(1.0*10**12)
            last_block['block_size_30d'] -= head[3]
        
        #inflation 1y %
        year.append([x[0],x[3],x[5],last_block['price']])
        reward_1y += x[3]
        last_block['miner_revenue_1Y'] += last_block['price']*(x[3]+x[5])
        while year[0][0] < x[0] - 365*24*60*60:
            amt = year.popleft()
            reward_1y -= amt[1]
            last_block['miner_revenue_1Y'] -= amt[3]*(amt[1]+amt[2])
        last_block['inflation_1Y']  = 100 * reward_1y / last_block['supply_total']
        last_block['marketcap']=last_block['supply_total']*last_block['price']
        last_block['marketcap_btc']=last_block['supply_total']*last_block['price_btc']
        last_block['marketcap_xmr']=last_block['supply_total']*last_block['price_xmr']
   	    
        #nonce uniformity
        #calculate which bin the nonce belongs in like a histogram

        if last_block['block_height']==1146200:
            #nonce uniformity constants
            #there are 2160 nonces and 2160 bins
            max_nonce = 2**64
        bin_size = int((max_nonce)/(360*3))
        nonce = int(x[7])//bin_size
        #add to memory
        nonces.append(nonce)
        #put nonce into bin
        bin_count[nonce] += 1
        #recalculate bins with exactly one
        if bin_count[nonce] == 1:
            singleton_bins += 1 
        elif bin_count[nonce] == 2:
            singleton_bins -= 1 
        if len(nonces)> 360*3:    
            #remove nonce and recalculate
            nonce = nonces.popleft()    
            bin_count[nonce] -= 1
            if bin_count[nonce] == 1:
                singleton_bins += 1 
            elif bin_count[nonce] == 0:
                singleton_bins -= 1
        #assuming the nonces are uniformly random, singleton_bins / 2160 == 1 / e
        #thus e * singleton_bins / 2160 == 1
        last_block['nonce_dist'] = (exp(1)*singleton_bins/(360*3))*100
        last_block['nonce'] = int(x[7])*100/max_nonce
            
        for i in range(len(output)):
            output[i].append(list(last_block.values())[i])
        
    return output
