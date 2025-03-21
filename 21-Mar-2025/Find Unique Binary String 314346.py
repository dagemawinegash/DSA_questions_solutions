# Problem: Find Unique Binary String - https://leetcode.com/problems/find-unique-binary-string/description/

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)

        def helper(arr):
            if len(arr) == n:
                ans.append("".join(arr))
                return
             
            arr.append("0")
            helper(arr)
            arr.pop()

            arr.append("1")
            helper(arr)
            arr.pop()

        ans = []
        helper([])
        # print(ans)
        nums = set(nums)
        for num in ans:
            if num not in nums:
                return num



