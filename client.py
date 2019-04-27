# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 03:12:37 2019

@author: DELL
"""
from _thread import * 
import threading
import socket
import _thread 

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
host="127.0.0.1"
port=9800
s.connect((host,port))

def receive_thread(s):
    while True :
        
        
        print("server:" ,s.recv(1024).decode('utf-8'))



start_new_thread(receive_thread,(s,))

while True :
    s.send(input().encode('utf-8'))