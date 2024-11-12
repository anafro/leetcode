# ----------------------------
# Category: Easy
# Leetcode link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# ----------------------------
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        number = 0
        cursor = head

        while cursor is not None:
            bit = cursor.val
            number += bit

            if cursor.next is not None:
                number <<= 1

            cursor = cursor.next

        return number


head = ListNode(1, ListNode(0, ListNode(1)))
print(Solution().getDecimalValue(head))