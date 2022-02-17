class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


tree_tuple = (
    (1, 3, None),
    2,
    ((None, 3, 4),
     5,
     (6, 7, 8)))
# print(len(tree_tuple))


# converting the nodes present in the form of tuple to the actual tree
def parse_tree(a_tuple_tree):
    if isinstance(a_tuple_tree, tuple) and len(a_tuple_tree) == 3:
        root = Node(a_tuple_tree[1])
        root.left = parse_tree(a_tuple_tree[0])
        root.right = parse_tree(a_tuple_tree[2])
    elif a_tuple_tree is None:
        # return None
        root = None
    else:
        root = Node(a_tuple_tree)
    return root


# printing a tree in a  cool way
def print_tree(someTree: Node, level=0):
    # whether the node is None or not
    if someTree is None:
        print(level * "\t"+"0")
        return
    # whether the node is a leaf or not
    elif (someTree.left is None and someTree.right is None):
        print("\t"*level+str(someTree.data))
    # Neither a leaf nor a None, i.e an balanced binary tree
    else:
        print_tree(someTree.right, level=level+1)
        print("\t"*level + str(someTree.data))
        print_tree(someTree.left, level=level+1)


store = []


# Converting a tree into a tuple form
def tree_to_tuple(rootNode: Node):
    global store
    if rootNode is None:
        return None
    if rootNode.left is None and rootNode.right is None:
        return rootNode.data

        # tree_to_tuple(rootNode.left)
        # print(rootNode.data)
        # tree_to_tuple(rootNode.right)
    to_append1 = tree_to_tuple(rootNode.left)
    to_append2 = rootNode.data
    to_append3 = tree_to_tuple(rootNode.right)
    tup = (to_append1, to_append2, to_append3)
    store.append(tup)  # just for testing (not a part of the code)
    return tup
    # print(store)


if __name__ == "__main__":
    tree1 = (parse_tree(tree_tuple))
    print_tree(tree1)
    r = tree_to_tuple(tree1)
    print(store)
    print(r)
