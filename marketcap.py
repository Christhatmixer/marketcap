
import requests
import time

optionList = ['BTC', 'ETH', 'XRP', 'BCH', 'LTC', 'ADA', 'NEO', 'XLM', 'EOS', 'XMR', 'XEM', 'DASH', 'MIOTA', 'USDT', 'TRX', 'ETC',
              'VEN', 'LSK', 'NANO', 'QTUM', 'OMG', 'BTG', 'BNB', 'ICX', 'ZEC', 'DGD', 'PPT', 'WAVES', 'STEEM', 'BCN', 'STRAT',
              'MKR', 'XVG', 'DOGE', 'RHOC', 'BTS', 'SC', 'DCR', 'SNT', 'AE', 'REP', 'BTM', 'WTC', 'KMD', 'ARK', 'ARDR', 'AION',
              'ZIL', 'VERI', 'CNX', 'ZRX', 'ETN', 'HSR', 'KCS', 'MONA', 'DGB', 'PIVX', 'GNT', 'QASH', 'GAS', 'BAT', 'SYS', 'ETHOS',
              'R', 'DRGN', 'FCT', 'NAS', 'LRC', 'FUN', 'GXS', 'RDD', 'DCN', 'XZC', 'ELF', 'IOST', 'SALT', 'KNC', 'KIN', 'LINK', 'POLY',
              'SMART', 'POWR', 'EMC', 'NXT', 'GBYTE', 'NEBL', 'BNT', 'MAID', 'SRN', 'PAY', 'PART', 'DENT', 'ICN', 'NXS', 'PLR', 'REQ', 'BTX',
              'ENG', 'STORJ', 'AGI']


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
validSelection = False
while validSelection == False:
    print(optionList)        
    selection = input("Track All or enter coin from list: ")
    if selection not in optionList:
        print("Not a valid selection")
    else:
        validSelection = True
while True:
    
    r = requests.get('https://api.coinmarketcap.com/v1/ticker/')
    data = r.json()
    
    time.sleep(300)
    r = requests.get('https://api.coinmarketcap.com/v1/ticker/')
    newData = r.json()
    if selection != "all":
        print("UPDATE")
        for counter, value in enumerate(newData):
            if value["symbol"] == selection:
                if float(value["percent_change_1h"]) > float(data[counter]["percent_change_1h"]):
                    percentageIncrease = float(value["percent_change_1h"]) - float(data[counter]["percent_change_1h"])
        time.sleep(300)
    else:
        print("UPDATE")
        for counter, value in enumerate(newData):
            if float(value["percent_change_1h"]) > float(data[counter]["percent_change_1h"]):
                percentageIncrease = float(value["percent_change_1h"]) - float(data[counter]["percent_change_1h"])
                print("{0} has increased by {1} percent".format(value["id"], percentageIncrease))
        time.sleep(300)                                
    




