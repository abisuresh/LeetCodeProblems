# Definition for singly-linked list.
import typing


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val}, {self.next}"


class Solution:
    def addTwoNumbers(self, l1: typing.Optional[ListNode], l2: typing.Optional[ListNode]) -> typing.Optional[ListNode]:
        carry_val = False

        new_node = ListNode()
        final_sum = new_node

        current_node = new_node

        while l1 is not None or l2 is not None:
            if l1 is None:
                sum_val = l2.val
                if carry_val:
                    sum_val = sum_val + current_node.val

                carry_val = False

                if sum_val > 9:
                    carry = sum_val // 10
                    current_node.val = sum_val % 10
                    next_node = ListNode()
                    next_node.val = carry
                    current_node.next = next_node
                    carry_val = True
                else:
                    current_node.val = sum_val
                    new_next_node = ListNode()
                    if l2.next is None:
                        break
                    current_node.next = new_next_node

                l2 = l2.next
                current_node = current_node.next

                continue

            if l2 is None:
                sum_val = l1.val
                if carry_val:
                    sum_val = sum_val + current_node.val

                carry_val = False

                if sum_val > 9:
                    carry = sum_val // 10
                    current_node.val = sum_val % 10
                    next_node = ListNode()
                    next_node.val = carry
                    current_node.next = next_node
                    carry_val = True
                else:
                    current_node.val = sum_val
                    new_next_node = ListNode()
                    if l1.next is None:
                        break
                    current_node.next = new_next_node

                l1 = l1.next
                current_node = current_node.next
                continue

            first_val = l1.val
            sum_val = first_val + l2.val

            if carry_val:
                sum_val = sum_val + current_node.val

            carry_val = False

            if sum_val > 9:
                carry = sum_val // 10
                current_node.val = sum_val % 10
                next_node = ListNode()
                next_node.val = carry
                current_node.next = next_node
                carry_val = True
            else:
                current_node.val = sum_val
                new_next_node = ListNode()
                if l1.next is None and l2.next is None:
                    break
                current_node.next = new_next_node

            l1 = l1.next
            l2 = l2.next
            current_node = current_node.next

        return final_sum


new_solution = Solution()
l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)

result = new_solution.addTwoNumbers(l1, l2)

print(result)
