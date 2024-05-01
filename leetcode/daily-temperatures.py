class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                curr_idx = stack.pop()
                ans[curr_idx] = i - curr_idx
            stack.append(i)

        return ans
