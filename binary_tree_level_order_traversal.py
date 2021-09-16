# Definition for a binary tree node.
import typing


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: typing.Optional[TreeNode]) -> typing.List[typing.List[int]]:
        if root is None:
            return []

        current = root

        order = []

        queue = []
        level = 0

        queue.append((current, level))

        while len(queue) > 0:
            current, level = queue.pop(0)
            if len(order) < level + 1:
                order.append([])

            order[level].append(current.val)

            if current.left:
                queue.append((current.left, level + 1))

            if current.right:
                queue.append((current.right, level + 1))

        return order
