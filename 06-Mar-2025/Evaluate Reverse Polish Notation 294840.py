# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "-", "*", "/"}
        for char in tokens:
            if char in operations:
                a = stack.pop()
                b = stack.pop()
                print(a, b)
                if char == "+":
                    stack.append(a + b)
                elif char == "-":
                    stack.append(b - a)
                elif char == "*":
                    stack.append(a * b)
                elif char == "/":
                    stack.append(int(b / a))      
            else:
                stack.append(int(char))
        return stack[-1]
        