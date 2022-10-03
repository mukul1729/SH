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
from time import time
import random
import bisect
import copy
from binarytree import Node
from binarytree import *
import array
# Python3 implementation of the approach

# Function to print the intersection
def findIntersection(intervals,N):

	# First interval
	l = intervals[0][0]
	r = intervals[0][1]

	# Check rest of the intervals
	# and find the intersection
	for i in range(1,N):

		# If no intersection exists
		if (intervals[i][0] > r or intervals[i][1] < l):
			print(-1)

		# Else update the intersection
		else:
			l = max(l, intervals[i][0])
			r = min(r, intervals[i][1])
		
	

	print("[",l,", ",r,"]")

# Driver code

intervals= [
			[ 1, 2 ],
			[ 2, 3 ],
			[ 1, 3 ]
			]
N =len(intervals)
findIntersection(intervals, N)

# this code is contributed by mohit kumar

