#!/usr/bin/python
"""
class           :       Process
description     :       convert event to process

"""

from sim_components import *
import os
import math
import sys
class Process():
    def __init__(self,e):
        # Convert event to process
        self.time      = e.time
        self.pid       = e.jobid
        self.memory    = e.memory
        self.burst_time = e.burst_time

        # Time
        self.quantum = 0            # Allocated time
        self.total_quantum = 0      # Elapsed time in CPU          
        self.cpu_time = 0           # Time when process enter CPU queue
        self.start_time = 0         # Time when process run in CPU
        self.completed_time = 0     # Time when process completed

        # IO
        self.io_start_time = 0      # Start time
        self.io_completed_time = 0  # Completed time
        self.io_burst = 0           # Burst time

        self.new = True

    def __str__(self):
        return str(self.pid)