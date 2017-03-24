import sys
import os
import shutil
import stat
import time
from  pwd import getpwuid
from os import stat
"""
COMMAND NAME       :  ls
DESCRIPTION        :   List  all files from the current directory.
	-a               :    It shows all the hidden files.
	-l               :    Displays  long listing.
  -h               :    Human readable sizes
"""
def size(size):
        suffixes=['B','KB','MB','GB','TB']
        precision=3
        suffixIndex = 0
        while size > 1024 and suffixIndex < 4:
            	suffixIndex += 1 #increment the index of the suffix
            	size = size/1024.0 #apply the division
        	return "%.*f%s"%(precision,size,suffixes[suffixIndex])


def ls(var,flag1):

	if(flag1==0):
  		
   		if var[0]=='ls' and len(var) == 1:
        		list=os.listdir(os.getcwd())
        		for i in list:
                		if i.startswith('.'):
               				list.remove(i)
        		 		      list.sort()
        			    	for i in list:
            					print i,
            					print "\t",
       	 				     	print ""
    	else:
			
        		flag=var[1]
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
                			          print str
         		elif flag=='-a':
            			list=os.listdir(os.getcwd())
            			list.sort()
            			for i in list:
               				print i,
               			 	print "\t",
           			 	    print ""
      	    elif flag=="-la":
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
                			print str
        		 elif flag=="-ah":
            			list=os.listdir(os.getcwd())
            			list.sort()
            			for i in list:
               			 	print i,
                		 	print "\t",
            			 	print ""
        		 elif flag=='-lh':
          		  	  list=os.listdir(os.getcwd())
            		  	list.sort()
            		  	for i in range(len(list)):
                			      info=os.stat(list[i])
                
                    	 			atime=time.asctime(time.localtime(info.st_atime))
              	        		name=getpwuid(stat(list[i]).st_uid).pw_name
             				        permissions = os.stat(list[i]).st_mode
                			      p=int(oct(permissions & 0777))
             				        s=size(info.st_size)
                			      str=p.__str__()+" "+name.__str__()+" "+ name.__str__() +" "+s.__str__()+" "+atime.__str__()+" "+list[i].__str__()
                			      print str
        		  elif flag=='-lah':
            			list=os.listdir(os.getcwd())
            			list.sort()
           			  for i in range(len(list)):
                			            info=os.stat(list[i])
              	                	atime=time.asctime(time.localtime(info.st_atime))
                		            	name=getpwuid(stat(list[i]).st_uid).pw_name
                			            permissions = os.stat(list[i]).st_mode
                			            p=int(oct(permissions & 0777))
                			            s=size(info.st_size)
              				            str=p.__str__()+" "+name.__str__()+" "+ name.__str__() +" "+s.__str__()+" "+atime.__str__()+" "+list[i].__str__()
                			            print str

	else:
		if(flag1==1):
   			f=open("default.txt",'w')
		  	if var[0]=='ls' and len(var) == 1:
			
        			list=os.listdir(os.getcwd())
        			for i in list:
                			if i.startswith('.'):
               					  list.remove(i)
        		 			        list.sort()
        			for i in list:
					        f.write(i+"\n")
		     else:
			
        			flag=var[1]
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
         			elif flag=='-a':
            				list=os.listdir(os.getcwd())
            				list.sort()
            				for i in list:
               					
						            f.write(i+"\n")
			       	elif flag=="-la":
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
                				#print str
					            	f.write(str)
        			elif flag=="-ah":
            				list=os.listdir(os.getcwd())
            				list.sort()
            				for i in list:
               			 		
						            f.write(i+"\t")
				      elif flag=='-lh':
          		  		  list=os.listdir(os.getcwd())
            		  		list.sort()
            		  		for i in range(len(list)):
                				      info=os.stat(list[i])
                
               	 				      atime=time.asctime(time.localtime(info.st_atime))
              	        			name=getpwuid(stat(list[i]).st_uid).pw_name
             					        permissions = os.stat(list[i]).st_mode
                				      p=int(oct(permissions & 0777))
             					        s=size(info.st_size)
                				      str=p.__str__()+" "+name.__str__()+" "+ name.__str__() +" "+s.__str__()+" "+atime.__str__()+" "+list[i].__str__()
                				
						                  f.write(str+"\n")
				      elif flag=='-lah':
            				list=os.listdir(os.getcwd())
            				list.sort()
           				  for i in range(len(list)):
                				            info=os.stat(list[i])
              	                		atime=time.asctime(time.localtime(info.st_atime))
                				            name=getpwuid(stat(list[i]).st_uid).pw_name
                				            permissions = os.stat(list[i]).st_mode
                				            p=int(oct(permissions & 0777))
                				            s=size(info.st_size)
              					            str=p.__str__()+" "+name.__str__()+" "+ name.__str__() +" "+s.__str__()+" "+atime.__str__()+" "+list[i].__str__()
                				
						                        f.write(str+"\n")
