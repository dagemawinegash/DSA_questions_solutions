from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)
        heap = [(-val, key) for key, val in counter.items()]
        heapq.heapify(heap)

        ans = [heapq.heappop(heap)[1] for _ in range(k)]
        
        return ans