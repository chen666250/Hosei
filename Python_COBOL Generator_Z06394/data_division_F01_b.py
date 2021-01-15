# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 19:18:30 2021

@author: chen
"""
from COBOLTemplates import COBOLTemplates
from data_division_F05 import data_division_F05
class data_division_F01_b:
    template=None
    fieldName=None
    childs=[]
    def __init__(self,fieldName="fieldName"):
        self.template=COBOLTemplates.data_division_F01_b
        self.fieldName=fieldName
        
    def addChild(self,fieldName2="fieldName2",stype2="stype2",length2="length2"):
        fieldName2=fieldName2.ljust(8," ")
        c=data_division_F05(fieldName2,stype2,length2)
        self.childs.append(c)
    
    def toPrint(self):
        temp=self.template%{"fieldName":self.fieldName}
        for c in self.childs:
            t2=c.toPrint()
            temp+=t2
            
        return temp
        
    