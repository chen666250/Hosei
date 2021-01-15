# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 23:43:59 2021

@author: chen
"""

from COBOLTemplates import COBOLTemplates
class data_division__working_F01_b:
    template=None
    fieldName6=None
    stype6=None
    length6=None
    
    def __init__(self,fieldName6="fieldName6",stype6="X",length6="length6"):
        self.template=COBOLTemplates.data_division__working_F01_b
        self.fieldName6=fieldName6.ljust(9," ")
        self.stype6=stype6
        self.length6=length6
        
       
    def toPrint(self):
        temp=self.template
        return temp%{"fieldName6":self.fieldName6,"stype6":self.stype6,"length6":self.length6}