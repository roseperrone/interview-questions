'''
Find the lowest (nearest) common ancestor between two nodes
in a tree.
'''

class Node(object):
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def find_lca(tree, a, b):
    '''
    Find the lowest (nearests) common ancestor of a and b.

    We assume a and b exist in the tree.
    '''
    if tree == a:
        return a
    if tree == b:
        return b

    a_left = is_child(a, tree.left)
    b_left = is_child(b, tree.left)
    if a_left and b_left:
        return find_lca(tree.left, a, b)
    if a_left or b_left:
        return tree
    return find_lca(tree.right, a, b)



