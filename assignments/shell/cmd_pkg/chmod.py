import sys
import os
"""
COMMAND NAME        :  chmod
DESCRIPTION         :  It is used to change modify permission.
"""
def chmod(perm,fname):
        permission=int(perm,8)
        os.chmod(fname,permission)
