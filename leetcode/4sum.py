class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        arr = []
        for i in range (len(nums)):
            if i > 0 and  nums [i] == nums [i-1]:
                continue
            for j in range (i+1, len(nums)):
                if j > i+1 and nums[j] == nums [j-1]:
                    continue
                
                l,r = j+1, len(nums)-1
                while l < r:
                    foursum = nums[i] + nums [j] + nums [l] + nums [r]
                    if foursum > target:
                        r-=1
                    elif foursum < target:
                        l+=1
                    else:
                        arr.append([nums[i], nums [j], nums [l], nums [r]])
                        l+=1
                        while  l < r and nums [l] == nums [l-1]: 
                            l+=1               
        return arr
            