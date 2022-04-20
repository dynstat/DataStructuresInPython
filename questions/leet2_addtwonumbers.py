# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

class ListNode:
    def __init__(self, val):
        self.val = val
        self.nxt = None


def addnumbers(list1: ListNode, list2: ListNode):
    newhead = None

    def createNum(head: ListNode):
        fullNumber = 0
        i = 1
        temp = head
        while temp:
            digit = temp.val
            fullNumber = digit * i + fullNumber
            temp = temp.nxt
            i = i*10
        return fullNumber
    first_num = createNum(list1)
    second_num = createNum(list2)
    # total number after adding numbers from both the given linked lists
    total = first_num+second_num
    temp2 = None
    # if both the list has element [0], [0] in them
    if total == 0:
        num = total % 10
        total //= 10
        # just adding this Node with newhead
        if newhead is None:
            newhead = ListNode(num)
            temp2 = newhead
        return newhead
    # joining rest of the nodes with the newhead using temp variable
    while total:
        num = total % 10
        total //= 10
        if newhead is None:
            newhead = ListNode(num)
            temp2 = newhead
            continue
        temp2.nxt = ListNode(num)
        temp2 = temp2.nxt
    return newhead

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


# driver code
if __name__ == "__main__":
    # Nodes for the 1st linked list
    l11 = ListNode(val=2)
    l12 = ListNode(val=4)
    l13 = ListNode(val=3)

    # Nodes for the 2nd linked list
    l21 = ListNode(val=5)
    l22 = ListNode(val=6)
    l23 = ListNode(val=4)
    # 1st linked list
    head1 = l11
    l11.nxt = l12
    l12.nxt = l13
    # 2nd linked list
    head2 = l21
    l21.nxt = l22
    l22.nxt = l23

    the_new_head = addnumbers(head1, head2)
    print_list(the_new_head)
