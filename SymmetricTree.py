# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if (root == None):
            return True

        leftNode = root.left
        rightNode = root.right
        result = False
        leftStack = []
        rightStack = []

        # while loop

        while (leftNode != None or rightNode != None or len(leftStack) > 0 or len(rightStack) > 0):

            if (leftNode == None and rightNode == None):
                leftNode = leftStack.pop().right
                rightNode = rightStack.pop().left

            if ((leftNode == None and rightNode != None) or (leftNode != None and rightNode == None)):
                return False

            if (leftNode == None and rightNode == None):
                continue

            if (leftNode.val != rightNode.val):
                return False

            if (leftNode.val == rightNode.val):

                leftStack.append(leftNode)
                rightStack.append(rightNode)

                leftNode = leftNode.left
                rightNode = rightNode.right
                if (leftNode == None and rightNode == None):
                    leftNode = leftStack.pop().right

                    rightNode = rightStack.pop().left

        return True