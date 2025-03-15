# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        def helper(i, j):
            if i > j:
                return 0
            option1 = nums[i] - helper(i + 1, j)
            option2 = nums[j] - helper(i, j - 1)
            return max(option1, option2)
        
        return helper(0, n - 1) >= 0



        