import os
import shutil

"""
COMMAND NAME        :    mkdir
DESCRIPTION         :    To create a directory.
PARAMETERS          :    Directory name
"""
def mkdir(cmd):
        os.makedirs(cmd)
