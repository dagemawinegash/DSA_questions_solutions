# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = 0
        r = sum(nums)

        def checker(curr_cap):
            res = 0
            curr_sum = 0
            for num in nums:
                if num > curr_cap:
                    return False
                curr_sum += num
                if curr_sum > curr_cap:
                    res += 1
                    curr_sum = num

            return res + 1 <= k

        ans = 0
        while l <= r:
            mid = l + (r - l) // 2
            if checker(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans