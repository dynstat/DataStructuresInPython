# 143. Reorder List
# Medium

# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln

# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

# You may not modify the values in the list's nodes. Only nodes themselves may be changed.


# Example 1:

# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Example 2:

# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self, head=None):
        self.head = head

    def reorder(self, head):
        temp = self.head
        n2 = temp.next
        pointer = self.head
        while pointer:
            if pointer is None:
                pointer = temp.next
                n2 = pointer
            pointer = pointer.next

    def Traversal(self):
        count = 0
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while(temp != None):
            print(temp.data)
            count += 1
            temp = temp.next
        print(f"Total number of nodes {count}")


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    # node4.next = None

    linkedlist = Linked_list(head)
    linkedlist.reorder(head)
    # linkedlist.Traversal()
