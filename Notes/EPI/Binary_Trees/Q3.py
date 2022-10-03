
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

root = Node(1,Node(2),Node(2))

def LCA(root, val_a, val_b):
    if root == None:
        return 0,None
    left_subtree = LCA(root.left, val_a, val_b)
    if left_subtree[0] == 2:
        return left_subtree
    right_subtree = LCA(root.right, val_a, val_b)
    if right_subtree[0] == 2:
        return right_subtree
    num_nodes = left_subtree[0] + right_subtree[0] + root == left_subtree +\
                                                     root == right_subtree
    return num_nodes, root if num_nodes == 2 else None




