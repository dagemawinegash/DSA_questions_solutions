import heapq
class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)
        if self.maxHeap and self.minHeap:
            if -self.maxHeap[0] > self.minHeap[0]:
                x = -heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, x)
        
        if len(self.maxHeap) > len(self.minHeap) + 1:
            x = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, x)
        
        if len(self.minHeap) > len(self.maxHeap) + 1:
            x = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -x)

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2


