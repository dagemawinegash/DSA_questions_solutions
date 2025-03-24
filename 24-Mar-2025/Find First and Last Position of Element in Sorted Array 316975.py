# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        def helper(goal, flag=False):
            l = 0
            r = n - 1
            res = -1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == goal:
                    res = mid
                if flag:
                    if nums[mid] < goal:
                        l = mid + 1
                    else:
                        r = mid - 1
                else:
                    if nums[mid] <= goal:
                        l = mid + 1
                    else:
                        r = mid - 1
                
            return res
        
        return [helper(target, True), helper(target)]