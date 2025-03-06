# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for char in s:
            if char == "(":
                stack.append(0)
            else:
                num = stack.pop()
                if num != 0:
                    val = 2 * num
                else:
                    val = 1
                stack[-1] += val
        
        return stack[-1]
