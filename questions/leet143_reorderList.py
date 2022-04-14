
from itertools import count


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return str(self.data)


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def traverse(self):
        count = 0
        if self.head is None:
            print("Linked List is Empty !!")
        else:
            temp = self.head
            while(temp != None):
                count += 1
                print(temp.data, end=" ")
                temp = temp.next
        print()
        return count

    def length(self):
        count = 0
        if self.head is None:
            print("Linked List is Empty !!")
        else:
            temp = self.head
            while(temp != None):
                count += 1
                temp = temp.next
        return count

    def reorder_list(self):
        c = self.head
        l = self.length()
        for i in range((l-1), 0, -2):
            n = c.next
            temp = c
            for _ in range(i):
                temp = temp.next
            r = temp
            c.next = r
            r.next = n
            c = n
            if i <= 2:
                c.next = None


if __name__ == "__main__":
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)

    the_head = one
    one.next = two
    two.next = three
    three.next = four
    four.next = five

    list1 = LinkedList(the_head)
    list1.traverse()
    list1.reorder_list()
    list1.traverse()

    # print("\n\n")
