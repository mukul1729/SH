from sys import stdin
from collections import deque,Counter,defaultdict
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

least_bit = lambda x: x & -x


def subset_masks(m):
    while m:
        m&=(m-1)
        print(m)


def next_mask(x):
    c = least_bit(x)
    r = x + c
    return (((r ^ x) >> 2) // c) | r


def sum_of_subsets(K, D):
    for b in range(K):
        for i in range(1 << K):
            if i & 1 << b:
                D[i] += D[i ^ (1 << b)]

def calc(m):
    i = 0
    ans = []
    while (1<<i)<=m:
        if ((m>>i)&(1))==1:
            ans.append(1<<i)
        i+=1
    return ans

m = 10**5
two = []
i = 1
while (1<<i)<=m:
    two.append(1<<i)
    i+=1
num,limit = map(int,input().split())
i = bisect_right(two,num)
print(two[i])
