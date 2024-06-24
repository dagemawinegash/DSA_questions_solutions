class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start):
            if start == len(nums):
                ans.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        
        ans = []
        backtrack(0)
        return ans