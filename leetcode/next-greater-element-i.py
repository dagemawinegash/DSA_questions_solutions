class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hashtable = {}
        res = [-1] * len(nums1)
        stack = []
        
        for i, x in enumerate(nums1):
            hashtable[x] = i
            
        for y in nums2:
            while stack and y > stack[-1]:
                index = hashtable[stack[-1]]
                res[index] = y
                stack.pop()
            if y in hashtable:
                stack.append(y)
        
        return res
