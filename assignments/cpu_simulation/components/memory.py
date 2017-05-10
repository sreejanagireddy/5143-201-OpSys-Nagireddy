#!/usr/bin/python
"""
class           :       Memory
function        :       allocate,deallocate
description     :       it allocates memory for scheduled process and deallocate after usage.

"""

from sim_components import *
import os
import math
import sys
class Memory():
    def __init__(self):
        self.limit = 512
        self.free  = self.limit
        self.processlist = []

    # Allocate memory for scheduled process
    def allocate(self,process):
        if process.memory <= self.free:
            self.free = self.free - process.memory
            self.processlist.append(process)
        else:
            return False
        return True

    def deallocate(self,pid):
        for process in self.processlist:
            if process.pid == pid:
                self.free += process.memory
                self.processlist.remove(process)
                return True
        else:
            return False
