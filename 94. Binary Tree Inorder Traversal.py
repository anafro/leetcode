# ----------------------------
# Category: Easy
# Leetcode link: https://leetcode.com/problems/binary-tree-inorder-traversal
# ----------------------------
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal_items = []

        def propagate_traversal(node: Optional[TreeNode]) -> None:
            if node is None:
                return

            propagate_traversal(node.left)
            traversal_items.append(node.val)
            propagate_traversal(node.right)

        propagate_traversal(root)
        return traversal_items