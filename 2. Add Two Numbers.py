# ----------------------------
# Category: Medium
# Leetcode link: https://leetcode.com/problems/add-two-numbers/description/
# ----------------------------
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        zero: ListNode = ListNode(0)
        overflow: int = 0
        first_digit: ListNode = l1
        second_digit: ListNode = l2
        sum: ListNode = ListNode(0)
        previous_sum_digit: Optional[ListNode] = None
        sum_digit: ListNode = sum

        while first_digit is not None or second_digit is not None or overflow != 0:
            digit_sum = (first_digit or zero).val + (second_digit or zero).val
            sum_digit.val = (digit_sum + overflow) % 10
            overflow = (digit_sum + overflow) // 10
            next_sum_digit: ListNode = ListNode(0)
            previous_sum_digit = sum_digit
            sum_digit.next = next_sum_digit
            sum_digit = next_sum_digit
            first_digit = (first_digit or zero).next
            second_digit = (second_digit or zero).next

        if sum_digit.val == 0 and previous_sum_digit is not None:
            previous_sum_digit.next = None

        return sum
