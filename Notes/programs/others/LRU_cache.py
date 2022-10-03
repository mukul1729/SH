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

class cache:
    class node:
        def __init__(self,key,value,prev=None,next=None):
            self.key = key
            self.value = value
            self.prev = prev
            self.next = next

    def __init__(self,size):
        self.size = size
        self.d = Counter()
        self.head = self.node(None,None,None)
        self.tail = self.node(None,None,None)

    def get_val(self,key):
        lnode = self.d[key]
        if lnode == None:
            return None
        if lnode!=self.head:
            self.removeFromList(lnode)
            self.insertAtFrontOfList(lnode)
        return lnode.value

    def removeFromList(self,node):
        if node == None:
            return
        if node.prev!=None:node.prev.next = node.next
        if node.next!=None:node.next.prev = node.prev
        if node==self.tail:self.tail = node.prev
        if node==self.head:self.head = node.next

    def insertAtFrontOfList(self,node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def removeKey(self,key):
        if key not in self.d:
            self.removeFromList(None)
        else:
            self.removeFromList(self.d[key])
            del self.d[key]
        return True

    def setKeyValue(self,key,value):
        self.removeKey(key)
        if len(self.d)>=self.size and self.tail!=None:
            self.removeKey(self.tail.key)
        node = self.node(key,value)
        self.insertAtFrontOfList(node)
        self.d[key] = node



a = cache(10)
a.setKeyValue(1,3)
a.setKeyValue(2,3)
print(a.get_val(1))
print(a.d)
