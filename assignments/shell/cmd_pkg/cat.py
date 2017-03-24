import sys
import os
import shutil

"""
COMMAND NAME      :  cat
DESCRIPTION       :  To display the given file.
PARAMETERS        :  file
"""


def cat(file,flag):
		
      if(flag==1):
			  f = open(file,'r')
			  f1=open("default.txt",'w')
            		
			   for line in f:
				    f1.write(line)
            		
		  else:
		 	  if(os.path.isfile(file)):
				    f = open(file,'r')
            print(f.read())	
def catredirect(file1,file2):
        f=open(file1,'r')
        f1=open(file2,'w')
        shutil.copy(file1,file2)
def catapp(file1,file2):
        f=open(file1,'r')
        f1=open(file2,'a')
        #shutil.copy(file1,file2)
	      for lines in f:
	            f1.write(lines)
