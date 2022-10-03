from sys import stdin
from collections import Counter,defaultdict,deque
import sys
import math
import os
import operator
import random
from fractions import Fraction
import functools
import bisect
import itertools
from heapq import *
import copy
import sys

class Fenwick:
    def __init__(self, array):
        self.array = array
        self.size = len(self.array)
        self.fenwick = [0]*((self.size)+1)
        self.create()

    def update(self, i, v):
        i+=1
        while (i<=self.size):
            self.fenwick[i] += v
            i += (i& -i)

    def create(self):
        for i in range(self.size):
            self.update(i,self.array[i])

    def query(self, i):
        res = 0
        i += 1
        while i>0:
            res += self.fenwick[i]
            i -= (i & -i)
        return res

    def __str__(self):
        return ' '.join(map(str,self.fenwick))



n = int(input())
arr = list(map(int,input().split()))
f = Fenwick(arr)
