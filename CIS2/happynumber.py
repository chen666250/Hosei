# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 23:54:39 2020

@author: chen
"""
temp=[]
hs=set()
def isHappyNum(num:str)->bool:
    if(temp.count(num)>1):
        temp.clear()
        return False
    lens=len(num)
    sums="0"
    for index in range(0,lens):
        sums=str(int(sums)+int(num[index])**2)
    if(sums=="1"):
        temp.clear()
        return True
    else:
        temp.append(sums)
        return isHappyNum(sums)
        
        
    

def findUnderLimit(limit:int):
    for num in range(0,limit+1):    
        if(isHappyNum(str(num))):
            hs.add(num)          
    print("HappyNum in Total ",len(hs))
    print("HappyNum rate is {:.2%} ".format(len(hs)/limit))
    
    