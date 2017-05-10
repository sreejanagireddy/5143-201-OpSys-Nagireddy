#!/usr/bin/python
"""
class            :    Event
description      :    this class is used for incoming events.

"""

from sim_components import *
import os
import math
import sys
# Class for incoming events
class Event():
    def __init__(self,e):
        e = e.split()
        self.event = e[0]
        self.time  = int(e[1])

        if self.event == 'A':
            self.jobid      = int(e[2])
            self.memory     = int(e[3])
            self.burst_time = int(e[4])
        elif self.event == 'I':
            self.burst_time = int(e[2])
        elif self.event == 'W' or self.event == 'S':
            self.semaphore = int(e[2])
