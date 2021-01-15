# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 20:30:27 2021

@author: chen
"""
from COBOLTemplates import COBOLTemplates
class data_division_F05:
    template=None
    fieldName2=None
    stype2=None
    length2=None
    
    def __init__(self,fieldName2="fieldName2",stype2="stype2",length2="length2"):
        self.template=COBOLTemplates.data_division_F05
        self.fieldName2=fieldName2
        self.stype2=stype2
        self.length2=length2
    
    def toPrint(self):
        temp=self.template
        return temp%{"fieldName2":self.fieldName2,"stype2":self.stype2,"length2":self.length2}
        