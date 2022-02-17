class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print("List is Empty !!")
            return
        temp = self.head
        while(temp != None):
            print(temp.data)
            temp = temp.next

    def add_last(self, val):
        newNode = Node(val)
        if self.head is None:
            return
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = newNode

    def delete(self, val_to_del):
        pass


if __name__ == "__main__":
    list1 = LinkedList()

    one = Node(5)
    two = Node(6)
    three = Node(7)

    list1.head = one
    one.next = two
    two.next = three
