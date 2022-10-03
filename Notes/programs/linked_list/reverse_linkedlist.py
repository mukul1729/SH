class node:
    def __init__(self,data,next):
        self.data = data
        self.next = next


d = node(5,None)
c = node(4,d)
b = node(3,c)
a = node(2,b)
l = node(1,a)

# iterative
pre = None
curr = l
while curr:
    nxt = curr.next
    curr.next = pre
    pre = curr
    curr = nxt
head = pre
while head:
    print(head.data)
    head = head.next

# recursive
def reverse(head):
    if head == None:
        return head
    if head.next == None:
        return head
    new = reverse(head.next)
    head.next.next = head
    head.next = None
    return new

a = reverse(l)
while a:
    print(a.data)
    a = a.next
