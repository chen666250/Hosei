# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 21:35:04 2021

@author: chen
"""
from COBOLTemplates import COBOLTemplates
class data_division__working_F05:
    template=None
    fieldName3=None
    stype3=None
    length3=None
    
    def __init__(self,fieldName3="fieldName3",stype3="X",length3="length3"):
        self.template=COBOLTemplates.data_division__working_F05
        self.fieldName3=fieldName3
        self.stype3=stype3
        self.length3=length3
        
    
       
    def toPrint(self):
        temp=self.template
        return temp%{"fieldName3":self.fieldName3,"stype3":self.stype3,"length3":self.length3}
    