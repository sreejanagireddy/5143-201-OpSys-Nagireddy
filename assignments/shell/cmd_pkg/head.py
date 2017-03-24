import sys
import os
import shutil
"""
COMMAND NAME        :  head
DESCRIPTION         :  It is used to display the first few lines of the file.
PARAMETERS          :  file
"""
def head(file,flag):
	 f=open(file,'r')
   i = 1
	 list=[]
	 if(flag==1):
		
		  for line in f:
               		 if i == 10:
                       		break
			             else:
                        	i = i+1
                        	list.append(line)
		  f.close()
		  f1=open("default.txt",'w')
		  for lines in list:
			    f1.write(lines)
   else:
         	for line in f:
                	if i == 10:
                        	break
			            else:
                        	i += 1
                        	print line
         f.close()

def headredirect(file1,file2):
        f1=open(file1,'r')
	      f2=open(file2,'w')

        i = 1
        for line in f1:
                if i == 10:
                        break
                else:
                        i += 1
                        f2.write(line)
			
def headapp(file1,file2):
        f1=open(file1,'r')
	      f2=open(file2,'a')

        i = 1
        for line in f1:
                if i == 10:
                        break
                else:
                        i += 1                      
                        f2.write(line)
