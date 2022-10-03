from collections import deque
from math import *
import sys
import random
from bisect import *
from enum import Enum

class UnionFind:
    def __init__(self, n):
        self.link = [i for i in range(0,n+1)]
        self.size = [1 for i in range(0,n+1)]

    def find(self, x):
        while x != self.link[x]:
            x = self.link[x]
        return x

    def same(self, a, b):
        return self.find(a) == self.find(b)

    def unite(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if self.size[a] < self.size[b]:
            a,b = b,a
        self.size[a] += self.size[b]
        self.link[b] = a

n,m = map(int,input().split())
d = {i:0 for i in range(n+1)}
p = UnionFind(n)

for _ in range(m):
    a,b = map(int,input().split())
    d[a]+=1
    d[b]+=1
    if p.same(a,b):
        print("No")
        sys.exit()
    p.unite(a,b)

for i in d:
    if d[i] >2:
        print("No")
        sys.exit()
print("Yes")

'''
4 2
1 3
2 3
'''

