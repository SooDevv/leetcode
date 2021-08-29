# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head

        cur = head.next
        prev = head

        while cur:
            if cur.val == prev.val:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        return head