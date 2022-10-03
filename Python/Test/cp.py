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
#import binarytree


'''
n,m = map(int,input().split())
g = [[0 for i in range(0,m)] for j in range(0,n)]
for _ in range(m):
    a,b = map(int,input().split())
    g[a-1][b-1] = g[b-1][a-1] = 1

a = 0
v = [0 for i in range(n)]
v[a] = 1
s = [0]
while len(s)!= 0:
    vert = s.pop()
    print(vert)
    for i in range(n):
        if g[vert][i] == 1 and v[i] == 0:
            v[i] = 1
            s.append(i)

a = '(1+2)*(3+4)'
graph = {
    'A' : ['C','B'],
    'B' : ['E', 'D'],
    'C' : ['F'],
    'D' : ['G'],
    'E' : ['F'],
    'F' : [],
    'G': []
}

visit = set()
def dfs(graph,node,visit):
    a = deque([node])
    while len(a)!=0:
        p = a.popleft()
        print(p)
        for i in graph[p]:
            if i not in visit:
                visit.add(i)
                a.append(i)

graph = {
    'A' : ['C','B'],
    'B' : ['E', 'D'],
    'C' : ['F'],
    'D' : ['G'],
    'E' : ['F'],
    'F' : [],
    'G': []
}

start = 'A'
visit = set()

def dfs(graph,start,visit):
    a = [start]
    while a:
        p = a.pop()
        print(p)
        for i in graph[p]:
            if i not in visit:
                visit.add(i)
                a.append(i)

print(dfs(graph,start,visit))
def add() -> Env:
    return 10
from binarytree import *
arr = [1,2,3,4,5,6,7,8]
root  = None
a,b = 0,7
def maker(root,arr,a,b):
    if b < a:
        return None
    else:
        mid = (a+b)//2
        root = Node(arr[mid],None,None)
        root.left = maker(root,arr,a,mid-1)
        root.right = maker(root,arr,mid+1,b)
        return root
print(maker(root,arr,a,b))





edge = []
v,e = map(int,input().split())
for i in range(e):
    a,b,w = map(int,input().split())
    edge.append([a,b,w])
distance = [10000]*(v)
print(distance)
distance[0] = 0
distance[1] = 0
for i in range(0,v-1):
    for e in edge:
        a,b,w = e
        distance[b] = min(distance[b],distance[a]+w)
print(distance)
6 7
1 3 3
1 4 7
1 2 5
2 4 3
2 5 2
3 4 1
4 5 2


A
B
D
E
F
C

'''
class graph:
    def __init__(self,name):
        self.name = name
        self.children = []

arr = [[0,0,0],
        [0,0,0],
        [0,0,0]]

def available(val,arr,row):
    for i in range(2):
        if arr[row][i] == val:
            return 1
    return 0

def available1(val,arr,col):
    for i in range(2):
        if arr[i][col] == val:
            return 1
    return 0


def solve(arr,col):
    if col == 3:
        for i in arr:
            print(i)
    else:
        for row in range(3):
            if arr[row][col]!=0:
                solve(arr,col+1)
            else:
                a = [1,2,3,4,5,6,7,8,9]
                for i in a:
                    a1 = (available(i,arr,row))
                    a2 = (available1(i,arr,col))
                    if a1+a2  == 0:
                        arr[row][col] = i
                        solve(arr,col+1)
                        arr[row][col] = 0

from heapq import *
graph = defaultdict(dict)
class vertex:
    def __init__(self,node,weight):
        self.node = node
        self.weight = weight

graph = {1:(vertex(2,5),vertex(5,1),vertex(4,9)),
        2:(vertex(1,5),vertex(3,2)),
        3:(vertex(4,6),vertex(2,2)),
        4:(vertex(1,9),vertex(3,6),vertex(5,2)),
        5:(vertex(4,2),vertex(1,1))}

def dijkstra(graph,n=5):
    distance = [10000]*(n+1)
    distance[0] = 0
    distance[1] = 0
    q = []
    processed = set()
    heappush(q,(0,1))
    path = {}
    while len(q)!=0:
        a = heappop(q)[1]
        if a in processed:
            continue
        processed.add(a)
        for u in graph[a]:
            b = u.node
            w = u.weight
            if distance[a]+w<distance[b]:
                distance[b] = distance[a]+w
                path[b] = a
                heappush(q,(distance[b],b))
    return distance,path
path = (dijkstra(graph,5))[1]
print(path)

'''
from Binary_Search_Trees import BST as bst
from binarytree import tree

r = tree(height = 3,is_perfect = True)
root = bst.CreateBST()
bst.Insert(root,[4,1,2,7,5,9])

def isbst(root):
    if root.left== None or root.right == None:
        return True
    return root.val>root.left.val and root.val<root.right.val\
            and isbst(root.left) and isbst(root.right)

print(isbst(r))
'''
