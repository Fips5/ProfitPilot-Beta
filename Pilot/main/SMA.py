from BUY import buy
from CLOSE import close 
import json
import requests
from datetime import datetime
import time

def fetch_sma_s():
    with open(r'C:\Users\David\Desktop\Pilot\5\SMA_S.json') as file:
        data = json.load(file)
        sma_s = data['sma_s']
    return sma_s

def fetch_sma_l():
    with open(r'C:\Users\David\Desktop\Pilot\20\SMA_L.json') as file:
        data = json.load(file)
        sma_l = data['sma_l']
    return sma_l


def check_sma_intersects( sma_s, sma_l, position):
    if sma_s == 0 or sma_l == 0:
        print("Market closed.")
        return
    
    if position['status'] == 'closed':
        if sma_s > sma_l:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            buy()
            print(f"Buy - Timestamp: {current_time}, SMA_S={sma_s}, SMA_L={sma_l}")
            position['status'] = 'open'
        elif sma_s == sma_l:
            print("Market Closed")
            position['status'] = 'closed'
        else:
            print(f"No action - waiting for Buy condition. SMA_S={sma_s}, SMA_L={sma_l}")
    elif position['status'] == 'open':
        if sma_s < sma_l:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            close()
            print(f"Close - Timestamp: {current_time}, SMA_S={sma_s}, SMA_L={sma_l}")
            position['status'] = 'closed'
        else:
            print(f"No action - waiting for Close condition.SMA_S={sma_s}, SMA_L={sma_l}")

def main():
    position = {'status': 'closed'}
    
    while True:
        sma_s = fetch_sma_s()
        sma_l = fetch_sma_l()
        
        check_sma_intersects(sma_s, sma_l, position)
        # 20 seconds
        time.sleep(40)  

if __name__ == '__main__':
    main()
