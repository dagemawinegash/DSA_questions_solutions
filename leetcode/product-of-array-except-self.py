class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n, pre, post = len(nums), 1, 1
        ans = [1] * (n)
    
        for i in range(n):
            ans[i] = pre
            pre *= nums[i]
        
        for i in range(n - 1, -1, -1):
            ans[i] *= post
            post *= nums[i]
            
        return ans