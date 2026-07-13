# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        if second.val matches:
            first.next = second.next
            del second
            second = first.next ?
        else:
            first = second
            second = first.next
        """
        if not head:
            return None
        while head and head.val == val:
            tmp = head
            head = head.next
            del tmp

        if not head:
            return None

        first = head
        second = head.next
        while second:
            if second.val == val:
                tmp = second
                first.next = second.next
                second = first.next
                del tmp   
            else:
                first = second
                second = first.next

        return head
        