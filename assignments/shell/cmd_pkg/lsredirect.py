import sys
import os
import shutil
import stat
import time
from  pwd import getpwuid
from os import stat
"""
COMMAND NAME       :  ls(redirection)
DESCRIPTION        :   List  all files from the current directory.
	   -a            :    It shows all the hidden files.
	   -l            :    Displays  long listing.
     -h            :    Human readable sizes
"""
def lsredirect(var,file,flag):
    f= open("file",'w')
    if var == 'ls':
	        if(flag==1):
		          if var[0]=='ls' and len(var) == 1:
        		        list=os.listdir(os.getcwd())
        		        for i in list:
                		    if i.startswith('.'):
               		 		      list.remove(i)
        		 		      list.sort()
        				      for i in list:
             					    f.write(i)
    else :
	f=open(file,'w')
        flag=var
        if flag=='-l':
       		     list=os.listdir(os.getcwd())
            	 list.sort()
               for i in list:
                	if i.startswith('.'):
                      list.remove(i)
         	     for i in range(len(list)):
                	info=os.stat(list[i])
                	atime=time.asctime(time.localtime(info.st_atime))
                	name=getpwuid(stat(list[i]).st_uid).pw_name
                	permissions = os.stat(list[i]).st_mode
                	p=int(oct(permissions & 0777))
                	str=p.__str__()+"\t"+name.__str__()+"\t"+ name.__str__() +"\t"+info.st_size.__str__()+"\t"+atime.__str__()+"\t"+list[i].__str__()
                	f.write(str+"\n")
        elif flag=="-a":
	      f=open(file,'w')
	      flag=var	
              list=os.listdir(os.getcwd())
              list.sort()
              for i in list:
		              f.write(i+"\t")
        elif flag=='-la':
	      f=open(file,'w')
              flag=var
              list=os.listdir(os.getcwd())
              list.sort()
              for i in list:
                    if i.startswith('.'):
                            list.remove(i)
              for i in range(len(list)):
                  info=os.stat(list[i])
                  # print info
                  # atime=info.st_atime
                  atime=time.asctime(time.localtime(info.st_atime))
                  name=getpwuid(stat(list[i]).st_uid).pw_name
                  permissions = os.stat(list[i]).st_mode
                  p=int(oct(permissions & 0777))
                  str=p.__str__()+"\t"+name.__str__()+"\t"+ name.__str__() +"\t"+info.st_size.__str__()+"\t"+atime.__str__()+"\t"+list[i].__str__()
                  f.write(str+"\n")
        elif flag=="-ah":
	
	          f=open(file,'w')
	          flag=var
            list=os.listdir(os.getcwd())
            list.sort()
            for i in list:
               
		                f.write(i+"\t")
        elif flag=='-lh':
	          f=open(file,'w')
	           flag=var

            list=os.listdir(os.getcwd())
            list.sort()
            for i in range(len(list)):
                info=os.stat(list[i])
                # print info
                # atime=info.st_atime
                atime=time.asctime(time.localtime(info.st_atime))
                name=getpwuid(stat(list[i]).st_uid).pw_name
                permissions = os.stat(list[i]).st_mode
                p=int(oct(permissions & 0777))
                s=size(info.st_size)
                str=p.__str__()+" "+name.__str__()+" "+ name.__str__() +" "+s.__str__()+" "+atime.__str__()+" "+list[i].__str__()
                f.write(str+"\t")
        elif flag=='-lah':
	          f=open(file,'w')
	          flag=var

            list=os.listdir(os.getcwd())
            list.sort()
            for i in range(len(list)):
                info=os.stat(list[i])
                # print info
                # atime=info.st_atime
                atime=time.asctime(time.localtime(info.st_atime))
                name=getpwuid(stat(list[i]).st_uid).pw_name
                permissions = os.stat(list[i]).st_mode
                p=int(oct(permissions & 0777))
                s=size(info.st_size)
                str=p.__str__()+" "+name.__str__()+" "+ name.__str__() +" "+s.__str__()+" "+atime.__str__()+" "+list[i].__str__()
                f.write(str+"\n")
