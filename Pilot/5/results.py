import json
import time

def read_sma_data():
    with open(r'C:\Users\David\Desktop\Pilot\5\sma\SMA5.json', 'r') as file:
        data = json.load(file)
    return data

while True:
    data = read_sma_data()

    sma = sum(data.values()) / len(data)

    sma_data = {"sma_s": sma}

    with open(r'C:\Users\David\Desktop\Pilot\5\SMA_S.json', 'w') as file:
        json.dump(sma_data, file)
    print (f"sma_s = {sma}")
    time.sleep(33 )
