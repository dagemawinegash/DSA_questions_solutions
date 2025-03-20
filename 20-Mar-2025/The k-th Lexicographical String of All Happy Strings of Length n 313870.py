# Problem: The k-th Lexicographical String of All Happy Strings of Length n - https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        s = ["a", "b", "c"]
        ans = []
        def helper(perms):                
            if len(perms) == n:
                ans.append("".join(perms))
                return
                
            for char in s:
                if not perms or perms[-1] != char:
                    perms.append(char)
                    helper(perms)
                    perms.pop()
        helper([])
        if k <= len(ans):
            return ans[k - 1]
        return ""
        