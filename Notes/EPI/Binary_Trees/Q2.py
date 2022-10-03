"""
Question 2 - Test if binary tree is symmetric
"""

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

root = Node(1,Node(2),Node(2))

def IsSymmetric(root):
    return root == None or CheckSymmetry(root.left, root.right)


def CheckSymmetry(subtree_0, subtree_1):
    if subtree_0 == None and subtree_1 == None:
        return True
    elif subtree_0!=None and subtree_1!=None:
        return subtree_0.data == subtree_1.data and \
                CheckSymmetry(subtree_0.left, subtree_1.right) and \
                CheckSymmetry(subtree_0.right, subtree_1.left)
    return False


print(IsSymmetric(root))
