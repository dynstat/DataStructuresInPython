# creating a Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# My Function to insert a node in an already existing BST, without returning the new/modified tree
def put_val_noReturn(r, val):
    if r is None:
        global root  # here, it is required to know the name of the global variable i.e. the root node of the tree
        root = Node(val)
        return
    if val < r.data:
        if r.left is None:
            newNode = Node(val)
            r.left = newNode
            return
        put_val_noReturn(r.left, val)
    else:
        if r.right is None:
            newNode = Node(val)
            r.right = newNode
            return
        put_val_noReturn(r.right, val)


# Working function, but requires to return the modified tree and to be placed into the "root" global variable
def working_putValueInBST(r, val):
    if r is None:
        return Node(val)
    elif val > root.data:
        r.right = working_putValueInBST(r.right, val)
    else:
        r.left = working_putValueInBST(r.left, val)
    return r


# inorder traversal
def inorder(r):
    def print_tree(r):
        if r is None:
            return "empty"
        print_tree(r.left)
        print(r.data, end=" ")
        print_tree(r.right)

    if print_tree(r) == "empty":
        print("List is empty!!")


# a function to check whether the given tree is a BST or not
def check_BST(root):
    def is_bst_util(node, min_val=float("-inf"), max_val=float("inf")):
        # Empty tree is a valid BST
        if node is None:
            return True

        # Check if current node's value is within valid range
        if node.data <= min_val or node.data >= max_val:
            return False

        # Recursively check left subtree (must be less than current node)
        # and right subtree (must be greater than current node)
        return is_bst_util(node.left, min_val, node.data) and is_bst_util(
            node.right, node.data, max_val
        )

    return is_bst_util(root)


# main driver code
if __name__ == "__main__":
    val = 200  # value to be added into the tree
    ##########################################
    # creating a Tree
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.left.right.left = Node(4)
    # root = None
    # ##########################################
    print("Initial Tree")
    inorder(root)  # to print a tree
    print("\nAfter inserting:")
    # Function to insert a value (node) into an appropriate location acc to BST
    put_val_noReturn(root, val)
    inorder(root)  # prining the tree again to see the changes
