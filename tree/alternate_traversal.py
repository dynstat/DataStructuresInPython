
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def alt_print_tree(root, level=1):
    if root is not None:
        if root.left is not None and root.right is not None:
            if (level+1) % 2 == 0:
                print(
                    f"Level {level +1}--> left {root.left.data}, right {root.right.data}")
        alt_print_tree(root.left, level+1)
        alt_print_tree(root.right, level+1)


# a function to print nodes in zigzag pattern from top to bottom
def zigzag(root):
    if root:
        print(root.data)
        if root.left:
            print(root.left.data)
            if root.left.right:
                zigzag(root.left.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.left = Node(12)
    root.right.left.right = Node(13)
    root.right.right.left = Node(14)
    root.right.right.right = Node(15)

    # alt_print_tree(root)
    zigzag(root)
