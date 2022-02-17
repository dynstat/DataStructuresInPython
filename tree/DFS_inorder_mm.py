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
    def __init__(self, rootNode: Node):
        self.rootNode = rootNode

    def in_trav(self):
        self.inorder_traversal(self.rootNode)

    # ---------------------------------------------------------------------------------
    # or if you want to run this without parameter, use self.rootNode instead of rootNode and self.rootNode.inorder_traversal()
    def inorder_traversal(self, rootNode):
        if rootNode is None:
            return

        self.inorder_traversal(rootNode.left)
        print(rootNode.value, end=" ")
        self.inorder_traversal(rootNode.right)

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
    bTree1.in_trav()
    print("\n")
    bTree1.insert(root, 12)
    bTree1.in_trav()
# -----------------------------------------OVER-----------------------------------------------
