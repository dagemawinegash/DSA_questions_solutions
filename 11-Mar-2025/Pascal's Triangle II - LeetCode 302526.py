# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def helper(n):
            if n == 0:
                return [1]

            prev = helper(n - 1)
            curr = [1]
            for i in range(1, n):
                curr.append(prev[i - 1] + prev[i])

            curr.append(1)
            return curr
        return helper(rowIndex)



                
                
        