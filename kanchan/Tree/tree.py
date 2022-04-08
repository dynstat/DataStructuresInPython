class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

 # To print the nodes of tree


def inorder_traverse(root):
    if root:
        inorder_traverse(root.left)
        print(root.data)
        inorder_traverse(root.right)


def preorder_traversal(root):
    if root:
        print(root.data)
        preorder_traversal(root.left)
        preorder_traversal(root.right)


def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data)


# printing the nodes of alternate levels
def alternate_traversal(root, tree_depth=0, level=0):

    if root:
        count += 1
        alternate_traversal(root.left, count+1)
        print(count)
        if count % 2 == 0:
            print(root.data)
        alternate_traversal(root.right, count+1)


if __name__ == "__main__":

    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.left.right.left = Node(4)

    # postorder_traversal(root)
    # print(alternate_traversal(root))
