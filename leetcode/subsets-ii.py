class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        ans = []
        def backtrack(i, arr):
            if i >= len(nums):
                ans.append(arr[:])
                return
            arr.append(nums[i])
            backtrack(i + 1, arr)
            arr.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, arr)
        nums.sort()
        backtrack(0,[])
        return ans
