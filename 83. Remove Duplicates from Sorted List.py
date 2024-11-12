# ----------------------------
# Category: Easy
# Leetcode link: https://leetcode.com/problems/remove-duplicates-from-sorted-list
# ----------------------------
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {str(self.next)}"


def append(node: Optional[ListNode], element: int) -> ListNode:
    new_node = ListNode(element)

    if node is not None:
        node.next = new_node

    return new_node


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        result = None
        result_cursor = result
        cursor = head
        unique_element = None

        while cursor is not None:
            current_element = cursor.val

            if unique_element != current_element:
                unique_element = current_element
                result_cursor = append(result_cursor, unique_element)

                if result is None:
                    result = result_cursor

            cursor = cursor.next

        return result


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)

    print(Solution().deleteDuplicates(head))
