# Not creating a LinkedList class, and creating global functions to use LinkedList
# CHECK the head address, when the list is empty and filled
# The address of head is changed when list is empty, but doesnt change when list is filled
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f'{str(self.data)} at {id(self.data)}'

    def __str__(self) -> str:
        return self.__repr__()


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
    count = 1
    print(f"head {count}--> {id(head)}")
    newNode = Node(val)
    print(f"newNode {count}--> {id(newNode)}")
    if head is None:
        print(f"head {count}--> {id(head)}")
        print(f"newNode {count}--> {id(newNode)}")
        head = newNode
        print(f"head just before returning {count}--> {id(head)}")
        return head
    temp = head
    while(True):
        print(f"temp {count}--> {id(temp)}")
        if temp.next is None:
            temp.next = newNode
            print(f"head just before returning {count}--> {id(head)}")
            break
        temp = temp.next
        count += 1
    # return head


if __name__ == "__main__":

    one = Node(5)
    two = Node(6)
    three = Node(7)

    LinkedList_head = one   # <------ make it None to empty the list
    one.next = two
    two.next = three
    print("----------Printing List--------------")
    print_list(LinkedList_head)
    print(f"\nLinkedlist_head id = {id(LinkedList_head)}")
    print("++++++++ adding 8 to the list +++++++++")
    add_last(LinkedList_head, 8)

    # LinkedList_head = add_last(LinkedList_head, 8)  # <---FIX
    print("----------Printing List--------------")
    print_list(LinkedList_head)
    print(f"\nLinkedlist_head id = {id(LinkedList_head)}")
