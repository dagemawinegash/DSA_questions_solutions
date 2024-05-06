class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        num3 = float('-inf')
        stack = []

        for num in reversed(nums):
            if num < num3:
                return True
            while stack and num > stack[-1]:
                num3 = stack.pop()
            stack.append(num)
        
        return False
