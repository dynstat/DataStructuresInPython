#  To find whether the given linked list is cyclic or not
# given linked list --> [2,3,5,6,-1,5]


class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # the address storing method
    def isCyclic(self):
        khali_list: set = {}
        temp = self.head
        while temp:
            temp_address = id(temp)
            if temp_address not in khali_list:
                khali_list.add(temp_address)
            else:
                return True
            temp = temp.next
        return False
    # using two pointer method

    def is_cyclic(self):
        s = self.head
        f = self.head


if __name__ == "__main__":
    Node1 = Node(3)
    Node2 = Node(2)
    Node3 = Node(0)
    Node4 = Node(-4)

    list1 = LinkedList()

    #  create any linked list (either cyclic or not)
    list1.head = Node1
    Node1.next = Node2
    Node2.next = Node3
    Node3.next = Node4
    # Node4.next = Node2

    print(list1.isCyclic())
