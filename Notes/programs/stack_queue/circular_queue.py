from sys import stdin
from collections import deque,Counter,defaultdict,OrderedDict
import sys
import math,os
import operator
import random
from fractions import Fraction
import functools
import bisect
import itertools
from heapq import *
from time import time
import random
import bisect
import copy
from binarytree import Node
import array


class queue:
    CAPACITY = 10
    def __init__(self):
        self.data = [None]*queue.CAPACITY
        self.size = 0
        self.front = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self.data[self.front]

    def deque(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        ans = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front+1)%len(self.data)
        self.size-=1
        return ans

    def enqueue(self,e):
        if self.size == len(self.data):
            self.resize(2*len(self.data))
        avail = (self.front+self.size)%len(self.data)
        self.data[avail] = e
        self.size += 1

    def resize(self,cap):
        old = self.data
        self.data = [None]*cap
        walk = self.front
        for k in range(self.size):
            self.data[k] = old[walk]
            walk = (walk+1)%len(old)
        self.front = 0

q = queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.deque())
print(q.deque())
print(q.deque())
