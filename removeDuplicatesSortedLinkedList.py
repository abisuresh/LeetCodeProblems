import typing


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution for removing duplicates from a sorted linked list
class Solution:
    def deleteDuplicates(self, head: typing.Optional[ListNode]) -> typing.Optional[ListNode]:
        current_node = head

        # if linked list is empty return
        if current_node is None:
            return

        while current_node.next is not None:
            # check if the current node's value is the same as the next node's value
            if current_node.val == current_node.next.val:
                # get the node after the duplicate node
                node_after_duplicate = current_node.next.next

                # set the duplicate node to None
                current_node.next = None

                # reset next pointer to point to node after duplicate
                current_node.next = node_after_duplicate

            else:
                # not duplicate so can proceed as normal
                current_node = current_node.next

        # head is now pointing to the head of a linked list without the duplicates

        return head
