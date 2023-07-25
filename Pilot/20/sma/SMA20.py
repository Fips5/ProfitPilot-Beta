import os
import requests
import json
import time
import sys

MAX_ENTRIES = 12

def restart_program():
    python = sys.executable
    sys.stdout.flush()
    sys.stderr.flush()
    os.execv(python, [python] + sys.argv)


'''def get_price():
    try:
        response = requests.get(r"http://localhost:8000")  
        response.raise_for_status() 
        data = response.json()
        return data["prices"][0]
    except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
        print(f"Error occurred while retrieving price: {e}")
        restart_program()
        return None'''

def get_price():
    try:
        with open(r"C:\Users\David\Desktop\API Manual\Webcam Model\output.json", "r") as file:
            data = json.load(file)
            return data["price"][0]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error occurred while retrieving price: {e}")
        restart_program()
        return None


def write_to_json(data):
    with open(r"C:\Users\David\Desktop\Pilot\20\sma\SMA20.json", "r+") as file:
        try:
            file_data = json.load(file)
        except json.decoder.JSONDecodeError:
            file_data = {}

        file_data.update(data)
        
        keys = list(file_data.keys())[-MAX_ENTRIES:]
        file_data = {str(index+1): file_data[key] for index, key in enumerate(keys)}
        
        file.seek(0)
        json.dump(file_data, file, indent=4)
        file.truncate()

def main():
    counter = 1
    while True:
        price = get_price()
        write_to_json({counter: price})
        counter += 1
        print('running')
        time.sleep(30 )

if __name__ == "__main__":
    main()