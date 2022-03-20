class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def Traverse(root):
    if root:
        print(root.data)
        Traverse(root.left)
        Traverse(root.right)


def print_tree(someTree: Node, level=0):
    # whether the node is None or not
    if someTree is None:
        print(level * "\t"+".")
        return
    # whether the node is a leaf or not
    elif (someTree.left is None and someTree.right is None):
        print("\t"*level+str(someTree.data))
    # Neither a leaf nor a None, i.e an balanced binary tree
    else:
        print_tree(someTree.right, level=level+1)
        print("\t"*level + str(someTree.data))
        print_tree(someTree.left, level=level+1)


def insertion(root, val):
    newnode = Node(val)
    if root:

        if root.left is None and root.right is not None:
            root.left = newnode
            return
        if root.right is None and root.left is not None:
            root.right = newnode
            return
        if root.left is None and root.right is None:
            root.left = newnode
            return
        insertion(root.left, val)
        # insertion(root.right, val)


def insert(root, val):
    store = [root]
    newnode = Node(val)
    while (store):
        r = store.pop()
        if r is None:
            r = newnode
            return r
        if r.left is None:
            r.left = newnode
            break
        store.append(r.left)
        if r.right is None:
            r.right = newnode
            break
        store.append(r.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    #root.left.right.left = Node(10)
    # root.left.right.right = Node(11)
    # root.left.left.left = Node(8)
    # root.left.left.right = Node(9)
    root.right.left = Node(6)
    # root.right.right = Node(7)
    # root.right.left.left = Node(12)
    # root.right.left.right = Node(13)
    # root.right.right.left = Node(14)
    # root.right.right.right = Node(15)

    print("before insertion")
    print_tree(root)
    print("after insertion")
    # insertion(root, val=10)
    insert(root, val=10)
    print_tree(root)
