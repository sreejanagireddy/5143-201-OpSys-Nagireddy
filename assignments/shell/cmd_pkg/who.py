import sys
import os
"""
COMMAND NAME    :  who
DESCRIPTION     :  It is used to list the users currently logged in.
"""
def who():
        x=subprocess.check_output("who")
        print x
