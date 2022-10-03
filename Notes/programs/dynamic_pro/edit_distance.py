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
import time
import random
import bisect
import copy

'''
NEABJPJOI
RFMQRJKJKIA
'''
a = input()
b = input()
dp = [[0 for i in range(len(b)+1)] for j in range(len(a)+1)]
a = '0'+a
b = '0'+b
for i in range(1,len(a)):
    dp[i][0] = i
for i in range(1,len(b)):
    dp[0][i] = i
for i in range(1,len(a)):
    for j in range(1,len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] += 1+min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])
print(dp[len(a)-1][len(b)-1])

