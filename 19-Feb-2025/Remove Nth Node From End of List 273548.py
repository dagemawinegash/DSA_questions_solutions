# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            curr = curr.next
            size += 1
        
        n = size - n + 1
        if n == 1:
            return head.next
        
        curr = head
        for _ in range(n - 2):
            if curr:
                curr = curr.next
        if not curr.next:
            curr.next = None
            return head
        curr.next = curr.next.next
        return head


        
        