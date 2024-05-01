class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        res = 0
        curr_sum = 0
        prefix = {0 : 1}

        for n in nums:
            curr_sum += n
            remainder = curr_sum % k
            res += prefix.get(remainder, 0)
            prefix[remainder] = 1 + prefix.get(remainder, 0)

        return res
        