# https://leetcode.com/problems/middle-of-the-linked-list/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MiddleLinkedList:
    def middle_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        all_values = []
        it = head
        while it.next is not None:
            all_values.append(int(it.val))
            it = it.next
        all_values.append(int(it.val))
        mid = int((len(all_values) / 2) + 1)

        node = head
        for i in range(1, mid):
            node = node.next

        return node
