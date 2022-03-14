class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

 # To print the nodes of tree


def inorder_traverse(root):
    if root:
        inorder_traverse(root.left)
        print(root.data)
        inorder_traverse(root.right)


def preorder_traversal(root):
    if root:
        print(root.data)
        preorder_traversal(root.left)
        preorder_traversal(root.right)


def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data)


if __name__ == "__main__":

    root = Node(1)
    root.left = Node(12)
    root.left.left = Node(5)
    root.left.right = Node(6)
    root.right = Node(9)

    postorder_traversal(root)
