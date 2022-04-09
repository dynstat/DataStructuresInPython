# 142. Linked List Cycle II
# Medium

# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

# Do not modify the linked list.


# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.

# Example 2:

# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.

# Example 3:

# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.


# Constraints:

#     The number of the nodes in the list is in the range [0, 104].
#     -105 <= Node.val <= 105
#     pos is -1 or a valid index in the linked-list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self, head=None):
        self.head = head

    def cyclic_index(self):
        temp = self.head
        empty_list = set()

        while temp:
            temp_address = id(temp)
            if temp_address in empty_list:
                return temp
            empty_list.add(temp_address)
            temp = temp.next


if __name__ == "__main__":
    node1 = Node(3)
    node2 = Node(2)
    node3 = Node(0)
    node4 = Node(4)

    head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2

    list1 = Linked_list(head)
    print(list1.cyclic_index())
