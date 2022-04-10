# program to reverse a given linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head is None:
            print("Linked List is Empty !!")
        else:
            temp = self.head
            while(temp != None):
                print(temp.data)
                temp = temp.next

    def rev_linkedList(self):


if __name__ == "__main__":
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    list1 = LinkedList()

    list1.head = one
    one.next = two
    two.next = three
    three.next = four

    list1.traverse()
    print("\n\n")
