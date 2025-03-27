# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if sum(nums) == 0:
            return 0

        def checker(k):
            arr = [0] * (n + 1)
            for i in range(k + 1):
                i, j, val = queries[i]
                arr[i] += val
                arr[j + 1] -= val
                
            curr_sum = 0
            for i in range(len(arr) - 1):
                curr_sum += arr[i]
                if nums[i] - curr_sum > 0:
                    return False

            return True

        l = 0
        r = len(queries) - 1
        n = len(nums)
        ans = -1
        while l <= r:
            mid = l + (r - l) // 2
            if checker(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        if ans == -1:
            return -1
        else:
            return ans + 1
