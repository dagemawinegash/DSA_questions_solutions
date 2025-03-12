# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            inverted = []
            for i in range(len(s)):
                if s[i] =="0":
                    inverted.append("1")
                else:
                    inverted.append("0")
            return "".join(inverted)
        
        # def reverse(s):
        #     return "".join(reversed(s))
        def helper(n):
            if n == 1:
                return "0"
            return helper(n - 1) + "1" + "".join(reversed(invert(helper(n - 1))))
        return helper(n)[k - 1]
        