import sys
import os
"""
COMMAND NAME 	  :  history
DESCRIPTION       :  It is used to show history of all commands in the file.
"""
def history(cmd):
        a=open("/home/opsys_group05/history1.txt",'r')
        count=len(a.readlines())
        a.close()
        f=open("history1.txt",'a')
        f.write(str(count+1)+"\t"+cmd+"\n")

def history1(flag):
	  f=open("history1.txt",'r')
	 
	  if flag == 1:
		    f2=open("default.txt",'w')
		    for lines in f:
			      f2.write(lines)
			
		    f2.close()	

        print(f.read())

		
def historyredirect(file2):
        f=open("history1.txt",'r')
	      f1=open(file2,'w')
        for line in f:
               
              f1.write(line)
	      f1.close()
def historyapp(file2):
        f=open("history1.txt",'r')
	      f1=open(file2,'a')
        for line in f:
               
              f1.write(line)
	      f1.close()
