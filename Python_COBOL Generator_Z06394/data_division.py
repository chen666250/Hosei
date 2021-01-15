# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 12:00:31 2021

@author: chen
"""
from COBOLTemplates import COBOLTemplates
from division import division
from file_FD import file_FD
from local_variables_a import local_variables_a
from data_division__working_F01_b import data_division__working_F01_b
class data_division(division):
    header=COBOLTemplates.data_division_Header
    working_header=COBOLTemplates.data_division_working_Header
    files=[]
    workstation=[]
    def __init__(self,Dfs):
        for f in Dfs:
            temp=file_FD(f)
            self.files.append(temp)
    
    def addWorkStationFileA(self,fieldName4="fieldName4"):
        temp=local_variables_a(fieldName4="fieldName4")
        self.workstation.append(temp)
    def addWorkStationFileB(self,fieldName6="fieldName6",stype6="X",length6="length6"):
        temp=data_division__working_F01_b(fieldName6=fieldName6,stype6=stype6,length6=length6)
        self.workstation.append(temp)
    
    def toPrint(self):
        temp=self.header
        for file in self.files:
            temp+=file.toPrint()
        
        temp+=self.working_header
        for f in self.workstation:
            temp+=f.toPrint()
        
        return temp