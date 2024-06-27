class Solution:
    def findGCD(self, nums: list[int]) -> int:
        a = max(nums)
        b = min(nums)
        
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        
        return b