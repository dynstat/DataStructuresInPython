from pydantic import BaseModel, Field, ValidationError
from typing import Optional


class Node(BaseModel):
    value: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


class BST(BaseModel):
    root: Optional["Node"] = None

    # method of traversing the tree
    @staticmethod
    def inorder(node: Optional["Node"] = None):
        if node is None:
            return
        if node.left:
            BST.inorder(node.left)
        print(node.value)
        if node.right:
            BST.inorder(node.right)


if __name__ == "__main__":
    # Constructing the BST:

    #         50
    #        /  \
    #      30    70
    #     / \    / \
    #   20  40  60  80

    root = Node(value=50)
    root.left = Node(value=30)
    root.right = Node(value=70)
    root.left.left = Node(value=20)
    root.left.right = Node(value=40)
    root.right.left = Node(value=60)
    root.right.right = Node(value=80)

    bst = BST(root=root)
    BST.inorder(bst.root)
