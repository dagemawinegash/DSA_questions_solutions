# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        def calculate(left, right):
            nonlocal ans
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j] + diff:
                    ans += len(right) - j
                    i += 1
                else:
                    j += 1

        def merge(left, right):
            calculate(left, right)
            i = j = 0 
            res = []
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            while i < len(left):
                res.append(left[i])
                i += 1
            while j < len(right):
                res.append(right[j])
                j += 1
                
            return res
                    
        def mergeSort(l, r):
            if l == r:
                return [nums[l]]
            mid = l + (r - l) // 2
            left_side = mergeSort(l, mid)
            right_side = mergeSort(mid + 1, r)
            return merge(left_side, right_side)

        ans = 0 
        nums = []
        for i in range(len(nums1)):
            nums.append(nums1[i] - nums2[i])
        # print(nums)

        mergeSort(0, len(nums) - 1)
        return ans