# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
dummy -> head -> ... -> 
"""
"""
In Python, memory management is automatic
(reference counting + garbage collector), 
so you don’t need to explicitly free nodes.
Once you break all links to a node
(by doing prev.next = cur.next),
nothing points to it anymore,
and Python will clean it up later.
"""
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(val=0, next=head)
        prev = dummy
        cur = head

        while cur:
            if cur.val == val:
                tmp = cur
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return dummy.next
