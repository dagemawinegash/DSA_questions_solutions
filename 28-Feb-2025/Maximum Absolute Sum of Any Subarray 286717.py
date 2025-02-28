# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        def helper(flag):
            total = nums[0]
            curr_sum = nums[0]

            for num in nums[1:]:
                option1 = curr_sum + num
                option2 = num
                if flag:
                    if curr_sum < 0: curr_sum = option2
                    else: curr_sum = option1
                    total = max(total, curr_sum)
                else:
                    if curr_sum > 0: curr_sum = option2
                    else: curr_sum = option1
                    total = min(total, curr_sum)
            return total

        return max(abs(helper(True)), abs(helper(False)))



        