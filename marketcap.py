
import requests
import time

optionList = ['All', 'BTC', 'ETH', 'XRP', 'BCH', 'LTC', 'ADA', 'NEO', 'XLM', 'EOS', 'XMR', 'XEM', 'DASH', 'MIOTA', 'USDT', 'TRX', 'ETC',
              'VEN', 'LSK', 'NANO', 'QTUM', 'OMG', 'BTG', 'BNB', 'ICX', 'ZEC', 'DGD', 'PPT', 'WAVES', 'STEEM', 'BCN', 'STRAT',
              'MKR', 'XVG', 'DOGE', 'RHOC', 'BTS', 'SC', 'DCR', 'SNT', 'AE', 'REP', 'BTM', 'WTC', 'KMD', 'ARK', 'ARDR', 'AION',
              'ZIL', 'VERI', 'CNX', 'ZRX', 'ETN', 'HSR', 'KCS', 'MONA', 'DGB', 'PIVX', 'GNT', 'QASH', 'GAS', 'BAT', 'SYS', 'ETHOS',
              'R', 'DRGN', 'FCT', 'NAS', 'LRC', 'FUN', 'GXS', 'RDD', 'DCN', 'XZC', 'ELF', 'IOST', 'SALT', 'KNC', 'KIN', 'LINK', 'POLY',
              'SMART', 'POWR', 'EMC', 'NXT', 'GBYTE', 'NEBL', 'BNT', 'MAID', 'SRN', 'PAY', 'PART', 'DENT', 'ICN', 'NXS', 'PLR', 'REQ', 'BTX',
              'ENG', 'STORJ', 'AGI']

# Check 1h increase
def check1hIncrease(value):
    if float(value["percent_change_1h"]) > float(data[counter]["percent_change_1h"]):
        percentageIncrease = float(value["percent_change_1h"]) - float(data[counter]["percent_change_1h"])
        print("{0} has increased by {1} percent".format(value["id"], percentageIncrease))
    time.sleep(300)
# Check 1h decrease
def check1hDecrease(value):
    if float(value["percent_change_1h"]) < float(data[counter]["percent_change_1h"]):
        percentageIncrease = float(value["percent_change_1h"]) - float(data[counter]["percent_change_1h"])
        print("{0} has decreased by {1} percent".format(value["id"], percentageIncrease))
    time.sleep(300)
    
# Check 24h increase
def check24hIncrease(value):
    if float(value["percent_change_24h"]) > float(data[counter]["percent_change_24h"]):
        percentageIncrease = float(value["percent_change_24h"]) - float(data[counter]["percent_change_24h"])
        print("{0} has increased by {1} percent".format(value["id"], percentageIncrease))
    time.sleep(300)
def check24hDecrease(value):
    if float(value["percent_change_24h"]) < float(data[counter]["percent_change_24h"]):
        percentageIncrease = float(value["percent_change_24h"]) - float(data[counter]["percent_change_24h"])
        print("{0} has increased by {1} percent".format(value["id"], percentageIncrease))
    time.sleep(300)
    
# Check 1h increase, decrease, and stagnation
def check1hChange(value):
    if float(value["percent_change_1h"]) > float(data[counter]["percent_change_1h"]):
        percentageIncrease = float(value["percent_change_1h"]) - float(data[counter]["percent_change_1h"])
        print("{0} has increased by {1} percent".format(value["id"], percentageIncrease))
    elif float(value["percent_change_1h"]) == float(data[counter]["percent_change_1h"]):
        print("{0} has no change".format(value["id"]))
    elif float(value["percent_change_1h"]) < float(data[counter]["percent_change_1h"]):
        percentageDecrease = float(value["percent_change_1h"]) - float(data[counter]["percent_change_1h"])
        print("{0} has increased by {1} percent".format(value["id"], percentageIncrease))
    time.sleep(300)
    
    
   
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
    if selection != "All":
        print("UPDATE")
        for counter, value in enumerate(newData):
            if value["symbol"] == selection:
                if float(value["percent_change_1h"]) > float(data[counter]["percent_change_1h"]):
                    percentageIncrease = float(value["percent_change_1h"]) - float(data[counter]["percent_change_1h"])
                    print("{0} has increased by {1} percent".format(value["id"], percentageIncrease))
        time.sleep(300)
    else:
        print("UPDATE")
        for counter, value in enumerate(newData):
            if float(value["percent_change_1h"]) > float(data[counter]["percent_change_1h"]):
                percentageIncrease = float(value["percent_change_1h"]) - float(data[counter]["percent_change_1h"])
                print("{0} has increased by {1} percent".format(value["id"], percentageIncrease))
        time.sleep(300)                                
    




