import os
import shutil
import sys
"""
COMMAND NAME      :  tail
DESCRIPTION       :  It is used to display the last few lines of the file.
PARAMETERS        :  file
"""
def tail(input,flag):
	f=open(input,'r')
	i = 1
	list=[]
	if(flag==1):
        	recorder=20
        	num=0
        	numLines=sum(1 for line in open(input))
       		f = open(input,'r')
        	for lines in f:
                	num=num+1
                	if numLines-num<recorder:
                        	list.append(lines)
        	f.close()
		      f1=open("default.txt",'w')
		      for lines in list:
			          f1.write(lines)
	else:
		recorder=20
        	num=0
        	numLines=sum(1 for line in open(input))
       		f = open(input,'r')
        	for lines in f:
                	num=num+1
                	if numLines-num<recorder:
                        	print (lines)
        	return
          f.close()

def tailredirect(file1,file2):
        recorder=20
        num=0
        numLines=sum(1 for line in open(file1))
        f1 = open(file1,'r')
	f2=open(file2,'w')
        for lines in f1:
                num=num+1
                if numLines-num<recorder:
                        #f2=open(file2,'a')
                        f2.write(lines)
def tailapp(file1,file2):
        recorder=20
        num=0
        numLines=sum(1 for line in open(file1))
        f1 = open(file1,'r')
	      f2=open(file2,'a')
        for lines in f1:
                num=num+1
        	      if numLines-num<recorder:
                        
                       	f2.write(lines)
