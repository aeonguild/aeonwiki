from compute import get_block_data
from file_writer import build_chart
from data import cache_blocks, cache_price, get_csv
from datetime import datetime
import gc
import time
import os.path

last_block = None
for x in ["blocks.csv","blocks_1000000.csv","blocks_2000000.csv"]:
    if(not os.path.exists(x)):
        last_block = 0 
        with open(x, 'w') as fp: 
            pass
print("opening block data... (0/5)")
if last_block == None:
    block = get_csv("blocks")[-1]
    last_block = int(block[1])
print("append new block data... (1/5)")
cache_blocks(last_block)


last_price = None
for x in ["price.csv","price_btc.csv","price_xmr.csv"]:
    if(not os.path.exists(x)):
        last_price = 1438819200
        with open(x, 'w') as fp: 
            pass
if last_price == None:
    last_price = str(int(get_csv("price")[-1][0]))
print("append new price data... (2/5)")
cache_price(last_price, period=86400)

print("compute data... (3/5)")
data = get_block_data()

#prep block charts
timestamp = ["new Date("+str(int(x*1000))+")" for x in data[0].pop(0)[1:]]
print("draw line charts... (4/5)")
while data[0]:
    gc.collect()
    yaxis = data[0].pop()
    key = yaxis.pop(0)
    print(key)
    if(key=='nonce'):
        build_chart(timestamp[-2*12960:],yaxis[-2*12960:],'nonce_recent')
    build_chart(timestamp,yaxis,key)

#prep month charts
timestamp = [datetime.fromtimestamp(x).strftime('%B, %Y') for x in data[1].pop(0)[1:]]
print("draw bar charts... (4/5)")
while data[1]:
    gc.collect()
    yaxis = data[1].pop()
    key = yaxis.pop(0)
    if(yaxis[0]!=None):
        yaxis = yaxis[11:]
        timestamp2=timestamp[11:]
    else:
        timestamp2=timestamp
    print(key)
    build_chart(timestamp2,yaxis,key)
    


















    
    
    
