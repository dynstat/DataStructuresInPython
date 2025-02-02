from pydantic import BaseModel, Field, ValidationError
from typing import Optional


class Node(BaseModel):
    value: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


class BST(BaseModel):
    # In pydantic, this is not a class attr, it is an instance attribute.
    root: Optional["Node"] = None

    # method of traversing the tree
    @staticmethod
    def inorder(node: Optional["Node"] = None):
        if node is None:
            return
        if node.left:
            BST.inorder(node.left)
        print(node.value, end=" ")
        if node.right:
            BST.inorder(node.right)

    def inorder_iterative(self, node: Optional["Node"] = None):
        print()
        # if the root node is None, no need to traverse, simply return
        if node is None:
            return

        # to traverse, the current is a temp node to be used.
        current = node
        # STACK data structure is being used as we will be appending some other (right node) values after appending root node
        # (and before the other parent nodes wich we were already appended to the stack).
        # therefore, since we are not printing or using the node values in the same order in which we are adding/appending them,
        # we need to use stack
        stack = []
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            print(f"{current.value}", end=" ")
            current = current.right

    def preorder(self, node: Optional["Node"]):
        if node is None:
            return
        print(f"{node.value}", end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    def preorder_iterative(self, node: Optional["Node"]):
        print()  ## next line character for separation of result
        stack = [node]

        while stack:
            current = stack.pop()
            print(f"{current.value}", end=" ")

            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

    def postorder(self, node: Optional["Node"]):  # left right ROOT
        # BASE CASE
        if node is None:
            return

        self.postorder(node.left)
        self.postorder(node.right)
        print(f"{node.value}", end=" ")


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
    # BST.inorder(bst.root)
    # bst.inorder_iterative(bst.root)
    # bst.preorder(root)
    # bst.preorder_iterative(root)
    bst.postorder(root)
