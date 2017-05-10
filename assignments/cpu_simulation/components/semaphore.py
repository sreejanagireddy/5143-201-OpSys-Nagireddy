#!/usr/bin/python
"""

class: semaphore
attributea:count (int):semophore count
"""

from sim_components import *
import os
import math
import sys
class Semaphore():
    def __init__(self,count):
        self.count = count
        self.queue = deque()