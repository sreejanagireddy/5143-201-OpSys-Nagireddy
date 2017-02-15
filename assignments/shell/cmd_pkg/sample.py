import os

import sys

import shutil

import time

import stat



from os.path import expanduser

  

    def cat(self,file):

        if(os.path.isfile(file)):

            f = open(file,'r')

            print(f.read())

        else:

            print("file does not exist")

            

    def mv(self,src,dest):

        if os.path.isfile(src):

            shutil.move(src,dest)

            print("moved succesfully")

        else:

            print("source file doesnot exist")	



    def cp(self,src1,dest1):

        try:

            shutil.copy(src1,dest1)

            print("copyied succesfully")

        except shutil.Error as e:

            print("file not found")

        except IOError as e:

            print('Error: %s' % e.strerror)

            

    def wc(self,filename):

        try:

            f=open(filename,'r')

            wordcount=0 

            for lines in f:

                count=lines.split()

                wordcount=wordcount+len(count)

            f.close()

            print("word count:",str(wordcount))

        except IOError as e:

            print("no such file")



   

            

    def cd(self,flag):

        if(flag=='~'):

            hie=os.getcwd()

            print(hie)

            home = expanduser("~")

            print(home)

        elif(flag=='..'):

            os.chdir('..')

            new=os.getcwd()

            print(new)

            



    def rm(self,file):

        if os.path.exists(file):

            try:

                os.remove(file)

                print("removed successfully")

            except IOError as e:

                print("file doesnot exist")
