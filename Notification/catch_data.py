# -*- coding: utf-8 -*-
"""
@author: victor
"""

import sys
import pymongo
from pymongo import MongoClient
from datetime import datetime, timedelta

mongo_url_01="mongodb://administrator:administrator@140.118.151.39:27017/"
testurl="mongodb://admin:bmwee8097218@140.118.122.115:30415/"
def last_data(url,DB,Collection):
    global mongo_url_01,testurl
    try:
        conn = MongoClient(url) 
        db = conn[DB]
        collection = db[Collection]
        cursor=collection.find().sort("_id",-1).limit(1)
        data=[d for d in cursor]
        if data==[]:
            return False
        else:
            return data[0]['Datetime']
    except:
        return False
def catch_data(url,DB,Collection,time):
    global mongo_url_01,testurl
    try:
        conn = MongoClient(url) 
        db = conn[DB]
        collection = db[Collection]
        cursor=collection.find({'Datetime':{'$gte': (time-timedelta(minutes=3)), '$lte': (time+timedelta(minutes=3))}}).sort("_id",-1)
        data=[d for d in cursor]
        if data==[]:
            return False
        else:
            return data
    except:
        return False
def nowdata(url,DB,Collection):
    time=last_data(url,DB, Collection)
    data=catch_data(url,DB, Collection,time)
    return data
url="mongodb://admin:bmwee8097218@140.118.122.115:30415/"
DB="AP_test"
Collection="Controller4"
print(nowdata(url,DB,Collection))