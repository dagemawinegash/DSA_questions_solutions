# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode(-1)
        right = ListNode(-1)
        left_tail = left
        right_tail = right

        while head:
            if head.val >= x:
                right_tail.next = head
                right_tail = head
            else:
                left_tail.next = head
                left_tail = head
            head = head.next
        
        left_tail.next = right.next
        right_tail.next = None
        
        return left.next
