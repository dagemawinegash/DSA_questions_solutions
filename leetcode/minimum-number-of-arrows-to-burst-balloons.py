class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        ans = 1
        points.sort()
        start = points[0]

        for i in range(1, len(points)):
            end = points[i]
            if start[1] < end[0]:
                ans += 1
                start = end
            else:
                start = (end[0], min(start[1], end[1]))
        
        return ans
