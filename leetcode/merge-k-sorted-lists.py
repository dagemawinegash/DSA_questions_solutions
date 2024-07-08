from typing import Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode(-1)
        curr = dummy
        
        for i, node in enumerate(lists):
            if node: 
                heapq.heappush(heap, (node.val, i, node))
        
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        return dummy.next





        