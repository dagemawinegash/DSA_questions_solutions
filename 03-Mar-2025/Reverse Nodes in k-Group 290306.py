# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        start = head
        end = head

        last_head = dummy

        while True:

            count = k

            while count and end:
                end = end.next
                count-=1
            
            if count > 0:
                return dummy.next
            
            next = end
            next_last_head = start

            count = k
            while count:
                tmp = start.next
                start.next = next
                next = start
                start = tmp
                count -= 1
            
            last_head.next = next
            last_head = next_last_head
