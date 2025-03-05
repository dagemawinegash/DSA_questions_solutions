# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        stack = []
        for char in arr:
            if stack and char == "..":
                stack.pop()
            elif char and char not in {".", ".."}:
                stack.append(char)
        return "/" + "/".join(stack)

        