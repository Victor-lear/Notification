# -*- coding: utf-8 -*-
"""
@author: victor
"""
from create_function import creat_channelbusy
from create_function import creat_interference
from create_function import creat_pingcheck
import threading
import sys
url="mongodb://administrator:administrator@140.118.151.39:27017/"
DB="AP"
Collection="Controller4"
thread = []
thread.append(threading.Thread(target = creat_channelbusy.exe_create_channelbusy,args=(url, DB, Collection)))
thread.append(threading.Thread(target = creat_interference.exe_create_interference,args=(url, DB, Collection)))
thread.append(threading.Thread(target = creat_pingcheck.exe_create_pingcheck,args=(url, DB, Collection)))
for i in range(len(thread)):
    thread[i].start()
for i in range(len(thread)):
    thread[i].join()

