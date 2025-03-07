# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        minDeque = deque()
        maxDeque = deque()
        left = 0
        ans = 0

        for right in range(len(nums)):
            while minDeque and nums[minDeque[-1]] >= nums[right]:
                minDeque.pop()
            minDeque.append(right)

            while maxDeque and nums[maxDeque[-1]] <= nums[right]:
                maxDeque.pop()
            maxDeque.append(right)

            while nums[maxDeque[0]] - nums[minDeque[0]] > limit:
                if minDeque[0] == left:
                    minDeque.popleft()
                if maxDeque[0] == left:
                    maxDeque.popleft()
                left += 1

            ans = max(ans, right - left + 1)

        return ans

        