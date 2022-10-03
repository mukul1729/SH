from binarytree import *

bst = Node(1,Node(2,Node(4,None,None),None),Node(3,Node(5,None,None),None))
print(bst)

def dfs(root):
    if root!=None:
        ans[root.val] = 1
        print(root.val)
        dfs(root.left)
        dfs(root.right)
        if root.left:
            ans[root.val]+=ans[root.left.val]
        if root.right:
            ans[root.val]+=ans[root.right.val]

ans = [0]*6
print(dfs(bst))
print(ans)
