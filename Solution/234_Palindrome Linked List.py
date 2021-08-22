# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from collections import deque


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q = deque()

        if not head:
            return True

        node = head
        while node:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True
