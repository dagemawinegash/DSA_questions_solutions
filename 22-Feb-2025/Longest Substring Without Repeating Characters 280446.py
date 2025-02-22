# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        d = Counter()
        start = 0

        for end, char in enumerate(s):
            d[char] += 1
            while d[char] >= 2:
                d[s[start]] -= 1
                start += 1
            ans = max(ans, end - start + 1)
        return ans
        