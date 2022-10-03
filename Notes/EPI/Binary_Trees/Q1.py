"""
Question1 - Test if the binary tree is height balanced- for each node in the tree the diff
between right and left subtree is at most one

class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value  # The node value (float/int/str)
        self.left = left    # Left child
        self.right = right  # Right child

# Generate a random binary tree and return its root node.
my_tree = tree(height=3, is_perfect=False)

# Generate a random BST and return its root node.
my_bst = bst(height=3, is_perfect=True)

# Generate a random max heap and return its root node.
my_heap = heap(height=3, is_max=True, is_perfect=False)

my_tree = tree(height=3, is_perfect=False, letters=True)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(root)
#
#        __1
#       /   \
#      2     3
#     / \
#    4   5
#
print(root.inorder)
# [Node(4), Node(2), Node(5), Node(1), Node(3)]

print(root.preorder)
# [Node(1), Node(2), Node(4), Node(5), Node(3)]

print(root.postorder) 
# [Node(4), Node(5), Node(2), Node(3), Node(1)]

print(root.levelorder) 
# [Node(1), Node(2), Node(3), Node(4), Node(5)]

print(list(root)) # Equivalent to root.levelorder
# [Node(1), Node(2), Node(3), Node(4), Node(5)]

values = [7, 3, 2, 6, 9, None, 1, 5, 8]
root = build(values)

"""
from binarytree import *


def CheckBalanced(root):
    if root == None:
        return True,-1

    left_result = CheckBalanced(root.left)
    if not left_result[0]:
        return False,0

    right_result = CheckBalanced(root.right)
    if not right_result[0]:
        return False,0

    is_balanced = abs(left_result[1] - right_result[1])<=1
    height = max(left_result[1], right_result[1]) + 1
    return is_balanced,height


root = tree(height = 3, is_perfect=True)
print(root)
print(CheckBalanced(root))





























