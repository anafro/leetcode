# ----------------------------
# Category: Easy
# Leetcode link: https://leetcode.com/problems/valid-parentheses/description/
# ----------------------------
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None

        merge_list = ListNode()
        merge_cursor = merge_list
        first_cursor = list1
        second_cursor = list2

        while first_cursor is not None or second_cursor is not None:
            if first_cursor is not None and second_cursor is not None:
                first = first_cursor.val
                second = second_cursor.val

                if first < second:
                    merge_cursor.val = first
                    first_cursor = first_cursor.next
                else:
                    merge_cursor.val = second
                    second_cursor = second_cursor.next
            elif first_cursor is not None:
                merge_cursor.val = first_cursor.val
                first_cursor = first_cursor.next
            elif second_cursor is not None:
                merge_cursor.val = second_cursor.val
                second_cursor = second_cursor.next

            if first_cursor is not None or second_cursor is not None:
                merge_cursor.next = ListNode()
                merge_cursor = merge_cursor.next

        return merge_list