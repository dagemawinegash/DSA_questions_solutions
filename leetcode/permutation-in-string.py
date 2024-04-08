from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_count = Counter(s2[:len(s1)-1])
        s1_count = Counter(s1)
        start = 0

        for i in range(len(s1)-1, len(s2)):
            window_count[s2[i]] += 1
            if window_count == s1_count:
                return True
            window_count[s2[start]] -= 1
            if window_count[s2[start]] == 0:
                del window_count[s2[start]]
            start += 1
            
        return False  