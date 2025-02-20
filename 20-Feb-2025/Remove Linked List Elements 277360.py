# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy

        while curr:
            temp = curr
            while temp.next and temp.next.val == val:
                temp = temp.next
            if temp != curr:
                curr.next = temp.next
            curr = curr.next

        return dummy.next

        