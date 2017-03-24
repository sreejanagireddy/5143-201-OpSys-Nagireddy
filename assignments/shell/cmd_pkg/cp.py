import sys
import os
import shutil 
"""
COMMAND NAME :   cp (copy)
DESCRIPTION         :  It is used to copy the information from one file to the other file.
PARAMETERS         :   file1,file2
"""

def copy(srcfile,destfile):
        shutil.copy(srcfile, destfile)
