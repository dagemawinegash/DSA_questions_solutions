import heapq

class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        heap = []
        
        for i in range(n - 1):
            change = heights[i + 1] - heights[i]
            if change <= 0:
                continue
            
            bricks -= change
            heapq.heappush(heap, -change)
            
            if bricks < 0:
                if ladders <= 0:
                    return i
                ladders -= 1
                bricks += -heapq.heappop(heap)
                
        return n - 1
