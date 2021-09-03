#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import typing


class Solution:
    def inorderTraversal(self, root: typing.Optional[TreeNode]) -> typing.List[int]:
        order = []

        # if root node is null, exit
        if root is None:
            return order

        if root.left:
            self.inorderTraversal(root.left)

        order.append(root.val)

        if root.right:
            self.inorderTraversal(root.right)

        print(root)

        return order
