# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        arr = [True] * n
        for u, v in edges:
            arr[v] = False
        count = 0
        ans = -1
        for node, val in enumerate(arr):
            if val:
                count += 1
                ans = node
            if count >= 2:
                return -1
        return ans
        
