# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(stg):
            stack = []
            for char in stg:
                if stack and char == "#":
                    stack.pop()
                elif char != "#":
                    stack.append(char)
            return stack
        
        return helper(s) == helper(t)
        
        