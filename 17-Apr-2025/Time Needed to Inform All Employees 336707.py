# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i, num in enumerate(manager): 
            if i != headID:
                graph[num].append(i)
        
        def helper(node):
            if not graph[node]:
                return 0
            max_time = 0
            for neighbour in graph[node]:
                max_time = max(max_time, helper(neighbour))
            return max_time + informTime[node]

        return helper(headID)
       