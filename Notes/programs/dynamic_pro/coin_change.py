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

denomination = [1,6,10]
amount = 12

def coin_change(amount,denomination):
    ans = [sys.maxsize]*(amount+1)
    ans[0] = 0
    for i in range(1,len(ans)):
        for j in range(len(denomination)):
            if denomination[j] <= i:
                ans[i] = min(ans[i], ans[i-denomination[j]]+1)
    return ans

print(coin_change(amount,denomination))

