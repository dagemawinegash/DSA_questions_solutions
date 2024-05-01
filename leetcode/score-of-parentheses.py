class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for char in s:
            if char == "(":
                stack.append(0)
            else:
                res = max(2 * stack.pop(), 1)
                stack[-1] += res
        
        return stack[-1]