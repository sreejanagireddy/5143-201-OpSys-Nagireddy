import sys
import os
"""
COMMAND NAME      :  wc (word count)
DESCRIPTION       :  It is used to count the words,lines and characters in a file.
PARAMETERS        :  file
"""
def wc(file,flag):
	num_lines = 0
    	num_words = 0
    	num_chars = 0
    	with open(file, 'r') as input_file:
	      if(flag==1):
		        f1=open("default.txt",'r')
		        for line in input_file:
            			num_lines += 1
            			line_words = line.split()
            			num_words += len(line_words)
	    	 	        for word in line_words:
		    		    num_chars += len(word)
				    f1.write(' %i  %i  %i %s' % (num_lines, num_words, num_chars, file))
      	      else:
	        	for line in input_file:
	          	    num_lines += 1
            	   	    line_words = line.split()
        	    	    num_words += len(line_words)
	    		    for word in line_words:
		    			    num_chars += len(word)
    			    		    print  ' %i  %i  %i %s' % (num_lines, num_words, num_chars, file)
