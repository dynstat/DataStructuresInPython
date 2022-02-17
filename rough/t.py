class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return self.data


def putValueInBSTo(root, val):
    if root is None:
        return Node(val)
    elif val > root.data:
        y = root.right
        root.right = putValueInBSTo(root.right, val)
    else:
        root.left = putValueInBSTo(root.left, val)
    return root


root = Node(5)
root.left = Node(4)
root.right = Node(6)

putValueInBSTo(root, 7)
