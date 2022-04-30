# program to reverse a given linked list

class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None

    def __repr__(self) -> str:
        return str(self.value)


# 3 pointers (curr, prev, nxt), iterative method
def rev_LL(head: Node):
    if head is None:
        return None
    # creating 3 pointers
    curr = head
    prev = None
    nxt = curr.next

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev  # returning the last Node as it will be the starting point of this reversed linked list

# traverse function


def traverse(head: Node):
    temp = head
    while temp:
        print(temp.value, end=" ")
        temp = temp.next
    print()


# driver code
if __name__ == "__main__":
    the_head = None
    # creating Nodes using Node class
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)

    # creating a linked list
    the_head = one
    one.next = two
    two.next = three
    three.next = four
    traverse(the_head)
    # changing the_head (below) as it was still pointing to the Node "one" and rev_LL() made one to point to None
    the_head = rev_LL(the_head)
    traverse(the_head)
