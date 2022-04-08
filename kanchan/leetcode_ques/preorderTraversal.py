# Given the root of a binary tree, return the preorder traversal of its nodes' values.


# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,2,3]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root):
        self.root = root
        self.empty_list = []

    def preorderTraverval(self, r):
        if r:
            self.empty_list.append(r.value)
            self.preorderTraverval(r.left)
            self.preorderTraverval(r.right)
        return self.empty_list


if __name__ == "__main__":
    # creating nodes for the tree
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    ##############################
    # Creating tree with the root node named as "root"
    root = node1
    node1.right = node2
    node2.left = node3
    ##############################

    # Creating Tree object and passing our created tree in it.
    tree_obj = Tree(root)
    print(tree_obj.preorderTraverval(root))
