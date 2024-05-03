class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []

        for i in range(2 * n):
            num = nums[i % n]
            while stack and num > nums[stack[-1]]:
                idx = stack.pop()
                ans[idx] = num
            stack.append(i % n)

        return ans