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
1.1
Subset Sum
Problem 1.1 Given a set of n numbers ai sum up to M , and any K ≤ M , whether there is a 
subset of the numbers such that they sum up to (hit) K? We assume n might be as big as
1000, but M or K is not too big.
'''


a = [2,3,7] #denomination
K = 12 # subset sum or target
M = sum(a) 

def subset(a,K,M):
    m = [0]*(K+1)
    m[0] = 1
    for i in range(1,K+1):
        for j in range(len(a)):
            if i<=sum(a) and i>=a[j]: # i<=sum(a) if one coin can be choosed else remove
                m[i] |= m[i-a[j]]     # the statement if any no of coins is allowed
    return m

print(subset(a,K,M))

