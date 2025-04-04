# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def merge(left_side, right_side):
            def helper(left_side, right_side):
                if not left_side:
                    return right_side
                if not right_side:
                    return left_side
                if left_side.val < right_side.val:
                    left_side.next = helper(left_side.next, right_side)
                    return left_side
                else:
                    right_side.next = helper(left_side, right_side.next)
                    return right_side
            return helper(left_side, right_side)

        def mergeSort(head):
            if not head or not head.next:
                return head
            prev = None
            slow = head
            fast = head
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            # print(prev.val)
            prev.next = None
            left_side = mergeSort(head)
            right_side = mergeSort(slow)
            return merge(left_side, right_side)
        
        return mergeSort(head)
