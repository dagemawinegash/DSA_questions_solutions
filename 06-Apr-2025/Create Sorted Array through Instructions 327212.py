# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        arr = []
        ans = 0
        
        for num in instructions:
            left = bisect_left(arr, num)
            right = len(arr) - bisect_right(arr, num)
            ans = (ans + min(left, right)) % MOD
            arr.insert(left, num)
        
        return ans
