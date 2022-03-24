# tree with class
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class Tree:
    def __init__(self, root):
        self.r = root
        root = None
# inorder traversal

    def inorder_wrapper_traversal(self):
        self.inorder_Traversal(self.r)

    def inorder_Traversal(self, root):
        if root:
            self.inorder_Traversal(root.left)
            print(root.data)
            self.inorder_Traversal(root.right)

    def preorder_Traversal(self, root):
        if root:
            print(root.data)
            self.preorder_Traversal(root.left)
            self.preorder_Traversal(root.right)

    def postorder_Traversal(self, root):
        if root:
            self.postorder_Traversal(root.left)
            self.postorder_Traversal(root.right)
            print(root.data)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.right.left = Node(8)
    tree1 = Tree(root)

    tree1.inorder_wrapper_traversal()
