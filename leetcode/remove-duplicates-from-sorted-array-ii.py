class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i,j = 0 , 1
        count = 1
        while j < len(nums):
            if nums[i]==nums[j]:
                count+=1
                if count <= 2:
                    nums[i+1]=nums[j]
                    i+=1
            else:
                count = 1
                nums[i+1] = nums[j]
                i+=1
            j+=1
        return i+1
        


             

        