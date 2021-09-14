# Determine max depth of tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import typing


class Solution:
    def maxDepth(self, root: typing.Optional[TreeNode]) -> int:
        count = 0

        left_count = 0

        right_count = 0

        if not root:
            return 0

        if root.left is None and root.right is None:
            return 1

        count += 1

        if root.left is not None:
            left_count += self.maxDepth(root.left)

        if root.right is not None:
            right_count += self.maxDepth(root.right)

        if left_count >= right_count:
            count += left_count
        elif right_count > left_count:
            count += right_count

        return count
