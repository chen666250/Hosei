# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 14:05:55 2021

@author: chen
"""
from data_division_F01_a import data_division_F01_a
from data_division_F01_b import data_division_F01_b

from COBOLTemplates import COBOLTemplates
class file_FD:
    template=None
    RecordName=None
    length=80
    data_division_F01_a=None
    data_division_F01_b=None
    
    def __init__(self,RecordName="RecordName",length="80"):
        self.RecordName=RecordName
        self.length=length
        self.template=COBOLTemplates.data_division_FD
        
    def toPrint(self):
         self.template=COBOLTemplates.data_division_FD
         self.template=self.template%{"RecordName":self.RecordName,"length":self.length}
         if(self.data_division_F01_a!=None):
             self.template+=self.data_division_F01_a.toPrint()
         if(self.data_division_F01_b!=None):
             self.template+=self.data_division_F01_b.toPrint()
         return self.template
    def addData_division_F01_a(self,fieldName="fieldName",stype="X",length="80"):
        self.data_division_F01_a=data_division_F01_a(fieldName=fieldName,stype=stype,length=length)
    
    def addData_division_F01_b(self,fieldName="fieldName"):
        self.data_division_F01_b=data_division_F01_b(fieldName)
       
        
        
        