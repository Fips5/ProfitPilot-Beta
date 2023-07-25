import requests
import json
import time

MAX_ENTRIES = 5

def get_price():
    response = requests.get("http://localhost:8000")  # Replace with your API endpoint URL
    data = response.json()
    return data["prices"][0]

def write_to_json(data):
    with open("live_prices.json", "r+") as file:
        try:
            file_data = json.load(file)
        except json.decoder.JSONDecodeError:
            file_data = {}
        
        # Add new entry
        file_data.update(data)
        
        # Keep only the newest 5 entries
        keys_to_keep = sorted(file_data.keys(), key=int, reverse=True)[:MAX_ENTRIES]
        file_data = {key: file_data[key] for key in keys_to_keep}
        
        file.seek(0)
        json.dump(file_data, file, indent=4)
        file.truncate()

def main():
    counter = 1
    while True:
        price = get_price()
        write_to_json({counter: price})
        counter += 1
        time.sleep(3)

if __name__ == "__main__":
    main()


