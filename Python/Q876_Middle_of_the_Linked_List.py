from typing import Optional
import ast
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val) +'->'+ str(self.next)

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        lst = []
        while head:
            count += 1
            lst.append(head)
            head = head.next
        mid = count // 2
        return lst[mid]
