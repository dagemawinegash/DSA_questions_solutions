class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        l,r,odd,cnt,ans = 0,0,0,0,0
        while r < len(nums):
            if nums[r]%2:
                odd+=1
                cnt=0
            while odd==k:
                cnt+=1 
                if nums[l]%2:
                    odd-=1
                l+=1
            ans+=cnt
            r+=1
        return ans