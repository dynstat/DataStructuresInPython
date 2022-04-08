class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


linked_list_head = None

# to print data of a tree....


def Traverse(linked_list_head):
    temp = linked_list_head
    while(temp != None):
        print(temp.data)
        temp = temp.next

# a function to insert a node in the end of list.


def Last_add(linked_list_head, data):
    newnode = Node(data)
    temp = linked_list_head
    while(temp != None):

        if temp.next is None:
            temp.next = newnode
            break
        temp = temp.next


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    linked_list_head = None
    node1.next = node2
    node2.next = node3
    node3.next = node4

    print("before adding")
    Traverse(linked_list_head)
    print()
    Last_add(linked_list_head, 50)
    print("after adding")
    Traverse(linked_list_head)
