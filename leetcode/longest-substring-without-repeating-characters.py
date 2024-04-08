class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_chars = set()
        ans,start = 0,0
        for end in range(len(s)):
            while s[end] in set_chars:
                set_chars.remove(s[start])
                start+=1
            set_chars.add(s[end])
            ans = max(ans,end-start+1)
        return ans