# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 21:49:45 2020

@author: chen
"""
import math
def isPrime(num:str)->bool:
    num=int(num)
    if num<=1:
        return False
    for i in range(2,int(math.sqrt(num)) + 1):
        if num%i==0:
            return False
        
    return True

def isEmirp(num:str)->bool:
    ans=[]
    if num in ans:
        return True
    else:
        if(isPrime(num)and isPrime(num[::-1]) and not isNPalindrome(num) ):
            ans.append(num)
            ans.append(num[::-1])
            return True
        else:
            return False
 

def isNPalindrome(n:str)->bool:
    
    if(len(n)==1 or (len(n)==2)and n[0]==n[1]):
        return True
    
    if(n[0]!=n[len(n)-1]):
        return False
    else:
        return isNPalindrome(n[1:len(n)-1])


def showallEprime(n:int):
    eprimes=[]
    for i in range(1,n+1):
        if(isEmirp(str(i))):
            print("found Eprime ",i)
            eprimes.append(str(i))
    print("in total ",len(eprimes))        
    return eprimes    
    
    
    
    