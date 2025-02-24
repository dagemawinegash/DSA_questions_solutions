# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0 : -1}
        curr_sum = 0
        
        for i, num in enumerate(nums):
            curr_sum += num
            if curr_sum % k in d:
                if i - d[curr_sum % k] >= 2:
                    return True
            else:
                d[curr_sum % k] = i

        return False
