class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum == target:
                return [left+1, right+1]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
            
        