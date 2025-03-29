# Problem: Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int: 
        l = 0
        n = len(nums)
        r = n - 1
        ans = float('inf')

        while l <= r:
            mid = l + (r - l) // 2
            ans = min(ans, nums[mid])

            # eliminate the sorted half
            if nums[mid] <= nums[r]:
                r = mid - 1
            else:
                l = mid + 1
                
            
        return ans