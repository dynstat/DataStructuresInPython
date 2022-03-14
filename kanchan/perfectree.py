# a perfect is a tree which has leafnodes at same level.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# to find the depth of tree.


def depth_tree(root):
    count = 0
    while(root is not None):
        count += 1
        root = root.left
    return count-1

# to check a given tree is perfect binary tree


def is_perfect_tree(root, depth, level=0):
    if root is None:
        return True
    if root.left is None and root.right is None:
        if depth == level:
            return True
    if root.left is None or root.right is None:
        return False
    if root.left is not None and root.right is not None:
        return (is_perfect_tree(root.left, depth, level+1) and (is_perfect_tree(root.right, depth, level+1)))


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.right.left = Node(8)

    depth = (depth_tree(root))
    print(depth)

    print(is_perfect_tree(root, depth, level=0))
