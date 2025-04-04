# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd_head = head
        even_head = head.next
        odd_curr = odd_head
        even_curr = even_head

        while even_curr and even_curr.next:
            odd_curr.next = even_curr.next
            odd_curr = odd_curr.next
            even_curr.next = odd_curr.next
            even_curr = even_curr.next
        
        odd_curr.next = even_head
        return odd_head
        