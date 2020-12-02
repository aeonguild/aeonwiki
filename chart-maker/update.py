from block_data import last_block, get_block_data
from chart import build_chart
from cache import cache_blocks, cache_price, get_csv
import gc
import time
import os.path

last_block = None
for x in ["blocks.csv","blocks_1000000.csv","blocks_2000000.csv"]:
    if(not os.path.exists(x)):
        last_block = 0 
        with open(x, 'w') as fp: 
            pass
if last_block == None:
    block = get_csv("blocks")[-1]
    last_block = int(block[1])
print("save block data... (1/4)")
cache_blocks(last_block)


last_price = None
for x in ["price.csv","price_btc.csv","price_xmr.csv"]:
    if(not os.path.exists(x)):
        last_price = 1438819200
        with open(x, 'w') as fp: 
            pass
if last_price == None:
    last_price = str(int(get_csv("price")[-1][0]))
print("save price data... (2/4)")
cache_price(last_price, period=86400)

print("calculate data... (3/4)")
data = get_block_data()
timestamp = ["new Date("+str(int(x*1000))+")" for x in data.pop(0)[1:]]

print("build charts... (4/4)")
while data:
    gc.collect()
    yaxis = data.pop()
    key = yaxis.pop(0)
    build_chart(timestamp,yaxis,key)
    
    
