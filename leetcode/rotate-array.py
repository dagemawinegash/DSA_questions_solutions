class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = [0]*len(nums)
        for i,num in enumerate(nums):
            index = (i+k)%len(nums)
            arr[index] = nums[i]
        for i in range(len(arr)):
            nums[i] = arr[i]
    
        