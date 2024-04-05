class Solution:
    def minProcessingTime(self, processorTime: list[int], tasks: list[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        ans,j = 0,0
        for i in range(len(processorTime)):
            ans = max(ans, processorTime[i]+tasks[j])
            j+=4      
        return ans
