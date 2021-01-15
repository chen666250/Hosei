# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 09:41:49 2021

@author: chen
"""
from COBOLTemplates import COBOLTemplates
class function:
    functionName=None
    functionHeader=COBOLTemplates.function_Header
    lineTemplate="""    %(keyword1)s %(keyword2)s %(keyword3)s %(keyword4)s      
"""
    steps=[]
    def __init__(self,functionName="A000-START"):
        self.functionName=functionName
        
  
        
    def addStep(self,keyword1="",keyword2="",keyword3="",keyword4=""):
        keyword1=keyword1.ljust(8," ")
        keyword2=keyword2.ljust(8," ")
        keyword3=keyword3.ljust(8," ")
        keyword4=keyword4.ljust(8," ")
        temp=self.lineTemplate%{"keyword1":keyword1,"keyword2":keyword2,"keyword3":keyword3,"keyword4":keyword4}
        self.steps.append(temp)
        
    def toPrint(self):
        temp=self.functionHeader%{"header":self.functionName}
        for s in self.steps:
            temp+=s
        return temp