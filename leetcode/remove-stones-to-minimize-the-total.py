import heapq
from math import floor

class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        max_heap = [-pile for pile in piles]
        heapq.heapify(max_heap)

        for _ in range(k):
            largest_pile = -heapq.heappop(max_heap)
            reduced_pile = largest_pile - floor(largest_pile / 2)
            heapq.heappush(max_heap, -reduced_pile)
        
        return -sum(max_heap)
