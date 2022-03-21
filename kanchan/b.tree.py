# full tree is a tree which has zero child nodes or two child.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# to check whether it is full tree or not?


def isfullTree(root):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    if root.left is not None and root.right is not None:
        return (isfullTree(root.left)) and (isfullTree(root.right))

    return False


def Inorder_traversal(root):
    if root:
        Inorder_traversal(root.left)
        print(root.data)
        Inorder_traversal(root.right)


if __name__ == "__main__":
    root = Node(56)
    root.left = Node(50)
    root.left.right = Node(65)
    root.left.left = Node(60)
    root.right = Node(55)
    root.right.left = Node(40)

    print(isfullTree(root))
