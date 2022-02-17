# Binary Tree
# creating a Node for binary Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return self.data

    def __str__(self) -> str:
        return self.__repr__()


def logic(root):
    if root is None:
        return
    logic(root.left)
    print(root.data, end=' ')
    logic(root.right)


def add_new(root, value):
    if root is None:
        root = Node(value)
        return

    store = []
    store.append(root)
    while (len(store) != 0):
        # store -- > [root]
        root = store.pop(0)
        # store -- > []
        if root.left is None:
            root.left = Node(value)
            break
        else:
            store.append(root.left)

        if root.right is None:
            root.right = Node(value)
            break
        else:
            store.append(root.right)
    # end of addnew function


if __name__ == "__main__":
    root = Node(7)
    root.left = Node(5)
    root.right = Node(4)
    root.left.left = Node(3)
    root.left.right = Node(2)
    root.right.left = Node(11)

    # root.right.right = Node(9)

    logic(root)
    print("")
    add_new(root, 15)
    logic(root)
