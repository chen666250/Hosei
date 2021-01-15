# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 10:58:18 2021

@author: chen
"""

class COBOLTemplates:
    identification_division="""
IDENTIFICATION DIVISION.
PROGRAM-ID.    %(PROGRAM_ID)s.
AUTHOR.        %(AUTHOR)s.
        """
        
    envirnoment_division="""
*
ENVIRONMENT DIVISION.
*
INPUT-OUTPUT SECTION.
FILE-CONTROL.
    SELECT %(InputName)s ASSIGN TO %(InputFile)s.
    SELECT %(OutputName)s ASSIGN TO %(OutputFile)s.
"""
    data_division_Header="""
DATA DIVISION.
FILE SECTION.
"""
    
    data_division_FD="""
FD  %(RecordName)s RECORD CONTAINS %(length)s CHARACTERS RECORDING MODE F.    
"""
    data_division_F01_a="""
01  %(fieldName)s        PIC %(stype)s(%(length)s) VALUE SPACES.    
"""
    data_division_F01_b="""
01  %(fieldName)s.    
"""
    data_division_F05="""    05  %(fieldName2)s       PIC %(stype2)s(%(length2)s)  VALUE SPACES.    
"""
    data_division_working_Header="""
WORKING-STORAGE SECTION.

"""

    data_division__working_F01_a="""
01  %(fieldName4)s.    
"""
    data_division__working_F01_b="""
01  %(fieldName6)s         PIC %(stype6)s(%(length6)s).    
"""
    data_division__working_F05="""    %(fieldName3)s         PIC %(stype3)s(%(length3)s).    
"""


    procedure_division_Header="""
    
PROCEDURE DIVISION.

"""
    procedure_division_func=""" 
    
"""
    function_Header="""
%(header)s.    
"""
    