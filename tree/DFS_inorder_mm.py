# DFS in a binary tree using inorder-method
# creating root of the binary tree
class Node:
    def __init__(self, data):
        self.left = None
        self.value = data
        self.right = None

# ---------------------------------------------------------------------------------


# Creating a binaryTree class
class binary_tree:
    # in-order traversal i.e. L->r->R
    def __init__(self, rootNode: Node = None):
        self.rootNode = rootNode

    # ---------------------------------------------------------------------------------
    # or if you want to run this without parameter, create a wrapper function

    def inorder_traversal(self, rootNode):
        if rootNode is None:
            return

        self.inorder_traversal(rootNode.left)
        print(rootNode.value, end=" ")
        self.inorder_traversal(rootNode.right)

    # wrapper function for inorder_traversal
    def in_trav(self):
        self.inorder_traversal(self.rootNode)
    # ---------------------------------------------------------------------------------
    # to create a method without self, we need to override the method as Staticmethod

    @staticmethod
    def check_empty_left(rootNode):
        if rootNode.left is None:
            return True
        else:
            return False

    @staticmethod
    def check_empty_right(rootNode):
        if rootNode.right is None:
            return True
        else:
            return False

    # ---------------------------------------------------------------------------------
    # inserting  a new node the inorder way

    def insert(self, testTree, value):
        if testTree is None:
            testTree = Node(value)
            return
        flag = 1
        while flag:
            if self.check_empty_left(testTree):
                testTree.left = Node(value)
                flag = 0
            else:
                tempTree = testTree
                testTree = testTree.left
                if self.check_empty_right(tempTree):
                    tempTree.right = Node(value)
                    flag = 0
# ---------------------------------------------------------------------------------
    # method to insert a new node in inorder way

    def insert_inorder_recursive(self, rootNode, value):
        if rootNode is None:
            rootNode = Node(value)
            return
        if rootNode.left is None:
            rootNode.left = Node(value)
            return
        self.insert_inorder_recursive(rootNode.left, value)
        # if rootNode.right is None:
        #     rootNode.right = Node(value)
        #     return

    # wrapper function for insert_inorder_recursive method

    def insert_recur(self, value_to_add):
        self.insert_inorder_recursive(self.rootNode, value_to_add)
    # printing a tree in a  cool way

    def print_tree(self, rootNode: Node, level=0):
        # whether the node is None or not
        if rootNode is None:
            print(level * "\t"+".")
            return
        # whether the node is a leaf or not
        elif (rootNode.left is None and rootNode.right is None):
            print("\t"*level+str(rootNode.value))
        # Neither a leaf nor a None, i.e an balanced binary tree
        else:
            self.print_tree(rootNode.right, level=level+1)
            print("\t"*level + str(rootNode.value))
            self.print_tree(rootNode.left, level=level+1)

    def print_tree_wrapper(self):
        self.print_tree(self.rootNode)


# main driver code
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)

    # inorder_traversal(root)
    bTree1 = binary_tree(root)
    bTree1.print_tree_wrapper()  # printing tree

    print("\n")
    # inserting 12 as node, in the left most bottom of the tree
    bTree1.insert_recur(12)
    bTree1.print_tree_wrapper()  # printing tree
# -----------------------------------------OVER-----------------------------------------------
