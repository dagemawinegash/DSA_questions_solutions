class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a','e','i','o','u'])
        start = 0
        ans = 0
        curr_vowels = 0
        for end in range(len(s)):
            if s[end] in vowels:
                curr_vowels += 1
            
            if end-start >= k:
                if s[start] in vowels:
                    curr_vowels-=1
                start+=1

            ans = max(ans,curr_vowels)
            
        return ans