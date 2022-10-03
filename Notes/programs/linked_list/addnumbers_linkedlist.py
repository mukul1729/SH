# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# iterative solution
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        result_tail = result
        carry = 0
        while l1 or l2 or carry:
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            carry, out = divmod(val1+val2 + carry, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next


#recursive solution
class node:
    def __init__(self,data,next):
        self.data = data
        self.next = next


b = node(2,None)
a = node(9,b)
h1 = node(5,a)

f = node(4,None)
e = node(9,f)
d = node(9,e)
h = node(9,d)

def add(l1,l2,carry):
    result = node(None,None)
    value = carry
    if l1!=None:
        value+=l1.data
    if l2!=None:
        value+=l2.data
    result.data = value%10
    if l1!=None or l2!=None:
        more = add(None if l1 == None else l1.next,None if l2 == None else\
                l2.next,1 if value>=10 else 0)
        result.next = more
    return result


c = (add(h,h1,0))
while c:
    print(c.data)
    c = c.next
