#!/usr/bin/python
""" ******************************Project Assignment -2******************************
                       
                      program to implement cpu scheduling simulation  
           
                      Note:code written in python
                      execution command: python simulation.py
                      output:displayed on console and send to file out.txt                 

    Team members:Ajay Dinakar Kandavalli,SreejaNagireddy, Revathi Chikoti
  

    @References :http://stackoverflow.com
	             https://docs.python.org/2/library/collections.html
				 https://docs.python.org/2/tutorial/classes.html
				 http://academic.udayton.edu/SaverioPerugini/
				 https://github.com/paladizm/Operating-Systems/tree/master/projects/p2
                 
   ***********************************************************************************
"""



"""

class        : simulator
functions    : run           :to start simulation
               display_status:the status of simulation is displayed here
			   main          :execution starts from here
**attributes** 
input_file    :input file
e             :event
description  : it is main class which manages loading events,movings process accordingly to level 1, level 2
               permorming IO, event handling, dispaly status of cpu_time, memory

"""


import os
import math
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/components')
from sim_components import *

# Simulator
class Simulator():
    def __init__(self):

        self.clock = 0
        self.memory = Memory()
        self.scheduler = Scheduler(self)
        self.cpu = CPU(self)

        self.event_dispatcher = { 
            'D': self.display_status,
            'A': self.scheduler.new_process,
            'I': self.scheduler.perform_io,
            'W': self.scheduler.sem_acquire,
            'S': self.scheduler.sem_release
        }
        
    def run(self,inputfile):

        # Load events
        events = load_input(inputfile)

        # Main loop
        while(len(events) != 0):
            #print events[0].event
            e = events[0]

            # Do IO
            if bool(self.cpu.io):
                #print self.cpu.io[0].io_completed_time,self.clock
                if self.cpu.io[0].io_completed_time == self.clock:
                    # Send to CPU que 1
                    p = self.cpu.io.popleft()
                    p.new = False
                    self.cpu.queues[0].append(p)
                    print("Event: C   Time: %s" % (self.clock))
             
            # Event handling
            if e.time == self.clock:
                self.event_dispatcher[e.event](e)
                events.popleft()

            self.cpu.update()

            if bool(self.cpu.running_process):
                self.cpu.running_process.quantum -= 1
                self.cpu.running_process.total_quantum += 1

                # Check if process exceed quota, terminate if necessary
                if self.cpu.running_process.total_quantum == self.cpu.running_process.burst_time:
                    pid = self.cpu.running_process.pid

                    print("Event: T   Time: %s" % (self.clock+1))
                    self.cpu.running_process.completed_time = self.clock+1
                    self.cpu.finished.append(self.cpu.running_process)

                    self.cpu.running_process = None
                    self.memory.deallocate(pid)

                elif self.cpu.running_process.quantum == 0:
                    # Move to level 2
                    print("Event: E   Time: %s" % (self.clock+1))
                    self.cpu.queues[1].append(self.cpu.running_process)
                    self.cpu.running_process = None

            self.clock += 1
 
        # Final report   
        print("\nThe contents of the FINAL FINISHED LIST")
        print("---------------------------------------\n")
        print("Job #  Arr. Time  Mem. Req.  Run Time  Start Time  Com. Time")
        print("-----  ---------  ---------  --------  ----------  ---------\n")


        sum_turn_around = 0
        sum_wait_time = 0
        for p in self.cpu.finished:
            print("%6s  %9s  %9s  %8s  %10s  %9s" % (p.pid, p.time, p.memory, p.burst_time, p.start_time, p.completed_time))
            sum_turn_around += (p.completed_time - p.time)
            sum_wait_time += p.cpu_time - p.time
        print("\n")

        avg_turn_around = float(sum_turn_around) / float(len(self.cpu.finished)) 
        avg_wait_time   = float(sum_wait_time) / float(len(self.cpu.finished))

        print("The Average Turnaround Time for the simulation was %s units.\n" % rounding(avg_turn_around))
        print("The Average Job Scheduling Wait Time for the simulation was %s units.\n" % rounding(avg_wait_time))
        print("There are %s blocks of main memory available in the system.\n" % (self.memory.free))
        return

    def display_status(self,e):
        #return
        print("Event: D   Time: %s" % (self.clock))
        print("\n************************************************************\n");
        print("The status of the simulator at time %s.\n" % (self.clock))
        print("The contents of the JOB SCHEDULING QUEUE")
        print("----------------------------------------\n")

        if bool(self.scheduler.queue):
            print("Job #  Arr. Time  Mem. Req.  Run Time")
            print("-----  ---------  ---------  --------\n")

            # Display process in queue
            for p in self.scheduler.queue:
                print("%5s  %9s %10s %9s" % (p.pid, p.time, p.memory, p.burst_time) )
        else:
            print("The Job Scheduling Queue is empty.")
        print("\n")

        # Display content in cpu queue
        print("The contents of the FIRST LEVEL READY QUEUE")
        print("-------------------------------------------\n")
        if bool(self.cpu.queues[0]):
            print("Job #  Arr. Time  Mem. Req.  Run Time")
            print("-----  ---------  ---------  --------\n")

            for p in self.cpu.queues[0]:
                print("%5s  %9s  %9s  %8s" % (p.pid,p.time,p.memory,p.burst_time))
        else:
            print("The First Level Ready Queue is empty.")
        print("\n")

        print("The contents of the SECOND LEVEL READY QUEUE")
        print("--------------------------------------------\n")
        if bool(self.cpu.queues[1]):
            print("Job #  Arr. Time  Mem. Req.  Run Time")
            print("-----  ---------  ---------  --------\n")

            for p in self.cpu.queues[1]:
                print("%5s  %9s  %9s  %8s" % (p.pid,p.time,p.memory,p.burst_time))
        else:
            print("The Second Level Ready Queue is empty.")
        print("\n")

        # IO
        print("The contents of the I/O WAIT QUEUE")
        print("----------------------------------\n")

        if bool(self.cpu.io):
            print("Job #  Arr. Time  Mem. Req.  Run Time  IO Start Time  IO Burst  Comp. Time")
            print("-----  ---------  ---------  --------  -------------  --------  ----------\n")

            for p in self.cpu.io:
                print("%5s  %9s  %9s  %8s  %13s  %8s  %10s" % (p.pid, p.time, p.memory, p.burst_time, p.io_start_time, p.io_burst, p.io_completed_time))
        else:
            print("The I/O Wait Queue is empty.")
        print("\n")


        label = ["ZERO","ONE","TWO","THREE","FOUR"]
        for i in range(self.cpu.sm):
            s = self.cpu.semaphores[i]
            title = "The contents of SEMAPHORE %s" % (label[i])
            print(title)
            print("-"*len(title))
            print("\nThe value of semaphore %s is %s.\n" % (i,s.count))
            if bool(s.queue):
                for p in s.queue:
                    print(p.pid)
            else:
                print("The wait queue for semaphore %s is empty." % (i))
            print("\n")

        # CPU time
        print("The CPU  Start Time  CPU burst time left")
        print("-------  ----------  -------------------\n")
        p = self.cpu.running_process
        if  p != None:
            babi = p.burst_time - p.total_quantum
            print("%7s  %10s  %19s" % (p.pid,p.start_time,babi))
        else:
            print("The CPU is idle.")
        print("\n")

        print("The contents of the FINISHED LIST")
        print("---------------------------------\n")
        print("Job #  Arr. Time  Mem. Req.  Run Time  Start Time  Com. Time")
        print("-----  ---------  ---------  --------  ----------  ---------\n")


        for p in self.cpu.finished:
            print("%6s  %9s  %9s  %8s  %10s  %9s" % (p.pid, p.time, p.memory, p.burst_time, p.start_time, p.completed_time))
        print("\n")

       # Memory status
        print("There are %s blocks of main memory available in the system.\n" % (self.memory.free))
		


if __name__ == "__main__":
    # Set input file
    #inputfile = os.path.dirname(os.path.realpath(__file__)) + '/input_data/jobs_in_a.txt'
    #inputfile = os.path.dirname(os.path.realpath(__file__)) + '/input_data/jobs_in_b.txt'
    inputfile = os.path.dirname(os.path.realpath(__file__)) + '/input_data/jobs_in_c.txt'
    f = open("out.txt", 'w')	
    s1 = Simulator()
    s2 = Simulator()
    s1.run(inputfile) #for sending output to  file out.txt  
    sys.stdout = f	#this sens the console output to a file
    s2.run(inputfile)
    f.close()
    	