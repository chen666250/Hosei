# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 11:17:17 2021

@author: chen
"""
from identification_division import identification_division
from envirnoment_division import envirnoment_division
from data_division import data_division
from procedure_division import procedure_division
import os
class COBOL:
    identification_division=None
    envirnoment_division=None
    data_division=None
    procedure_division=None
    
    def __init__(self):
        self.identification_division=identification_division()
        self.envirnoment_division=envirnoment_division()
        Dfs=[self.envirnoment_division.InputName,self.envirnoment_division.OutputName]
        self.data_division=data_division(Dfs)
        self.procedure_division=procedure_division()
        
    
 
    
    def toPrint(self):
        temp=""
        temp+= self.identification_division.toPrint()
        temp+= self.envirnoment_division.toPrint()
        temp+=self.data_division.toPrint()
        temp+=self.procedure_division.toPrint()
        print(temp)
        return temp
    def save2File(self,fileName="cobolFile"):
        temp=self.toPrint()
        file=open(os.path.join(fileName+".cob"),"w")
        file.write(temp)
        file.close()
        
       
        
        
        
    