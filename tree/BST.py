# creating a Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# My Function to insert a node in an already existing BST
# This doesn't add a node in the tree
def putValueInBST(root, val):
    if root is None:
        root = Node(val)
    elif val > root.data:
        y = root.right
        putValueInBST(y, val)
    else:
        putValueInBST(root.left, val)


# Working function
def working_putValueInBST(root, val):
    if root is None:
        return Node(val)
    elif val > root.data:
        root.right = working_putValueInBST(root.right, val)
    else:
        root.left = working_putValueInBST(root.left, val)
    return root


# This works as expected...
def put_val_manually(r, val):
    # Since the val will be = 7 here, so adding its Node at the right bottom of the tree.
    r.right.right = Node(val)


# inorder traversal
def print_tree(r):
    if r is None:
        return
    print_tree(r.left)
    print(r.data, end=' ')
    print_tree(r.right)


# main driver code
if __name__ == "__main__":
    val = 7  # value to add into the tree
    ##########################################
    # creating a Tree
    root = Node(5)
    root.left = Node(4)
    root.right = Node(6)
    # ##########################################
    print("Initial Tree")
    print_tree(root)  # to print a tree
    print("\nAfter putValueInBST:")

    # Expecting the value to be added... but doesn't work
    putValueInBST(root, val)
    print_tree(root)
    print("\nAfter working_putValueInBST:")
    working_putValueInBST(root, val)
    print_tree(root)
    print("\nAfter put_val_manually:")
    put_val_manually(root, val)
    print_tree(root)
    print("\n")
