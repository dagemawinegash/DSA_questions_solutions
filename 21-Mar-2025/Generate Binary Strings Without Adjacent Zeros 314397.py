# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:

        def helper(arr):
            if len(arr) == n:
                ans.append("".join(arr))
                return

            if arr and arr[-1] == "0":
                arr.append("1")
                helper(arr)
                arr.pop()

            else:
                arr.append("0")
                helper(arr)
                arr.pop()

                arr.append("1")
                helper(arr)
                arr.pop()
        
        ans = []
        helper([])
        return ans
