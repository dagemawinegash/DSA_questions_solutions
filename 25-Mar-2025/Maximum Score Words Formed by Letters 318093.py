# Problem: Maximum Score Words Formed by Letters - https://leetcode.com/problems/maximum-score-words-formed-by-letters/description/

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        n = len(words)
        d = Counter(letters)
        
        def calculate(count):
            res = 0
            for char in count:
                res += score[ord(char) - ord("a")] * count[char]
            return res

        def helper(i, arr):
            nonlocal ans
            if i == n:
                count = Counter("".join(arr))
                if count <= d:
                    ans = max(ans, calculate(count))
                return
            arr.append(words[i])
            helper(i + 1, arr)
            arr.pop()
            helper(i + 1, arr)

        ans = 0
        helper(0, [])
        return ans
                

        
        
        




        