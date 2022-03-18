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

    def insertt(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

    def insert_last(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while (True):
            if temp.next is None:
                temp.next = newNode
                break
            temp = temp.next

    def delete(self, val_to_del):
        temp = self.head
        if temp.data == val_to_del:
            self.head = temp.next
            return
        while(temp.next != None):
            if temp.next.data == val_to_del:
                temp.next = temp.next.next
                return
            temp = temp.next

        print(f"Element {val_to_del} Not Found is this list !!\n")


if __name__ == "__main__":
    one = Node(5)
    two = Node(19)
    three = Node(99)

    list1 = LinkedList()

    list1.head = one
    one.next = two
    two.next = three

    list1.traverse()
    print("\n\n")
    # list1.insertt(22)
    # list1.traverse()
    # print("\n\n")
    list1.insert_last(100)
    list1.traverse()
    print("\n\n")
    # list1.delete(1008493598)
    # list1.traverse()
    # print(locals(), '', '')
