# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        n = 0
        while curr:
            n += 1
            curr = curr.next
            
        curr = head
        count = 0
        while curr and count < n // 2:
            count += 1
            curr = curr.next
        
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        ans = 0
        while prev:
            ans = max(ans, head.val + prev.val)
            head = head.next
            prev = prev.next
        return ans


        
        