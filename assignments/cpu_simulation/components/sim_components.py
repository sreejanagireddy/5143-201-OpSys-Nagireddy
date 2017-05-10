#!/usr/bin/python
"""
functions  : load_input, rounding
attributes : file_name,variable
descrition : it reads text file/loads input file,
             have function to round the decimal values and 
             used to import modules

"""

import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/components')

# Read txt file into a list of events
def load_input(file_name):
    jobs = deque()
    with open(file_name,'r') as finput:
        for line in finput.readlines():
            jobs.append(Event(line.strip()))

    return jobs
def rounding(x):
    y = "%.5f" % x
    if int(y[-2]) <= 5:
        return y[:-2]
    else:
        return "%.3f" % x

from collections import deque
from event import Event		
from semaphore import Semaphore
from process import Process
from cpu import CPU
from memory import Memory
from scheduler import Scheduler
