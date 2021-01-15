# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 11:29:15 2021

@author: chen
"""
from COBOLTemplates import COBOLTemplates
from division import division
class identification_division(division):
      template=None
      PROGRAM_ID=None
      AUTHOR=None
      def __init__(self,PROGRAM_ID="PROGRAM_ID",AUTHOR="AUTHOR"):
          self.template=COBOLTemplates.identification_division
          self.PROGRAM_ID=PROGRAM_ID
          self.AUTHOR=AUTHOR
      
      
      def update(self,PROGRAM_ID="PROGRAM_ID",AUTHOR="AUTHOR"):
          self.PROGRAM_ID=PROGRAM_ID
          self.AUTHOR=AUTHOR
          self.template=COBOLTemplates.identification_division
          self.template=self.template%{"PROGRAM_ID":self.PROGRAM_ID,"AUTHOR":self.AUTHOR}
    
      def toPrint(self):
          self.update(self.PROGRAM_ID,self.AUTHOR)
          
          return self.template
      
       