# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 17:56:51 2021

@author: chen
"""
from COBOL import COBOL


c=COBOL()
c.identification_division.update(PROGRAM_ID="123",AUTHOR="chen" )
c.envirnoment_division.update(InputFile="PRTLINE",
                              InputName="PRT-LINE",
                              OutputFile="PRTDONE",
                              OutputName="PRT-DONE")
c.toPrint()
#
c.data_division.files[0].addData_division_F01_a(fieldName="PRT-REC",
                     stype="X",
                     length="80")
#


c.data_division.files[1].addData_division_F01_b(fieldName="PRT-REC-DONE") # add file 01 at data division
c.data_division.files[1].data_division_F01_b.addChild(fieldName2="PRT-DATE",
                     stype2="X",
                     length2="8")# add 05 child fields
c.data_division.files[1].data_division_F01_b.addChild(fieldName2="FILLER",
                     stype2="X",
                     length2="1")
#


c.data_division.addWorkStationFileA(fieldName4="PGM-VARIABLES")# add working storage variables 
c.data_division.workstation[0].addWorkChild(fieldName3="PGM-COUNT",
                           stype3="9",
                           length3="05")# add 05 child variables
#
c.data_division.addWorkStationFileB(fieldName6="YYYYMMDD",
                                    stype6="9",
                                    length6="8")#add working storage variables with out 05 level


######################################################################
c.procedure_division.addFunction(functionName="A000-START")
c.procedure_division.funcs["A000-START"].addStep("DISPLAY","'HELLO WORLD'")
c.procedure_division.funcs["A000-START"].addStep("OPEN","OUTPUT","PRT-LINE")
#####################################################################

c.save2File(fileName="cobolFile")






