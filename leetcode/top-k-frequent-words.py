import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        counter = Counter(words)
        maxHeap = []
        ans = []

        for key in counter:
            heapq.heappush(maxHeap, (-counter[key], key))
        
        for _ in range(k):
            count, word = heapq.heappop(maxHeap)
            ans.append(word)
        
        return ans