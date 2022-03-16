# a perfect is a tree which has leafnodes at same level.

from ast import literal_eval


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

# to check the level of given node.


def level_finder(root, to_find, level=0):
    if to_find == root.data:
        print(f"node found at level = {level}")
        return level
    if root.left != None and root.right != None:
        print(f"child name {root.left.data} and {root.right.data}")
        return level_finder(root.left, to_find, level+1) + level_finder(root.right, to_find, level+1)
    if root.left != None and root.right is None:
        print(f"left child {root.left.data}")
        return level_finder(root.left, to_find, level+1)
    if root.right != None and root.left is None:
        print(f"right child {root.right.data}")
        return level_finder(root.right, to_find, level+1)
    print("returning 0")
    return 0


def find_level(root, to_find, level=0):
    if root.data == to_find:
        return level
    if root.left != None and root.right != None:
        return find_level(root.left, to_find, level+1)*find_level(root.right, to_find, level+1)
    if root.left != None and root.right is None:
        return find_level(root.left, to_find, level+1)
    if root.right != None and root.left is None:
        return find_level(root.right, to_find, level+1)
    return 1


def height_finder(root, val_search):
    depth = depth_tree(root)
    level = find_level(root, to_find=val_search, level=0)
    print("depth", depth)
    height = depth-level
    return height


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.right.left = Node(8)

    #depth = (depth_tree(root))
   # print(depth)

    #print(is_perfect_tree(root, depth, level=0))

    #print(level_finder(root, to_find=8, level=0))
    print(find_level(root, to_find=8, level=0))

    print(height_finder(root, 8))
