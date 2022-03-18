# Not creating a LinkedList class, and creating global functions to use LinkedList

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# head of a linked List created
LinkedList_head = None


# a traversal function and passing the head of the linked list as its parameter
def print_list(head: Node):
    if head is None:
        print("List is Empty !!")
        return
    temp = head
    while(temp != None):
        print(temp.data, end="")
        temp = temp.next


# function to add a new node at the end of the Linkedlist
def add_last(head: Node, val: int):
    newNode = Node(val)
    if head is None:
        head = newNode
        return
    temp = head
    while(True):
        if temp.next is None:
            temp.next = newNode
            break
        temp = temp.next


if __name__ == "__main__":

    one = Node(5)
    two = Node(6)
    three = Node(7)

    LinkedList_head = one
    one.next = two
    two.next = three
    print_list(LinkedList_head)
    print()
    add_last(LinkedList_head, 8)
    print_list(LinkedList_head)
