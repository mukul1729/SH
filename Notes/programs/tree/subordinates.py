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
sys.setrecursionlimit(10**7)

def solve(tree,start,ans):
    ans[start] = 1
    for i in tree[start]:
        solve(tree,i,ans)
        ans[start] += ans[i]

n = int(input())
arr = list(map(int,input().split()))
tree = {i:[] for i in range(1,n+1)}
for i in range(2,len(arr)+2):
    tree[arr[i-2]].append(i)
ans = [0]*(n+1)
(solve(tree,1,ans))
ans = ans[1:]
print(*[i-1 for i in ans])

'''
input:
5
1 1 2 3
'''

