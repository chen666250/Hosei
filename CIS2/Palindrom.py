# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 08:30:50 2020

@author: chen
"""

def findNearestPalindrom(n:str)->str:
    if(len(n)==1):
        if(int(n)==9):
            return "11"
        else:
            return str(int(n)+1)
    else:
       oddoreven= oddOrEven(n)
       frontpart=saveTheFrontPart(n,oddoreven)
       isnpalindrome=isNPalindrome(n)
   
    if(oddoreven):#odd 
        if(isnpalindrome or (int(frontpart[:-1])<int(n[len(n)//2:][1:]))):
            return buildThePalindrom(frontpart,True,oddoreven)
        else:
            return buildThePalindrom(frontpart,False,oddoreven)
    else:   #even
        if(isnpalindrome or (int(frontpart)<int(n[len(n)//2:]))):
            
            return buildThePalindrom(frontpart,True,oddoreven)
        else:
            return buildThePalindrom(frontpart,False,oddoreven)
            
    

def oddOrEven(n:str)->bool:
    if(len(n)%2==0):
        return False
    else:
        return True
   
    

def saveTheFrontPart(n:str,oddOrEven:bool) ->str:
        lens=len(n)//2
     
    
        if(oddOrEven):
           
            return n[0:lens+1]
        
        else:
            return n[0:lens]
    
   
def buildThePalindrom(frontpart:str,addOne:bool,oddoreven:str)->str:
  
   
    if(addOne):
        frontpart=str(int(frontpart)+1)
       
    if(oddoreven):
        return frontpart+str(int(frontpart[::-1][1:]) )
    else:
        return frontpart+str(int(frontpart[::-1] ))
    
    
    


def isNPalindrome(n:str)->bool:
    
    if(len(n)==1 or (len(n)==2)and n[0]==n[1]):
        return True
    
    if(n[0]!=n[len(n)-1]):
        return False
    else:
        return isNPalindrome(n[1:len(n)-1])
    
    
