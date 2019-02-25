"""solution.py"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        T: O(?)
        S: O(?)
        """
        l3 = ListNode(0)
        temp_l3 = l3
        carry = 0
        while l1 or l2:
            l1v = 0 if l1 is None else l1.val
            l2v = 0 if l2 is None else l2.val

            sum_l1v_l2v_carry = l1v + l2v + carry
            if sum_l1v_l2v_carry > 9:
                carry = 1
                l3v = sum_l1v_l2v_carry%10
            else:
                carry = 0
                l3v = sum_l1v_l2v_carry

            temp_l3.next = ListNode(l3v)
            temp_l3 = temp_l3.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if carry != 0:
            temp_l3.next = ListNode(carry)

        return l3.next

        """
        T: O(?)
        S: O(?)
        """
        l3 = temp_l3 = ListNode(0)
        all_carry = 0
        while l1 or l2 or all_carry:
            if l1:
                all_carry += l1.val
                l1 = l1.next
            if l2:
                all_carry += l2.val
                l2 = l2.next

            temp_l3.next = ListNode(all_carry%10)
            temp_l3 = temp_l3.next
            all_carry = all_carry // 10

        return l3.next
