class Solution:
    def maxScore(self, s: str) -> int:
        prefix_sum = [0] * len(s)
        prefix_sum[0] = int(s[0])

        for i in range(1, len(s)):
            prefix_sum[i] = prefix_sum[i - 1] + int(s[i])

        count = 0
        ans = float('-inf')

        for i in range(len(s) - 1):
            if s[i] == "0":
                count += 1
            value = count + prefix_sum[-1] - prefix_sum[i]
            ans = max(ans, value)

        return ans