from sys import stdin
from collections import Counter,defaultdict,deque
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
import copy

v,e = map(int,input().split())
graph = [0 for i in range(v)]
edge = {i:[] for i in range(v)}
for _ in range(e):
    a,b = map(int,input().split())
    edge[a].append(b)
    graph[b] += 1
ans = deque([])
for i in range(v):
    if graph[i] == 0:
        ans.append(i)
while len(ans)!=0:
    x = ans.popleft()
    print(x)
    for i in edge[x]:
        graph[i]-=1
        if graph[i] == 0:
            ans.append(i)
