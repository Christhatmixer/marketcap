
import requests
import time



def check1h():
    r = requests.get('https://api.coinmarketcap.com/v1/ticker/')
    data = r.json()
    for name in data:
        print(name["id"] + " " + name["percent_change_1h"])
def check24h():
    r = requests.get('https://api.coinmarketcap.com/v1/ticker/')
    data = r.json()
    for name in data:
        print(name["id"] + " " + name["percent_change_24h"])
while True:
    r = requests.get('https://api.coinmarketcap.com/v1/ticker/')
    data = r.json()
    time.sleep(300)
    r = requests.get('https://api.coinmarketcap.com/v1/ticker/')
    newData = r.json()
    for counter, value in enumerate(newData):
        if value["percent_change_1h"] > data[counter]["percent_change_1h"]:
            
            print("{0} has increased by {1}".format(value["id"], value["percent_change_1h"]))
    time.sleep(300)
    
    
