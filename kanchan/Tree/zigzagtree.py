class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# to print data of tree in zig zig fashion.......


# Function to print tree nodes in zigzag pattern from top (root node) to bottom
def zig_zag(root):
    if root is not None:
        print(root.data)
        if root.left:
            print(root.left.data)
            if root.left.right:
                print(root.left.right.data)
                if root.left.right.left:
                    zig_zag(root.left.right.left)


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

    zig_zag(root)
