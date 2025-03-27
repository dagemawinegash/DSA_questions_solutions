# Problem: House Robber IV - https://leetcode.com/problems/house-robber-iv/

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def checker(capability):
            res = 0
            count = 0
            for num in nums:
                if num <= capability:
                    count += 1
                else:
                    res += ceil(count / 2)
                    count = 0
            res += ceil(count / 2)
            return res >= k

        ans = 0
        l = 1
        r = max(nums)
        while l <= r:
            mid = l + (r - l) // 2
            print(mid)
            if checker(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
        
            
