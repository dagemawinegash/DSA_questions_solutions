# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def helper(i, arr):
            if len(arr) == k:
                ans.append(arr[:])
                return
            if i > n:
                return 
        
            # option-1 choose the curr element
            arr.append(i)
            helper(i + 1, arr)
            # option-2 ignore the curr element
            arr.pop()
            helper(i + 1, arr)
        
        ans = []
        helper(1, [])
        return ans