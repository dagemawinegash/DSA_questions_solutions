class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        res = 0
        curr_sum = 0
        prefix = {0 : 1}

        for n in nums:
            curr_sum += n
            diff = curr_sum - k
            res += prefix.get(diff, 0)
            prefix[curr_sum] = 1 + prefix.get(curr_sum, 0)

        return res