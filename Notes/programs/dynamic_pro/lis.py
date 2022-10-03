from sys import stdin
from collections import deque,Counter,defaultdict
import sys
import math
import operator
import random
from fractions import Fraction
import functools
import bisect
import itertools
from heapq import *
import time
from binarytree import *

seq = [4,5,6,3,2,9,10,11]
n = len(seq)

m = [0]*(n)
m[0] = 1 #base case (first index = 1)
for i in range(1,n):
    m[i] = 1
    for j in range(0,i):
        if seq[j]<seq[i]:
            m[i] = max(m[i],m[j]+1)
print(m)

#output
[1, 2, 3, 0, 0, 4, 5, 6]
