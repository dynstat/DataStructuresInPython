from ast import Global


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def Traverse(root):
    if root:
        print(root.data)
        Traverse(root.left)
        Traverse(root.right)


def print_tree(someTree: Node, level=0):
    # whether the node is None or not
    if someTree is None:
        print(level * "\t"+"0")
        return
    # whether the node is a leaf or not
    elif (someTree.left is None and someTree.right is None):
        print("\t"*level+str(someTree.data))
    # Neither a leaf nor a None, i.e an balanced binary tree
    else:
        print_tree(someTree.right, level=level+1)
        print("\t"*level + str(someTree.data))
        print_tree(someTree.left, level=level+1)


def insert_bst(root, val):
    newnode = Node(val)
    if root is None:
        global R
        R = newnode

    if root:
        if val > root.data:
            if root.right is None:
                root.right = newnode
                return
            insert_bst(root.right, val)

        if val < root.data:
            if root.left is None:
                root.left = newnode
                return
            insert_bst(root.left, val)


if __name__ == "__main__":
    R = None
    #R = Node(25)
    insert_bst(R, 25)
    insert_bst(R, 30)
    insert_bst(R, 56)
    insert_bst(R, 21)
    print_tree(R)
