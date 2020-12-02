from csv import reader, writer
import time
import urllib.request
from json import loads
from rpc.daemon import Daemon
from rpc.backends.jsonrpc import JSONRPCDaemon
from ast import literal_eval

def get_csv(direc,fl=True):
    if direc == 'blocks':
        rows = []
        for part in ["_1000000.csv","_2000000.csv",".csv"]:
            with open(direc+part, 'r') as f:
                read = reader(f)
                newrows = list(read)
            rows = rows + [[float(x[i]) if i != 10 else literal_eval(x[i]) for i in range(len(x))] for x in newrows]
        return rows
    else:
        with open(direc+".csv", 'r') as f:
            rows = list(reader(f))
        rows = [[float(y) for y in x] for x in rows]
        return rows
        
def cache(data,direc):
    with open(direc+".csv", 'a+') as f:
        write = writer(f) 
        write.writerows(data)
    return True
            
def get_json(url):   
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as urltemp:
        data = loads(urltemp.read().decode())
    return data

def get_csv_from_url(url):   
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as urltemp:
        data = list(reader(urltemp.read().decode('latin-1').split('\n')))
    return data
        
def cache_price(last,period=86400):
    prices = []
    data = get_json("https://api.cryptowat.ch/markets/bittrex/aeonbtc/ohlc?periods="+str(period)+"&after="+str(last))
    data = list(data['result'][str(period)])[1:]
    prices_btc = []
    data_btc = get_json("https://api.cryptowat.ch/markets/bittrex/btcusd/ohlc?periods="+str(period)+"&after="+str(last))
    data_btc = list(data_btc['result'][str(period)])[1:]
    prices_xmr = []
    data_xmr = get_json("https://api.cryptowat.ch/markets/bittrex/xmrbtc/ohlc?periods="+str(period)+"&after="+str(last))
    data_xmr = list(data_xmr['result'][str(period)])[1:]
    s = min([len(data),len(data_btc),len(data_xmr)])
    while len(data_btc) > s:
        data_btc = data_btc[1:]
    while len(data) > s:
        data = data[1:]
    while len(data_xmr) > s:
        data_xmr = data_xmr[1:]
    for i in range(len(data)):
        prices_btc.append([data[i][0],float(data[i][4])])
        prices.append([data[i][0],float(data[i][4])*float(data_btc[i][4])])
        prices_xmr.append([data[i][0],float(data[i][4])/float(data_xmr[i][4])])
    if prices:
        cache(prices,"price")
        cache(prices_btc,"price_btc")
        cache(prices_xmr,"price_xmr")
        return True
    else:
        return False

def cache_blocks(last, end = None):
    daemon = Daemon(JSONRPCDaemon(host='127.0.0.1', port=32405))
    if end == None:
        end = daemon.height() - 1
    new = []
    while end > last:
        if last % 10000 == 0:
            if last <= 1000000:
                cache(new,"blocks_1000000")
            elif last <= 2000000:
                cache(new,"blocks_2000000")
            else:
                cache(new,"blocks")
            new = []
            print("cached: " + str(last) + "/" + str(end) + "... ("+str(last*100/end)+"%)")
        last +=1
        data = daemon.block(height=last)
        new.append([data.timestamp,data.height,data.difficulty,float(data.reward), \
            data.num_txs,float(data.fee),data.size,data.nonce,data.version[0],data.version[1],
            data.locked_txs,data.inputs,data.outputs,data.volume])
    if new:
        if last <= 1000000:
            cache(new,"blocks_1000000")
        elif last <= 2000000:
            cache(new,"blocks_2000000")
        else:
            cache(new,"blocks")
        return True
    else:
        return False

