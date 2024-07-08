import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)
            if x != y:
                heapq.heappush(max_heap, x - y)
        
        return -max_heap[0] if max_heap else 0