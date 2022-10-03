from binarytree import *
root = None
for _ in range(7):
    n = int(input())
    if root == None:
        root = Node(n,None,None)
        head = root
    else:
        root = head
        while root:
            prev = root
            if n>root.val:
                root = root.right
            else:
                root = root.left
        if n<prev.val:
            prev.left = Node(n,None,None)
        else:
            prev.right = Node(n,None,None)
        root = head
print(head)
