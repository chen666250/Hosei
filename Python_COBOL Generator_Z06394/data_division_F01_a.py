# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 14:41:16 2021

@author: chen
"""
from COBOLTemplates import COBOLTemplates
class data_division_F01_a:
    template=None
    fieldName=None
    stype=None
    length=None
    def __init__(self,fieldName="fieldName",stype="X",length="80"):
        self.template=COBOLTemplates.data_division_F01_a
        self.fieldName=fieldName
        self.stype=stype
        self.length=length
        
    def toPrint(self):
        temp= self.template%{"fieldName": self.fieldName,"stype":self.stype,"length":self.length}
        return temp