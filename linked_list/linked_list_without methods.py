class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


LinkedList_head = None


def print_list(head: Node):
    if head is None:
        print("List is Empty !!")
        return
    temp = head
    while(temp != None):
        print(temp.data)
        temp = temp.next


def add_last(head: Node, val):


if __name__ == "__main__":

    one = Node(5)
    two = Node(6)
    three = Node(7)

    LinkedList_head = one
    one.next = two
    two.next = three
    print_list(LinkedList_head)
