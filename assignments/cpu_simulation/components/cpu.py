#!/usr/bin/python
"""
class           :   CPU
function        :   new_process,update, runQ1
attributes      :   process
description     :   it manages time quantam of process

"""

from sim_components import *
import os
import math
import sys
from collections import deque
class CPU():
    def __init__(self,sim,lvl=2,sm=5):
        self.sim = sim
        self.level = 1
        self.sm = sm
        self.running_process = None

        # Queues
        self.queues   = [deque() for i in range(lvl)]        # Main queue
        self.io       = deque()                              # IO queue
        self.finished = []                                   # Finished list
        self.semaphores = [Semaphore(1) for i in range(sm)]  # Semaphores

    def new_process(self,process):
        self.queues[0].append(process)
        self.update()

    # Should this moved to main loop?
    def update(self):
        self.sim.scheduler.update_state()
        # Move to running
        if self.running_process == None:

            # Run process from queue 1
            if bool(self.queues[0]):
                self.runQ1()

            # Run process from queue 2
            elif bool(self.queues[1]):
                self.running_process = self.queues[1].popleft()
                self.running_process.quantum = 300
                self.level = 2

        elif bool(self.queues[0]) and self.level == 2:
            # Move running_process back to queue 2
            self.queues[1].append(self.running_process)
            self.runQ1()

    def runQ1(self):
        self.running_process = self.queues[0].popleft()
        self.level = 1
        self.running_process.quantum = 100
       
        if self.running_process.new:
            self.running_process.start_time = self.sim.clock