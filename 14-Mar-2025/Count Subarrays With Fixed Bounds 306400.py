# Problem: Count Subarrays With Fixed Bounds - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        min_idx = -1
        max_idx = -1
        bad_idx = -1
        for i, num in enumerate(nums):
            if num == minK:
                min_idx = i
            if num == maxK:
                max_idx = i
            if not (minK <= num <= maxK):
                bad_idx = i

            ans += max(0, min(min_idx, max_idx) - bad_idx)
            
        return ans

        
       