import json
import time

def read_sma_data():
    with open(r'C:\Users\David\Desktop\Pilot\20\sma\SMA20.json', 'r') as file:
        data = json.load(file)
        return data

while True:
    data = read_sma_data()

    sma = sum(data.values()) / len(data)

    sma_data = {"sma_l": sma}

    with open(r'C:\Users\David\Desktop\Pilot\20\SMA_L.json', 'w') as file:
        json.dump(sma_data, file)
    print (f"sma_l = {sma}")
    time.sleep(33 )
