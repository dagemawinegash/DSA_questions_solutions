# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        ans = ["0"] * n
        count = 0
        ans[-1] = "1"
        i = 0
        for char in s:
            if char == "1":
                if count != 0:
                    ans[i] = "1"
                    i += 1
                count += 1
        return "".join(ans)
       

        
        
        



