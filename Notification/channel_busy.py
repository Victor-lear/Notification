#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: victor
"""
import sys
import pymongo
from pymongo import MongoClient
from datetime import datetime


def setup_alarm(B_time= None,E_time= None,data= False):
    if(data!=False):
        
        if(B_time!=None and E_time!=None ):
            time=datetime.now()   #need to check vm time currect or not
            if(B_time<=time and time<=E_time):
                for i in range (len(data)):
                   
                        busy=0
                        data[i]={
                        'ap_name':data[i]['ap_name'],
                        'channel_busy':busy
                        }
            else:
                for i in range (len(data)):
                    if(data[i]['channel_busy']>=0.8):
                        busy=1
                    else:
                        busy=0
                    data[i]={
                        'ap_name':data[i]['ap_name'],
                        'channel_busy':busy
                        }
            
            
        else:
            for i in range (len(data)):
                if(data[i]['channel_busy']>=0.8):
                    busy=1
                else:
                    busy=0
                data[i]={
                    'ap_name':data[i]['ap_name'],
                    'channel_busy':busy
                    }
        return data
    else:
        return False

    
