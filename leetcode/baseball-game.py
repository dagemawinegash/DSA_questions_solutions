class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        for char in operations:
            if char not in["C","D","+"]:
                stack.append(int(char))
            elif char == "C":
                stack.pop()
            elif char == "D":
                stack.append(2*stack[-1])
            elif char == "+":
                stack.append(stack[-1]+stack[-2])
        return sum(stack)