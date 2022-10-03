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

s = input()
ans = ''
w = 0
o = 0
for i in s:
    if i == 'v':
        w+=1
    elif i == 'o':
        ans = ans + 'w'*(w-1)+'o'
        w=0
ans = ans + 'w'*(w-1)+'o'

def count(x,y):
    (m,n) = len(x),len(y)
    t = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        t[i][0] = 1
    for i in range(1,m+1):
        for j in range(1,n+1):
            t[i][j] = (t[i-1][j-1] if (x[i-1] == y[j-1]) else 0) + t[i-1][j]
    return t[m][n]
print(count(ans,'wow'))
