class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        x = 0

        for char in s:
            if char == "(":
                stack.append(char)
            elif char == ")" and stack and stack[-1] == "(":
                stack.pop()
            else:
                x += 1
        
        return len(stack) + x