# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 20:58:25 2021

@author: chen
"""
from data_division__working_F05 import data_division__working_F05
from COBOLTemplates import COBOLTemplates
class local_variables_a:
    template=None
    fieldName4=None
    workChild=[]
    def __init__(self,fieldName4="fieldName4"):
        self.template=COBOLTemplates.data_division__working_F01_a
        self.fieldName4=fieldName4
        
        
    def addWorkChild(self,fieldName3="fieldName3",stype3="X",length3="length3"):
        temp=data_division__working_F05(fieldName3,stype3,length3)
        self.workChild.append(temp)
    
    def toPrint(self):
        temp= self.template%{"fieldName4": self.fieldName4}
        for c in self.workChild:
            temp+=c.toPrint()
        return temp