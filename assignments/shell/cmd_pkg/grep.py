import os
import sys
import shutil
"""
COMMAND NAME :  grep
DESCRIPTION         :  It is used to search the given keyword from the file.
PARAMETERS          :  ‘keyword’ file
"""
def grep(keyword,file,flag):
        f=open(file,'r')
	      list=[]
	      if(flag==1):
		
		        for line in f:
			            if keyword in line:
                		    	list.append(line)
		                        f.close()
		                        f1=open("default.txt",'w')
		                        for lines in list:
			                f1.write(lines)
	      else:
            		for line in f:
				if keyword in line:
                		    	print line
def grepredirect(keyword,file1,file2):
        f=open(file1,'r')
        f1=open(file2,'w')
        for line in f:
          if keyword in line:
			      f1.write(line)
def grepapp(keyword,file1,file2):
        f=open(file1,'r')
        f1=open(file2,'a')
        for line in f:
       		 if keyword in line:
			      f1.write(line)
