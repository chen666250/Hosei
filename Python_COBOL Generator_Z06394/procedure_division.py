# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 15:08:57 2021

@author: chen
"""
from COBOLTemplates import COBOLTemplates
from division import division
from function import function
class procedure_division(division):
    Header=COBOLTemplates.procedure_division_Header
    funcs={}
    def __init__(self):
        pass
    
    
    
    def addFunction(self,functionName="A000-START"):
        temp=function()
        self.funcs[functionName]=temp
    
    def toPrint(self):
        temp=""
        temp+=self.Header
        for f in self.funcs:
            temp+=self.funcs[f].toPrint()
        return temp
    
