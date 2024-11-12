# ----------------------------
# Category: Easy
# Leetcode link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# ----------------------------
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def propagate_height_calculation(node: Optional[TreeNode], relative_height: int = 0) -> int:
            if node is None:
                return relative_height

            return max(
                propagate_height_calculation(node.left, relative_height + 1),
                propagate_height_calculation(node.right, relative_height + 1),
            )

        return propagate_height_calculation(root)