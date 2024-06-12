class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        ans = 0
        nums.sort()

        for i in range(len(nums) - 1, 1, -1):
            a = nums[i]
            j = 0
            k = i - 1
            while j < k:
                if nums[j] + nums[k] > a:
                    ans += k - j
                    k -= 1
                else:
                    j += 1
        return ans
