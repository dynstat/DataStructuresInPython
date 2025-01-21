# File: tree_traversals.py:path/to/tree_traversals.py


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return f"({self.val})"

    def __repr__(self):
        return f"({self.val})"


def inorder_iterative(root):
    """
    Perform inorder traversal of a binary tree using iteration.
    """
    stack = []
    current = root

    while stack or current:
        while current:
            stack.append(current)  # Push current node to stack
            current = current.left  # Move to left child
        current = stack.pop()  # Pop node from stack
        print(current.val, end=" ")  # Visit node
        current = current.right  # Move to right child


# Example Usage:
if __name__ == "__main__":
    # Constructing the following Binary Tree:
    #         1
    #        / \
    #       2   3
    #      / \
    #     4   5

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print("\nIterative Inorder Traversal:")
    inorder_iterative(root)  # Output: 4 2 5 1 3
