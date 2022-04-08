

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# to check whether a given tree is bst or not.


def is_binaryTree(root):
    if root is None:
        return True
    if root.left.data > root.data or root.right.data < root.data:
        return False

    if root.left.data < root.data and root.right.data > root.data:
        return (is_binaryTree(root.left)) and is_binaryTree(root.right)


def bst_search(data, root):
    if root is None:
        return "tree is empty"
    if data == root.data:
        return root.data
    if data < root.data:
        bst_search(root.left)
    if data > root.data:
        bst_search(root.right)


if __name__ == "__main__":
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)
    root.right.right = Node(14)

    # print(is_binaryTree(root))

    print(bst_search(6, root))
