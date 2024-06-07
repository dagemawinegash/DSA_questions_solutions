from collections import Counter
from math import ceil

class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        counter = Counter(answers)
        ans = 0
        for answer in counter:
            ans += ceil(counter[answer] / (answer + 1)) * (answer + 1)
        return ans