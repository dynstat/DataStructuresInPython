#  To find whether the given linked list is cyclic or not
# given linked list --> [2,3,5,6,-1,5]


class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None

    def __repr__(self) -> str:
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head: Node = None

    # the address storing method
    def isCyclic(self):
        empty_set: set = set()  # creating an empty set
        temp = self.head
        while temp:
            temp_address = id(temp)
            if temp_address not in empty_set:
                empty_set.add(temp_address)
            else:
                return True
            temp = temp.next
        return False

    # using two pointer method
    def is_Cyclic(self):
        if self.head is None:
            return False
        s = self.head
        f = self.head
        while f:
            if s.next is None:
                return False
            s = s.next

            if f.next is None:
                return False
            f = f.next.next
            if f == s:
                return True
        return False


# driver code
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
    Node4.next = Node2

    print(list1.is_Cyclic())
