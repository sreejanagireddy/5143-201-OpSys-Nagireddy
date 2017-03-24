import sys
import os
import shutil
"""
COMMAND NAME        :   mv  (move)
DESCRIPTION         :  It is used to move or rename the  file to the other file.
PARAMETERS          : file 1,file2.
"""
def mv(src_file,dest_file):
        
		shutil.move(src_file,dest_file)
