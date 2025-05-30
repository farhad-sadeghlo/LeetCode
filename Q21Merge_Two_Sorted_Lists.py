from typing import Optional
from Linked_List import Node, LinkedList

class MergeTwoSortedLists:
    def __init__(self, l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:
        self.l1 = l1
        self.l2 = l2

    def merge_two_list(self):
        dummy = Node(0)
        curr = dummy
        l1, l2 = self.l1, self.l2
        while l1 and l2:
            if l1.value <= l2.value:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2
        return dummy.next
#