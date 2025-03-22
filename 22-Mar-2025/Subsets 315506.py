# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def helper(i, arr):
            if i >= n:
                ans.append(arr[:])
                return
            
            # option-1 choose the curr element
            arr.append(nums[i])
            helper(i + 1, arr)
            # option-2 ignore the curr element
            arr.pop()
            helper(i + 1, arr)
        
        helper(0, [])
        return ans
        


        