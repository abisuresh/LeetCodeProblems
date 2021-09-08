# Check if trees are the same

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import typing


class Solution:
    def isSameTree(self, p: typing.Optional[TreeNode], q: typing.Optional[TreeNode]) -> bool:

        if q and not p:
            return False

        if p and not q:
            return False

        if not p and not q:
            return True

        if p.val != q.val:
            return False

        if p.left and q.left:
            result = self.isSameTree(p.left, q.left)
            if not result:
                return False
        elif p.left or q.left:
            return False

        if p.right and q.right:
            result = self.isSameTree(p.right, q.right)
            if not result:
                return False
        elif p.right or q.right:
            return False

        return True
