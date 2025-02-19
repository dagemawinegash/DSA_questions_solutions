# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leadPtr = head

        while n > 0:
            n -= 1
            leadPtr = leadPtr.next
        
        lagPtr = head
        prev = None
        while leadPtr:
            prev = lagPtr
            lagPtr = lagPtr.next
            leadPtr = leadPtr.next
        
        if prev == None: head = head.next
        else: prev.next = lagPtr.next
        return head
        


        
        