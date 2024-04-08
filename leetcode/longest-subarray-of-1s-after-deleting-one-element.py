class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        start = 0
        ans = 0
        zero_count = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[start] == 0:
                    zero_count-=1
                start+=1
            ans = max(ans,end-start)  
        return ans
