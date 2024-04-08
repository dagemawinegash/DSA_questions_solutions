class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        ans = 0
        for i in range(len(nums)):
            l,r = i+1, len(nums)-1
            while l < r:
                threesum = nums[i] + nums [l] + nums [r]
                if abs(threesum-target) < closest:
                    closest = abs(threesum-target)
                    ans = threesum
                if threesum < target:
                    l+=1
                elif threesum > target:
                    r-=1
                else:
                    return threesum
        return ans
        