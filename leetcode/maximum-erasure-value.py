class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        left, right = 0, 0
        hashset = set()
        ans = 0
        curr_sum = 0
        
        while right < n:
            if nums[right] not in hashset:
                hashset.add(nums[right])
                curr_sum += nums[right]
                right += 1
                ans = max(ans, curr_sum)
            else:
                hashset.remove(nums[left])
                curr_sum -= nums[left]
                left += 1
        
        return ans