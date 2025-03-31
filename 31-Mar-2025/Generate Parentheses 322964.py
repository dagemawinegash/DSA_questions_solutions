# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def helper(opened, closed, path):
            if len(path) == 2 * n:
                ans.append("".join(path))
            
            if opened < n:
                path.append("(")
                helper(opened + 1, closed, path)
                path.pop()
            if opened > closed:
                path.append(")")
                helper(opened, closed + 1, path)
                path.pop()
        
        helper(0, 0, [])
        return ans
