#!/usr/bin/python
"""
class       : Scheduler
functions   : new_process, update_state,perform_io,sem_acquire,sem_release
attributes  : event
description : Scheduler class adds a new process to scheduler queue ,updates state of jobs in queue,
              performs_IO, manages semaphore acquire and release.
"""

from sim_components import *
import os
import math
import sys
# Scheduler component
class Scheduler():
    def __init__(self,sim):
        self.sim    = sim
        self.queue  = deque()

    # Add new process to scheduler queue
    def new_process(self,e):
        process = Process(e)

        print("Event: A   Time: %s" % (process.time))

        if process.memory > self.sim.memory.limit:
            print("This job exceeds the system's main memory capacity.")
            return

        # Add job to scheduler queue
        self.queue.append(process)

        # Update job schedule
        self.update_state()

    # Update ready state of jobs in queue
    def update_state(self):
        if bool(self.queue):
            success = self.sim.memory.allocate(self.queue[0])
        
            if success:
                process = self.queue.popleft()
                process.cpu_time = self.sim.clock
                self.sim.cpu.new_process(process)

    def perform_io(self,e):
        #print "alamak",e.time,e.burst_time,self.sim.cpu.running_process

        if bool(self.sim.cpu.running_process):
            print("Event: I   Time: %s" % (self.sim.clock))
    
            # Set IO time
            self.sim.cpu.running_process.io_burst = e.burst_time
            self.sim.cpu.running_process.io_start_time = self.sim.clock
            self.sim.cpu.running_process.io_completed_time = self.sim.clock + e.burst_time

            # Move process to IO queue
            self.sim.cpu.io.append(self.sim.cpu.running_process)

            # Sort IO queue by completed time
            self.sim.cpu.io = deque(sorted(self.sim.cpu.io,key=lambda p: p.io_completed_time))
            
            self.sim.cpu.running_process = None

    # BABI
    def sem_acquire(self,e):
        print("Event: W   Time: %s" % (self.sim.clock))
        s = self.sim.cpu.semaphores[e.semaphore]
        s.count -= 1

        if s.count < 0 :
            if bool(self.sim.cpu.running_process):
                # Move process to semaphore queue
                s.queue.append(self.sim.cpu.running_process)
                self.sim.cpu.running_process = None

    def sem_release(self,e):
        print("Event: S   Time: %s" % (self.sim.clock))
        s = self.sim.cpu.semaphores[e.semaphore]
        s.count += 1
        # Release back process to Q1
        if bool(s.queue):
            p = s.queue.popleft()
            p.new = False
            self.sim.cpu.queues[0].append(p)
