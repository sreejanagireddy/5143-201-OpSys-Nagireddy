
"""
Program Name: SHELL COMMANDS
Team: Revathi Chikoti , Sreeja Nagireddy, Biradhavolu Sai Avinash Reddy
Description: 
	Implementation of "SHELL" in Python using the threads inorder to execute the each command in a thread.
"""
def function(cmd,flag):
			
		            	var = cmd.split(' ')
                	if '>>' in cmd and var[0]=='cat'  : #redirect standard output to a file
                      		var=cmd.split(' ')
                        	file1=var[1]
                        	file2=var[3]
                        	t = threading.Thread(target=catapp,args=(var[1],var[3],))
                        	t.start()
                        	t.join()
			            elif '>>' in cmd and var[0]=='history':
                        	var=cmd.split(' ')
                         	file1=var[2]
                         	t = threading.Thread(target=historyapp,args=(var[2],))
                         	t.start()
                         	t.join()
			            elif '>>' in cmd and var[0]=='head':
                        	var=cmd.split(' ')
                         	file1=var[1]
                         	file2=var[3]
                         	t = threading.Thread(target=headapp,args=(var[1],var[3],))
                         	t.start()
                         	t.join()
			
                	elif '>>' in cmd and var[0]=='grep' :
                        	var=cmd.split(' ')
                         	keyword=var[1]
                         	file1=var[2]
                         	file2=var[4]
                         	t = threading.Thread(target=grepapp,args=(var[1],var[2],var[4],))
                         	t.start()
                         	t.join()
			            elif '>>' in cmd and var[0]=='sort':
                       	 	var=cmd.split(' ')
                         	file1=var[1]
                         	file2=var[3]
                        	t = threading.Thread(target=sortapp,args=(var[1],var[3],))
                         	t.start()
                         	t.join()
		            	elif '>>' in cmd and var[0]=='tail':
                        	var=cmd.split(' ')
                         	file1=var[1]
                         	file2=var[3]
                         	t = threading.Thread(target=tailapp,args=(var[1],var[3],))
			                   	t.start()
			 	                  t.join()  

                	elif '>' in cmd and var[0]=='grep' :
                        	var=cmd.split(' ')
                         	keyword=var[1]
                         	file1=var[2]
                         	file2=var[4]
                         	t = threading.Thread(target=grepredirect,args=(var[1],var[2],var[4],))
                         	t.start()
                         	t.join()
                	elif '>' in cmd and var[0]=='history':
                        	var=cmd.split(' ')
                         	file1=var[2]
                         	t = threading.Thread(target=historyredirect,args=(var[2],))
                         	t.start()
                         	t.join()
	            		elif '>' in cmd and var[0]=='sort':
                       	 	var=cmd.split(' ')
                         	file1=var[1]
                         	file2=var[3]
                        	t = threading.Thread(target=sortredirect,args=(var[1],var[3],))
                         	t.start()
                         	t.join()
                	elif '>' in cmd and var[0]=='head':
                        	var=cmd.split(' ')
                         	file1=var[1]
                         	file2=var[3]
                         	t = threading.Thread(target=headredirect,args=(var[1],var[3],))
                         	t.start()
                         	t.join()
                	elif '>' in cmd and var[0]=='tail':
                        	var=cmd.split(' ')
                         	file1=var[1]
                         	file2=var[3]
                         	t = threading.Thread(target=tailredirect,args=(var[1],var[3],))
			                    t.start()
			 	                  t.join()
	       		      elif '>' in cmd and var[0]=='ls' and len(var) == 3:
                        	file=var[2] 
                         	t = threading.Thread(target=lsredirect,args=(var[0],file,flag,))
                         	t.start()
                         	t.join()
			            elif '>' in cmd and var[0]=='ls' and len(var) == 4:
				                  file=var[3]
                        	t = threading.Thread(target=lsredirect,args=(var[1],file,flag,))
                      		t.start()
                        	t.join()
			            elif '>' in cmd and var[0]=='cat':
                        	var=cmd.split(' ')
                         	file1=var[1]
                         	file2=var[3]
                         	t = threading.Thread(target=catredirect,args=(var[1],var[3],))
			                  	t.start()
			 	                  t.join()

	        	      elif '<' in cmd and var[0]=='cat':
	
        	                t = threading.Thread(target=cat,args=(var[2],flag,))
                        	t.start()
                        	t.join()	
                	elif '<' in cmd and var[0]=='grep':
                        	var=cmd.split(' ')
                        	t = threading.Thread(target=grep,args=(var[1],var[3],flag,))
                        	t.start()
                        	t.join()
                	elif '<' in cmd and var[0]=='sort':
                          var=cmd.split(' ')
                       	  t = threading.Thread(target=sort,args=(var[2],flag,))
                        	t.start()
                        	t.join()
                	elif '<' in cmd and var[0]=='head':
			                   	var=cmd.split(' ')
                        	t = threading.Thread(target=head,args=(var[2],flag,))
                       		t.start()
                       		t.join()
                	elif '<' in cmd and var[0]=='tail':
	
                	        var=cmd.split(' ')
        	                t = threading.Thread(target=tail,args=(var[2],flag,))
                        	t.start()
                        	t.join()
			            elif '<' in cmd and var[0]=='wc':
				                  var=cmd.split(' ')
                        	t = threading.Thread(target=wc,args=(var[1],flag,))
                      		t.start()
                        	t.join()

                	elif(var[0]=='ls'):
                        	t = threading.Thread(target=ls,args=(var,flag,))
                      		t.start()
                        	t.join()
              		elif(var[0]=='mkdir'):
                        	t = threading.Thread(target=mkdir,args=(var[1],))
				                  t.start()
                        	t.join()
                	elif(var[0]=='pwd'):
                        	t = threading.Thread(target=pwd)
                        	t.start()
                        	t.join()
                	elif(var[0]=='cat' and len(var) == 2):
				                  t = threading.Thread(target=cat,args=(var[1],flag,))
                        	t.start()
                        	t.join()
              		elif(var[0]=='cp'):
                        	t = threading.Thread(target=copy,args=(var[1],var[2],))
                        	t.start()
                        	t.join()
                	elif(var[0]=='rm'):
                        	t = threading.Thread(target=remove,args=(var[1],))
                        	t.start()
                        	t.join()
                	elif(var[0]=='mv'):
                        	t = threading.Thread(target=mv,args=(var[1],var[2],))
                        	t.start()
			            elif(var[0]=='rmdir'):
                        	t = threading.Thread(target=rmdir,args=(var[1],))
                        	t.start()
                        	t.join()
                	elif(var[0]=='head'):
                        	t = threading.Thread(target=head,args=(var[1],flag,))
                        	t.start()
                        	t.join()
                	elif(var[0]=='cd'):
                        	t = threading.Thread(target=cd,args=(var[1],))
                        	t.start()
                        	t.join()
                	elif(var[0]=='grep'):
                        	t = threading.Thread(target=grep,args=(var[1],var[2],flag,))
                        	t.start()
                        	t.join()
              		elif(var[0]=='wc'):
                        	t = threading.Thread(target=wc,args=(var[1],flag,))
                      		t.start()
                        	t.join()
		            	elif(var[0]=='cat' and len(var)==5):
                        	t = threading.Thread(target=concatination,args=(var[1],var[2],var[4],))
                        	t.start()
                        	t.join()
                	elif(var[0]=='chmod'):
                        	t = threading.Thread(target=chmod,args=(var[1],var[2],))
                        	t.start()
                        	t.join()
               	  elif(var[0]=='history'):
                	        t = threading.Thread(target=history1,args=(flag,))
                        	t.start()
                       		t.join()
                	elif(var[0]=='wcf'):
                        	t = threading.Thread(target=wcf,args=(var[1],))
                        	t.start()
                        	t.join()
                	elif(var[0]=='tail'):
                        	t = threading.Thread(target=tail,args=(var[1],flag,))
                       		t.start()
                        	t.join()
                	elif (var[0]=='who'):
			                  	t = threading.Thread(target=who)
                        	t.start()
                        	t.join()
                	elif(var[0]=='sort'):
                        	t = threading.Thread(target=sort,args=(var[1],flag,))
                        	t.start()
                        	t.join()
                  elif(var[0]=='less'):
                        	t = threading.Thread(target=less,args=(var[1],))
                        	t.start()
                        	t.join()
                          
def pipe(cmd):
	if '|' in cmd:
		var = cmd.split('|')
		
		if (len(var)==2):
			
			flag=1
			
			c=var[0].rstrip();
			function(c,flag)
			input=var[1]+'\t'+"default.txt"
			flag=0
			input=' '.join(input.split())
			function(input,flag)
	  	elif (len(var) == 3):
			flag=1
			c=var[0].rstrip();	
			function(c,flag)
			input=var[1]+'\t'+"default.txt"
			input=' '.join(input.split())
			input=input.rstrip()
			function(input,flag)
			input=var[2]+'\t'+"default.txt"
			flag=0
			input=' '.join(input.split())
			input=input.rstrip()

			function(input,flag)	


if __name__ == '__main__':
       while True:
                cmd = raw_input('% ')
                history(cmd)
                var=[]
		if '|' in cmd:
               		pipe(cmd)
		elif '!' in cmd:
				
				flag=0
				fp=open("history1.txt",'r')
				cmd=cmd[1:]
				i=0
				j1=cmd
				j=int(j1)
				j=j-1
				for l in fp:
					
					if i==j:
						cmd=l
						cmd=cmd[len(j1):]
						cmd=cmd.lstrip()

						cmd=' '.join(cmd.split())
						#print(cmd)
						function(cmd,flag)
						break
					else:
						i+=1
						continue		
		else:
			flag=0
			function(cmd,flag)
