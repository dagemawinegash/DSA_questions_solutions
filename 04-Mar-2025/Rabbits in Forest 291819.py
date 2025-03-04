# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d = Counter(answers)
        ans = 0
        for num in d:
            ans += ceil(d[num] / (num + 1)) * (num + 1)
        return ans
            
       