import heapq

class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        tasks = [(enqueueTime, processingTime, i) for i, (enqueueTime, processingTime) in enumerate(tasks)]
        tasks.sort()
        ans = []
        min_heap = []
        time = 0
        i = 0
        
        while len(ans) < len(tasks):
            while i < len(tasks) and tasks[i][0] <= time:
                enqueueTime, processingTime, idx = tasks[i]
                heapq.heappush(min_heap, (processingTime, idx))
                i += 1
            
            if min_heap:
                processingTime, idx = heapq.heappop(min_heap)
                ans.append(idx)
                time += processingTime
            else:
                time = tasks[i][0]
        
        return ans
