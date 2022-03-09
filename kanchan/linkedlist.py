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

    def start_node(self, value):
        newnode = Node(value)
        temp = self.head
        self.head = newnode
        newnode.next = temp


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

    list1.start_node(9)

    list1.Traversal()
