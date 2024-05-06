class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        stack = []
        result = 0

        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                j = stack.pop()
                k = stack[-1] if stack else -1
                result += arr[j] * (i - j) * (j - k)
                result %= MOD
            stack.append(i)

        while stack:
            j = stack.pop()
            k = stack[-1] if stack else -1
            result += arr[j] * (n - j) * (j - k)
            result %= MOD

        return result