class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        ones,zeros = 0,0
        ans = 0
        hashmap = {} # ones-zeros -> index
        for i, n in enumerate(nums):
            if n == 0:
                zeros+=1
            else:
                ones+=1
            if ones-zeros not in hashmap:
                hashmap[ones-zeros] = i
            if ones == zeros:
                ans = ones+zeros
            else:
                index = hashmap[ones-zeros]
                ans = max(ans, i-index)
        return ans


        