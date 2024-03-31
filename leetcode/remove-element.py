class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        j = 0
        while i < len(nums):
            if nums[i]!=val:
                nums[i], nums[j] = nums[j], nums[i]
                j+=1
            i+=1
        return j