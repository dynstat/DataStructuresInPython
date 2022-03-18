# Binary Tree
# creating a Node for binary Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return str(self.data)

    def __str__(self) -> str:
        return self.__repr__()


def traverse(root):
    if root is None:
        return
    traverse(root.left)
    print(root.data, end=' ')
    traverse(root.right)


def add_new(root, value):
    if root is None:
        root = Node(value)
        return
    store = [root]
    while store:
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


# to find the depth of any binary tree
def depth(root):
    # creating an inner function
    def inner(root):
        if root is not None:
            return 1 + (max(inner(root.left), inner(root.right)))
        else:
            return 0
    ans = inner(root)
    return ans


# another method to find the depth of a binary tree
def depth_(root, level=0):
    if root is None:
        return level
    else:
        return max(depth_(root.left, level+1), depth_(root.right, level+1))


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    root.right.right.left = Node(7)

    # root.right.right = Node(9)
    # print(Node(7))
    # logic(root)
    # print("")
    # add_new(root, 15)
    # logic(root)
    depth_(root)
