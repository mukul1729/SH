import copy
import sys
import random

class node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

def lst_generator(length,start,end,unique=False,sort=False):
    if sort == False:
        lst1 = None
        un = set()
        i = 0
        while i<length:
            num = random.randint(start,end)
            if unique == True:
                if num in un:
                    continue
            un.add(num)
            lst1 = node(num,lst1)
            i+=1
        return lst1
    else:
        arr = sorted([random.randint(start,end+1) for i in range(length)])
        head = None
        while len(arr)>0:
            new = node(arr[0],None)
            if head == None:
                head = new
                h1 = head
            else:
                head.next = new
                head = new
            arr = arr[1:]
        return h1

def flush(lst):
    print('---')
    while lst:
        print(lst.data)
        lst = lst.next
    print('---')

def reverse(head):
    dummy_head = sublist_head = node(None, None)
    sublist_iter = sublist_head.next
    while head:
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp
    return dummy_head.next

dumb = l1 = lst_generator(7,1,20,True,False)
print(flush(reverse(l1)))

p1 = copy.deepcopy(l1)
l2 = lst_generator(3,1,20,True,True)
p2 = copy.deepcopy(l2)

f = node(6,None)
e = node(5,f)
d = node(4,e)
c = node(3,d)
b = node(2,c)
a = node(1,b)





k = 3
def shift(a,k):
    temp = [node(0,None),node(0,None)]
    turn = 0
    while a!=None:
        temp[turn].next = a
        temp[turn] = temp[turn].next
        a = a.next
        turn^=1

less = node(None,None)
head = less
equal = node(None,None)
greater = node(None,None)
pika = greater

head = l2 = lst_generator(5,1,1000,True,True)
merge = node(None,None)
tail = merge

while (l1 and l2):
    if l1.data < l2.data:
        tail.next, l1 = l1, l1.next
    else:
        tail.next, l2 = l2, l2.next
    tail = tail.next
tail.next = l1 or l2




while l1:
    first = l1
    while first and first.data == l1.data:
        first = first.next
    l1.next = first
    l1 = first

#print("----")
