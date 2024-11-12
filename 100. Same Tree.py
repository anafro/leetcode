# ----------------------------
# Category: Easy
# Leetcode link: https://leetcode.com/problems/same-tree/
# ----------------------------
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def propagate_comparison(node_a: Optional[TreeNode], node_b: Optional[TreeNode]) -> bool:
            if node_a is None or node_b is None:
                return node_a is node_b

            return node_a.val == node_b.val and propagate_comparison(node_a.left, node_b.left) and propagate_comparison(node_a.right, node_b.right)

        return propagate_comparison(p, q)