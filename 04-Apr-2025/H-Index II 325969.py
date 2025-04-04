# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l = 0
        r = n - 1
        ans = 0

        while l <= r:
            mid = l + (r - l) // 2 
            if citations[mid] >= n - mid:
                ans = n - mid
                r = mid - 1
            else:
                l = mid + 1

        return ans
