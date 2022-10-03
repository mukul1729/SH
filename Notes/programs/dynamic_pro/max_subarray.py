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
from binarytree import *


a = [-1,4,5,-18,9,2]
m = [0]*(len(a))
m[0] = a[0]
for i in range(1,len(a)):
    m[i] = max(a[i],m[i-1]+a[i])
print(m)
