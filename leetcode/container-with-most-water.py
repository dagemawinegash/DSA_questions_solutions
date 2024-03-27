class Solution:
    def maxArea(self, height: list[int]) -> int:
        ptr1 = 0
        ptr2 = len(height) - 1
        x = len(height) - 1
        res = 0
        while ptr1<ptr2:
            area = min(height[ptr1], height[ptr2]) * x
            if height[ptr1] < height[ptr2]:
                ptr1+=1
            else:
                ptr2-=1 
            x-=1
            res = max(res, area)
        return res