import sys
import os
import shutil
"""
COMMAND NAME      :  sort
DESCRIPTION       :  It is used to sort the data in the file.
"""
def sort(file,flag):
        with open(file,'r') as r:
		      list=[]
		      if(flag==1):
            for line in sorted(r):
              list.append(line)
			
			    fl=open("default.txt",'w')
			    for lines in list:
				      list.append(lines)
		      else:	
			      for line in sorted(r):
                        	print line
def sortredirect(file1,file2):
         with open(file1,'r') as r:
		            f2=open(file2,'w')

                for line in sorted(r):
                       f2.write(line)
def sortapp(file1,file2):
         with open(file1,'r') as r:
		            f2=open(file2,'a')
                for line in sorted(r):
                       f2.write(line)
