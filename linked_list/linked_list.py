# linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    def traverse_list(self):
        temp = self.head
        while(temp != None):
            print(temp.data)
            temp = temp.next

    def pushh(self, new_value):     # linkedlist1.pushh(3)
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

    def appendd(self, new_value):  # linkedlist1.appendd(96)
        node_to_join = Node(new_value)

        # case 1 : if the linked list is Empty
        if self.head is None:
            self.head = node_to_join
            return

        # case 2 : if the linked list is NOT Empty
        temp = self.head
        # now temp (as well as self.head)  is pointing to the first Node object
        while(temp.next != None):
            temp = temp.next
        temp.next = node_to_join


if __name__ == '__main__':

    # creating three nodes of Node() class
    first_node = Node(10)
    second_node = Node(50)
    third_node = Node(99)

    new_linkedList = Linked_list()  # created an object of linked list

    new_linkedList.head = first_node
    first_node.next = second_node
    second_node.next = third_node
    print("Initial values in linked list")
    new_linkedList.traverse_list()
    list_to_add = [12, 45, 67, 89, 90, 112, 130, 150, 180]
    for i in list_to_add:
        new_linkedList.appendd(i)
    print("values in linked list after appending")
    new_linkedList.traverse_list()
