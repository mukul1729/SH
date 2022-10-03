from sys import stdin
from collections import Counter,defaultdict,deque
import sys
import math
import os
import operator
import random
from fractions import Fraction
import functools
import bisect
import itertools
from heapq import *
import copy


p = 31
m = 10**9 + 9
s = 'kul'
t = 'jokingmukul'
p_pow = [0] * max(len(s),len(t))
p_pow[0] = 1
for i in range(1,len(p_pow)):
    p_pow[i] = (p_pow[i-1] * p) % m
h = [0]*(len(t)+1)
for i in range(len(t)):
    h[i+1] = (h[i] + (ord(t[i]) - 97)*p_pow[i])%m
h_s = 0
for i in range(len(s)):
    h_s = (h_s + (ord(s[i]) - 97)*p_pow[i])%m
for i in range(len(t)-len(s)+1):
    curr_h = (h[i+len(s)] - h[i])%m
    if curr_h == (h_s * p_pow[i])%m:
        print(i)
