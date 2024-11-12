# ----------------------------
# Category: Easy
# Leetcode link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# ----------------------------
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"({'<null>' if self.left is None else self.left} / {self.val} \\ {'<null>' if self.right is None else self.right})"


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        def propagate_bst_build(left: int = 0, right: int = len(nums) - 1) -> Optional[TreeNode]:
            if left > right:
                return None

            middle = (left + right) // 2
            root = TreeNode(nums[middle])
            root.left = propagate_bst_build(left, middle - 1)
            root.right = propagate_bst_build(middle + 1, right)

            return root

        return propagate_bst_build()


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7]
    print(Solution().sortedArrayToBST(numbers))
