# ----------------------------
# Category: Easy
# Leetcode link: https://leetcode.com/problems/symmetric-tree/
# ----------------------------
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def propagate_symmetric_comparison(node_a: Optional[TreeNode], node_b: Optional[TreeNode]) -> bool:
            if node_a is None or node_b is None:
                return node_a is node_b

            a = node_a.val
            b = node_b.val

            return a == b and propagate_symmetric_comparison(node_a.left, node_b.right) and propagate_symmetric_comparison(node_a.right, node_b.left)

        return propagate_symmetric_comparison(root.left, root.right)