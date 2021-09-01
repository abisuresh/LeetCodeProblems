# Definition for singly-linked list.
import typing


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: typing.Optional[ListNode], l2: typing.Optional[ListNode]) -> typing.Optional[ListNode]:
        if l1 is None:
            head = l2
            return head

        if l2 is None:
            head = l1
            return head

        head = ListNode()

        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        elif l2.val < l1.val:
            head = l2
            l2 = l2.next
        else:
            head = l1
            l1 = l1.next

        node = head

        while l1 is not None or l2 is not None:
            if l1 is None:
                print("l1 empty")
                node.next = l2
                break

            if l2 is None:
                node.next = l1
                break

            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next

            else:
                node.next = l2
                l2 = l2.next

            node = node.next

        return head
