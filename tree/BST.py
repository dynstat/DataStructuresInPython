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
        y = root.right.data
        putValueInBST(y, val)
    else:
        putValueInBST(root.left.data, val)


# Working function
def working_putValueInBST(root, val):
    if root is None:
        return Node(val)
    elif val > root.data:
        root.right.data = working_putValueInBST(root.right.data, val)
    else:
        root.left.data = working_putValueInBST(root.left.data, val)
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


# a function to check whether the given tree is a BST or not (with additional info.. helpful for debug or understanding)
def check_BST(root):
    print(f"MAIN ROOT = {root.data}")
    # Wether the tree is empty or not
    if root is None:
        return True
    # check if  leaf Node i.e. the node without any child
    if root.left is None and root.right is None:
        # for debugging
        print(f"Both {root.data}.left and {root.data}.right are None")
        return True
    # check if the Node has only left child
    if root.left is not None and root.right is None:
        print(f"only left Node {root.left.data} exists ")  # for debugging
        if root.left.data < root.data:
            return check_BST(root.left)
    # check if the Node has only right child
    if root.right is not None and root.left is None:
        print(f"only right Node {root.right.data} exists ")  # for debugging
        if root.right.data > root.data:
            return check_BST(root.right)
    # two children confirmed, so check if left child data is lesser than root and right child data is greater than root
    if root.left.data < root.data and root.right.data > root.data:
        print(
            f"root = {root.data}, root.left = {root.left.data}, root.right = {root.right.data}")  # for debugging
        return(check_BST(root.left) and check_BST(root.right))

    return False


# main driver code
if __name__ == "__main__":
    val = 22  # value to add into the tree
    ##########################################
    # creating a Tree
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.left.right.left = Node(4)
    # ##########################################
    # print("Initial Tree")
    # print_tree(root)  # to print a tree
    # print("\nAfter putValueInBST:")

    # # Expecting the value to be added... but doesn't work
    # putValueInBST(root, val)
    # print_tree(root)
    # print("\nAfter working_putValueInBST:")
    # working_putValueInBST(root, val)
    # print_tree(root)
    # print("\nAfter put_val_manually:")
    # put_val_manually(root, val)
    # print_tree(root)
    # print("\n")

    # calling the function
    print(check_BST(root))
