# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        d=ListNode()
        c=d
        t=head
        while t:
            if t.val!=val:
                c.next=t
                c=c.next
            t=t.next
        c.next=None
        return d.next