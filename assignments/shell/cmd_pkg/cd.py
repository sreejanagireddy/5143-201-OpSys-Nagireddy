import sys
import os
"""
COMMAND NAME   :   cd (change directory)
DESCRIPTION    :   Used to change directory to named directory.
        ~      :  Used to change directory to home directory.
       ..      :   Used to change directory to parent directory
PARAMETERS     :  Directory
"""
def cd(directory):
  if (directory=='..'):
            os.chdir('..')
            new=os.getcwd()
            print(new)
  elif(directory=='~'):
	      home=os.path.expanduser('~')
	      os.chdir(home)
	      new=os.getcwd()            	
        print(new)
	else:
		  if os.path.isdir(directory):
			    os.chdir(directory)
			    new=os.getcwd()
			    print(new)
      else:
			        print("directory does not exists")
