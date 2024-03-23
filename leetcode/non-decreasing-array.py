class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        counter = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                counter += 1
                if i > 0 and nums[i-1] > nums[i+1]:
                    nums[i+1] = nums[i]
                else:
                    nums[i] = nums[i+1]
            if counter > 1:
                return False
        return True
