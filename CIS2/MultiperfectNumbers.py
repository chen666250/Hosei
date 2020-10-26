# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 10:29:05 2020

@author: chen
"""

def findPerfect(num,multi=2):
    temp=[]
    for divide in range(1,(num//2)+1):
        if(num%divide==0):
            temp.append(divide)
    temp.append(num)        
#    print(temp)
         
    return True if(sum(temp)==num*multi) else False
 

def findAllUnder(lens=50000,multi=2):
    temps=[]
    for num in range(1,lens):
        if findPerfect(num,multi):
            temps.append(num)
            
    print(temps)