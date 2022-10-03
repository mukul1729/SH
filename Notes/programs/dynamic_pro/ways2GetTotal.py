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


coins = [1,2,3]
num = 5

cost = [[0 for i in range(num+1)] for j in range(len(coins))]
for i in range(len(coins)):
    cost[i][0] = 1
for i in range(len(coins)):
    for j in range(1,num+1):
        if coins[i]>j:
            cost[i][j] = cost[i-1][j]
        else:
            cost[i][j] = cost[i-1][j] + cost[i][j-coins[i]]
print(cost)
