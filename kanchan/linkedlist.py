class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    def Traversal(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while(temp != None):
            print(temp.data)
            temp = temp.next

    def add_start_node(self, value):
        newnode = Node(value)
        temp = self.head
        self.head = newnode
        newnode.next = temp

    def add_position(self, position, value):
        newnode = Node(value)
        temp = self.head
        count = 1
        while(temp != None):
            count += 1
            if count == position:
                newnode.next = temp.next
                temp.next = newnode
                return

            temp = temp.next
        print("Not found")

    def add_last(self, value):
        newnode = Node(value)
        temp = self.head
        while(True):
            if temp.next == None:
                temp.next = newnode
                return
            temp = temp.next


if __name__ == "__main__":
    node1 = Node(4)
    node2 = Node(5)
    node3 = Node(6)

    list1 = Linked_list()

    list1.head = node1
    node1.next = node2
    node2.next = node3

    list1.Traversal()

    print()

    # list1.start_node(9)
   # list1.add_position(2, 56)
    list1.add_last(22)
    list1.Traversal()
