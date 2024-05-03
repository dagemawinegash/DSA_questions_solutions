from collections import defaultdict
class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        target = sum(nums) % p
        if target == 0:
            return 0
        
        prefix_sum = 0
        prefix_sum_map = defaultdict(int)
        prefix_sum_map[0] = -1
        min_len = len(nums)
        
        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p
            complement = (prefix_sum - target) % p
            
            if complement in prefix_sum_map:
                min_len = min(min_len, i - prefix_sum_map[complement])
            
            prefix_sum_map[prefix_sum] = i
        
        return min_len if min_len < len(nums) else -1