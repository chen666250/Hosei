# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 11:40:10 2021

@author: chen
"""
from COBOLTemplates import COBOLTemplates
from division import division
class envirnoment_division(division):
    template=None
    InputName=None
    OutputName=None
    InputFile=None
    OutputFile=None
    def __init__(self,InputName="InputName",InputFile="InputFile",OutputName="OutputName",OutputFile="OutputFile"):
          self.template=COBOLTemplates.envirnoment_division
          self.InputName=InputName.ljust(10," ")
          self.InputFile=InputFile
          self.OutputName=OutputName.ljust(10," ")
          self.OutputFile=OutputFile

    def update(self,InputName="InputName",InputFile="InputFile",OutputName="OutputName",OutputFile="OutputFile"):
          self.template=COBOLTemplates.envirnoment_division
          self.InputName=InputName.ljust(10," ")
          self.InputFile=InputFile
          self.OutputName=OutputName.ljust(10," ")
          self.OutputFile=OutputFile
          self.template=self.template%{"InputName":InputName,"InputFile":InputFile,"OutputName":OutputName,"OutputFile":OutputFile}
    def toPrint(self):
          self.template=COBOLTemplates.envirnoment_division
          self.update(self.InputName,
          self.InputFile,
          self.OutputName,
          self.OutputFile)
          return self.template