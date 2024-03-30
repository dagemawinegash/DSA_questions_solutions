class Solution:
    def numTimesAllBlue(self, flips: list[int]) -> int:
        count = 0
        max_index = 0
        for i in range(len(flips)):
            max_index = max(max_index,flips[i])
            if max_index == i+1:
                count += 1
        return count