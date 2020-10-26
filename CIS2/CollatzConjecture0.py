# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 08:51:59 2020

@author: chen
"""

count={}
import matplotlib.pyplot as plt
def CollatzConjecture(num):
    if num not in count:
        count[num]=1
    else:
        count[num]+=1
    
    if(num==1):
        
        return True
    else :
        if(num%2==0):
         return CollatzConjecture(num/2)
        else:
         return CollatzConjecture(3*num+1)
    
    

for i in range(1,1000):
   CollatzConjecture(i)
    

keys=sorted(count.keys())
list1=[]
for key in keys:
    list1.append(count[key])


plt.plot((),list1)


    
    