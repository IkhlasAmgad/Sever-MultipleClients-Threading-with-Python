# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 03:14:40 2019

@author: DELL
"""
from _thread import * 
import threading
import socket

import _thread 
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
host="127.0.0.1"
port=9800
s.bind((host,port))
s.listen(30)


def receive_thread(c,ad):
    while True:
        x= c.recv(1024).decode('utf-8')
        print(ad[1]," : ", x)

def Send_thread(c,ad):
   
    #to run thread : thread nane . start
    while True:
        c.send(input().encode('utf-8'))
    


while True:
    c,ad=s.accept()
    print("connection from " ,ad[1] )
    start_new_thread(Send_thread,(c,ad))
    start_new_thread(receive_thread,(c,ad))
    
    
    #_thread.start_new_thread(client_thread ,(c,ad))
 #clint_thread is a fun (thread handle client)