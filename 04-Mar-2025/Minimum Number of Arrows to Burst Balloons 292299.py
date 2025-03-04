# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        ans = 1
        n = len(points)
        start = points[0]

        for i in range(1, n):
            end = points[i]
            if start[1] < end[0]:
                ans += 1
                start = end
            else:
                start = (end[0], min(start[1], end[1]))
        return ans
            
        
        
       