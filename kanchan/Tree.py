class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# inorder Traversal


def inorder_Traversal(root):
    if root is None:
        return
    inorder_Traversal(root.left)
    print(root.data)
    inorder_Traversal(root.right)


if __name__ == "__main__":
    root = Node(50)
    root.left = Node(55)
    root.right = Node(60)
    root.left.left = Node(65)
    root.right.left = Node(70)

    inorder_Traversal(root)
