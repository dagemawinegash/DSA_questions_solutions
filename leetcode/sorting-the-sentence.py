class Solution:
    def sortSentence(self, s: str) -> str:
        ans = ""
        words = s.split()
        words.sort(key=lambda word: int(word[-1])) 
        for word in words:
            ans += ''.join(word[:-1]) 
            if word != words[-1]:
                ans+= ' '  
        return ans