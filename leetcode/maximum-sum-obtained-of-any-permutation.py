class Solution:
    def maxSumRangeQuery(self, nums: list[int], requests: list[list[int]]) -> int:
        MOD = 10**9 + 7
        freq_counter = [0] * len(nums)
        for start, end in requests:
            freq_counter[start] += 1
            if end + 1 < len(nums):
                freq_counter[end + 1] -= 1

        for i in range(1, len(nums)):
            freq_counter[i] += freq_counter[i - 1]

        nums.sort(reverse=True)
        freq_counter.sort(reverse=True)

        total_sum = 0
        for i in range(len(freq_counter)):
            total_sum += freq_counter[i] * nums[i]

        return total_sum % MOD