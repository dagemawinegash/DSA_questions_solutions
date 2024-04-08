from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        ans = []
        start = 0
        window_count = Counter(s[:len(p)-1])
        p_count = Counter(p)
        for i in range(len(p)-1, len(s)):
            window_count[s[i]] += 1
            if window_count == p_count:
                ans.append(start)
            window_count[s[start]] -= 1
            if window_count[s[start]] == 0:
                del window_count[s[start]]
            start += 1
                
        return ans