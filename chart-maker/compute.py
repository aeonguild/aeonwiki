from data import get_csv
from collections import deque
from math import exp, log
from datetime import datetime

def get_block_data():
    from template import by_block, by_month
    #setup output list with keys as first element
    block_output = [[i] for i in list(by_block.keys())]
    month_output = [[i] for i in list(by_month.keys())]
    
    #import data from csv
    blocks = get_csv("blocks")[::-1]
    price = get_csv("price")[::-1]
    price_btc = get_csv("price_btc")[::-1]
    price_xmr = get_csv("price_xmr")[::-1]
    
    by_month['timestamp'] = blocks[-1][0]
    #initiate price
    p = price.pop()    
    p_btc = price_btc.pop()    
    p_xmr = price_xmr.pop()    
    
    
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
    block_count = 0
    while blocks:
        #block data
        x = blocks.pop()
        if blocks and len(blocks)%int(blocks[0][1]/100)==0:
            print(int(x[1]))

        #locked_txs
        if len(x[10])>0:
            locked_txs = locked_txs + [list(y) for y in x[10]]
            by_block['supply_locked'] += sum([y[0] for y in x[10]])
        new_locked_txs = []
        while locked_txs:
            tx = locked_txs.pop()
            if tx[1] > 500000000 and tx[1] < x[0]:
                by_block['supply_locked'] -= tx[0]
            elif tx[1] == 1:
                by_block['supply_locked'] -= tx[0]
            elif tx[1]< by_block['timestamp']:
                tx[1] = int(tx[1] - 1)
                new_locked_txs.append(tx)
            else:
                new_locked_txs.append(tx)
        locked_txs=new_locked_txs
            
        #no calculation data
        by_block['timestamp'] = x[0]
        by_block['block_height'] = int(x[1])
        by_block['version'] = str(int(x[8]))+"."+str(int(x[9]))
        by_block['supply_total'] += x[3]
        by_block['supply_circulating'] = by_block['supply_total']-by_block['supply_locked']
        by_block['block_size_cum'] += x[6]
        if(x[1]>2000):
            by_block['block_difficulty'] = x[2]
            by_block['block_reward'] = x[3]
            if(by_block['block_count_24h'] == None):
                by_block['block_count_24h'] = block_count
            
        day.append(x[0]) 
        block_count += 1   
        if(by_block['block_count_24h'] != None):
            by_block['block_count_24h'] += 1
        while day[0] < x[0] - 24*60*60:
            head = day.popleft()
            block_count -= 1
            if(by_block['block_count_24h'] != None):
                by_block['block_count_24h'] -= 1
        
        #price
        while p[0] < x[0] and price:
            p = price.pop()
            by_block['price'] = p[1]
        if(by_block['price'] != None):
            by_block['marketcap']=by_block['supply_total']*by_block['price']
            if(by_month['miner_revenue'] == None):
                by_month['miner_revenue'] = 0
                by_month['volume_usd'] = 0
                by_month['fee_usd'] = 0
            by_month['miner_revenue'] += (x[3]+x[5])*by_block['price']
            by_month['volume_usd'] += x[13]*by_block['price']/(1.0*10**12)
            by_month['fee_usd'] += x[5]*by_block['price']
        else:
            by_month['miner_revenue'] = None
            by_month['volume_usd'] = None
            by_month['fee_usd'] = None
            
        #btc_price
        while p_btc[0] < x[0] and price_btc:
            p_btc = price_btc.pop()
            by_block['price_btc'] = p_btc[1]
        if(by_block['price_btc'] != None):
            if(by_month['volume_btc'] == None):
                by_month['volume_btc'] = 0
            by_block['marketcap_btc']=by_block['supply_total']*by_block['price_btc']
            by_month['volume_btc'] += x[13]*by_block['price_btc']/(1.0*10**12)
        else:
            by_month['volume_btc'] = None
            
        #xmr_price
        while p_xmr[0] < x[0] and price_xmr:
            p_xmr = price_xmr.pop()
            by_block['price_xmr'] = p_xmr[1]
        if(  by_block['price_xmr'] != None):
            by_block['marketcap_xmr']=by_block['supply_total']*by_block['price_xmr']
            
            
        by_month['fee'] += x[5]
        by_month['tx'] += x[4]
        by_month['volume'] += x[13]/(1.0*10**12)
        by_month['block_size'] += x[6]
        by_month['inputs'] += x[11]
        by_month['outputs'] += x[12]
        by_month['outputs_inputs'] += (x[12]-x[11])
        
        #inflation 1y %
        year.append([x[0],x[3]])
        reward_1y += x[3]
        while year[0][0] < x[0] - 365*24*60*60:
            amt = year.popleft()
            reward_1y -= amt[1]
        by_block['inflation_1Y']  = 100 * reward_1y / by_block['supply_total']
   	    
        #nonce uniformity
        #calculate which bin the nonce belongs in like a histogram
        if by_block['block_height']==1146200:
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
        by_block['nonce_dist'] = (exp(1)*singleton_bins/(360*3))*100
        by_block['nonce'] = int(x[7])*100/max_nonce
            
        for i in range(len(block_output)):
            block_output[i].append(list(by_block.values())[i])
        
        if datetime.fromtimestamp(x[0]).strftime('%B') != datetime.fromtimestamp(by_month['timestamp']).strftime('%B') or len(blocks)==0:
            for i in range(len(month_output)):
                month_output[i].append(list(by_month.values())[i])
            by_month = {
                'timestamp' : x[0],
                'block_size' : 0,
                'fee' : 0,
                'fee_usd' : 0,
                'inputs' : 0,
                'miner_revenue' : 0,
                'outputs' : 0,
                'outputs_inputs' : 0,
                'tx' : 0,
                'volume' : 0,
                'volume_usd' : 0,
                'volume_btc' : 0
            }
        else:
            by_month['timestamp'] = x[0]
    return [block_output,month_output]
