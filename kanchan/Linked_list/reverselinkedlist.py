
class Node:
    def __init__(self, val):
        self.next = None
        self.value = val


class linked_list:
    def __init__(self, head=None):
        self.head = head
    # a function to reverse the linked list

    def reverse_list(self):
        current = self.head
        previous = None
        nxt = None
        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
        self.head = previous

    def Traverse(self):
        temp = self.head
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print()


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    linkedlist = linked_list(head)
    linkedlist.Traverse()
    linkedlist.reverse_list()
    linkedlist.Traverse()
