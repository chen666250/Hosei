
IDENTIFICATION DIVISION.
PROGRAM-ID.    123.
AUTHOR.        chen.
        
*
ENVIRONMENT DIVISION.
*
INPUT-OUTPUT SECTION.
FILE-CONTROL.
    SELECT PRT-LINE   ASSIGN TO PRTLINE.
    SELECT PRT-DONE   ASSIGN TO PRTDONE.

DATA DIVISION.
FILE SECTION.

FD  InputName  RECORD CONTAINS 80 CHARACTERS RECORDING MODE F.    

01  PRT-REC        PIC X(80) VALUE SPACES.    

FD  OutputName RECORD CONTAINS 80 CHARACTERS RECORDING MODE F.    

01  PRT-REC-DONE.    
    05  PRT-DATE       PIC X(8)  VALUE SPACES.    
    05  FILLER         PIC X(1)  VALUE SPACES.    

WORKING-STORAGE SECTION.


01  fieldName4.    
    PGM-COUNT         PIC 9(05).    

01  YYYYMMDD          PIC 9(8).    

    
PROCEDURE DIVISION.


A000-START.    
    DISPLAY  'HELLO WORLD'                        
    OPEN     OUTPUT   PRT-LINE               