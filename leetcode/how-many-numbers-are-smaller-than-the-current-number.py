class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        sorted_nums = sorted(nums)
        ans = []
        num_count = {} 
        for i, x in enumerate(sorted_nums):
            if x not in num_count:
                num_count[x] = i
        for x in nums:
            ans.append(num_count[x])
        return ans