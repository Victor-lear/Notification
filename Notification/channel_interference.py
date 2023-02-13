#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: victor
"""
import sys
import pymongo
from pymongo import MongoClient
from datetime import datetime

def setup_alarm(data):
    if(data!=False):
        for i in range (len(data)):
            if(data[i]['channel_interference']>=0.3):
                busy=1
            else:
                busy=0
            data[i]={
                'ap_name':data[i]['ap_name'],
                'channel_interference':busy
                }
        return data
    else:
        return False

    

