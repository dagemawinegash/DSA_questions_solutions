# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        MOD = (10 ** 9) + 7
        
        next_smallest = [n] * n
        stack = []
        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                idx = stack.pop()
                next_smallest[idx] = i
            stack.append(i)
        print(next_smallest)

        prev_smallest_equal = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[i] <= arr[stack[-1]]:
                idx = stack.pop()
                prev_smallest_equal[idx] = i
            stack.append(i)
        print(prev_smallest_equal)

        ans = 0
        for i in range(n):
            right = next_smallest[i] - i
            left = i - prev_smallest_equal[i]
            ans += (right * left * arr[i])
        print(ans)
        return ans % MOD






       