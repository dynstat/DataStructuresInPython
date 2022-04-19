# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

#######################################################################
# Solution

class ListNode:
    def __init__(self, val):
        self.val = val
        self.nxt = None

    def __repr__(self) -> str:
        return f"{str(self.val)} {id(self)}"


# traverse function for the linkedList
def print_list(head):
    if head is None:
        print("List is Empty !!")
        return
    temp = head
    while(temp != None):
        print(temp.val, end="->")
        temp = temp.nxt
    print(None)


def list_merger(list1: ListNode, list2: ListNode):
    newhead = None
    temp1 = list1
    temp2 = list2
    newhead_temp = newhead
    while temp1 and temp2:
        if temp1.val <= temp2.val:
            if newhead is None:
                newhead = temp1
                newhead_temp = newhead
            else:
                newhead_temp.nxt = temp1
                newhead_temp = newhead_temp.nxt
            temp1 = temp1.nxt
        else:
            if newhead is None:
                newhead = temp2
                newhead_temp = newhead
            else:
                newhead_temp.nxt = temp2
                newhead_temp = newhead_temp.nxt
            temp2 = temp2.nxt
        # if newhead_temp.nxt:
        #     newhead_temp = newhead_temp.nxt
    if temp1:
        newhead_temp.nxt = temp1
    elif temp2:
        newhead_temp.nxt = temp2
    return newhead


# driver code
if __name__ == "__main__":
    # Nodes for the 1st linked list
    l11 = ListNode(val=1)
    l12 = ListNode(val=2)
    l13 = ListNode(val=4)

    # Nodes for the 2nd linked list
    l21 = ListNode(val=1)
    l22 = ListNode(val=3)
    l23 = ListNode(val=4)
    # 1st linked list
    head1 = l11
    l11.nxt = l12
    l12.nxt = l13
    # 2nd linked list
    head2 = l21
    l21.nxt = l22
    l22.nxt = l23

    the_newhead = list_merger(head1, head2)
    print_list(the_newhead)
