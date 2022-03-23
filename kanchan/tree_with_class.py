# tree with class
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class Tree:
    def __init__(self, root):
        self.root = root
# inorder traversal

    def inorder_Traversal(self, root):
        if root:
            self.inorder_Traversal(root.right)
            print(self.data)
            self.inorder_Traversal(root.left)

    def preorder_Traversal(self, root):
        if root:
            print(root.data)
            self.preorder_Traversal(root.left)
            self.preorder_Traversal(root.right)

    def postorder_Traversal(self, root):
        if root:
            self.postorder_Traversal(root.left)
            self.postorder_Traversal(root.right)
