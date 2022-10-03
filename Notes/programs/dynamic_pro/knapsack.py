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

'''
6 15
6 5
5 6
6 4
6 6
3 5
7 2
'''

n,W = map(int,input().split()) #n,Max weight allowed
w = [0] #weights
v = [0] # values
for _ in range(n):
    i,j = map(int,input().split())
    w.append(i)
    v.append(j)

dp = [[0 for i in range(W+1)] for j in range(n+1)]
for i in range(n+1):
    for j in range(W+1):
        if j<w[i]:  # current weight is bigger 
            dp[i][j] = dp[i-1][j] # take value from previous row
        else:
            dp[i][j] = max(dp[i-1][j],v[i]+dp[i-1][j-w[i]]) # check if previous value is 
            # bigger or add value to knapsack and reduce the current weight by w[i]    
print(dp[n][W])

