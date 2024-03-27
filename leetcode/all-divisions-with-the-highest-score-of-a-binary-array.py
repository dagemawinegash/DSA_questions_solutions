class Solution:
    def maxScoreIndices(self, nums: list[int]) -> list[int]:
        N = len(nums)
        total = sum(nums)
        best = total
        score = total
        ans = [0]
        for left in range(N):
            if nums[left] == 0:
                score += 1
            else:
                score -= 1
            if best == score:
                ans.append(left + 1)
            elif best < score:
                best = score
                ans = [left + 1]
        return ans

    


        