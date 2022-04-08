# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.


# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:

# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Example 3:

# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    def Traverse(self):
        temp = self.head
        khali_list = []
        while(temp != None):
            if id(temp) not in khali_list:
                khali_list.append(id(temp))
                temp = temp.next
            if id(temp) in khali_list:
                return True
        return False


if __name__ == "__main__":
    Node1 = Node(1)
    # Node2 = Node(2)
    # Node3 = Node(0)
    # Node4 = Node(-4)

    list1 = Linked_list()
    list1.head = Node1
    # Node1.next = Node2
    # Node2.next = Node3
    # Node3.next = Node4
    # Node4.next = Node2

    print(list1.Traverse())
