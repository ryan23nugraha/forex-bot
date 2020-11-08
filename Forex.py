from datetime import datetime
import os
import requests
import pymongo
import dns
os.system('cls')


try:
    client = pymongo.MongoClient(
        "mongodb+srv://Forex23:7bCnUVU09Vlq6TS0@cluster0.fpun3.mongodb.net/forex?retryWrites=true&w=majority")
    db = client.forex
    collection = db.EURUSD
    print("connect to MongoDB")
except:
    print("Could not connect to MongoDB")
    exit()

URL = "https://www.freeforexapi.com/api/live?pairs=EURUSD"

tamp = requests.get(url=URL).json()['rates']['EURUSD']
dateTamp = datetime.fromtimestamp(tamp['timestamp'])
rate = tamp['rate']
print(f'{dateTamp} : {rate}')
while(1):
    tamp = requests.get(url=URL).json()['rates']['EURUSD']
    date = datetime.fromtimestamp(tamp['timestamp'])
    rate = tamp['rate']
    if dateTamp != date:
        dataDocument = {
            "EURUSD": {
                "date": date,
                "rate": rate
            }
        }
        collection.insert_one(dataDocument)
        print(f'{date} : {rate}')

    dateTamp = date
