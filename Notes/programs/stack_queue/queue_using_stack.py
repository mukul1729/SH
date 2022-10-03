from sys import stdin
from collections import deque,Counter,defaultdict
import sys
import math,os
import operator
import random
from fractions import Fraction
import functools
import bisect
import itertools
from heapq import *
import time
import random


class queue:
    def __init__(self):
        self.tail = []
        self.head = []

    def __len__(self):
        return len(self.head) + len(self.tail)

    def push(self,e):
        self.tail.append(e)

    def pop(self):
        if self.head == []:
            self.head = self.tail[::-1]
            self.tail = []
        return self.head.pop()

q = queue()
q.push(1)
q.push(2)
q.push(3)
print(q.pop())
print(q.pop())
print(q.pop())
