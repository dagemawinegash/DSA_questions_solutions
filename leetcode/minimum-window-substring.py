from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        t_count = Counter(t)
        window_count = {}
        have = 0
        need = len(t_count)
        res = [0, 0]
        start = 0
        length = float('inf')

        for end, char in enumerate(s):
            window_count[char] = window_count.get(char, 0) + 1
            if char in t_count and t_count[char] == window_count[char]:
                have += 1
            
            while have == need:
                if end - start + 1 < length:
                    res = [start, end]
                    length = end - start + 1
                window_count[s[start]] -= 1
                if s[start] in t_count and window_count[s[start]] < t_count[s[start]]:
                    have -= 1
                start += 1

        start, end = res
        if length == float('inf'):
            return ""
        else:
            return s[start:end+1]