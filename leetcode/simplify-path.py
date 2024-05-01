class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")

        for char in path:
            if char == ".." and stack:
                stack.pop()
            elif char not in {"", "..", "."}:
                    stack.append(char)
    
        return "/" + "/".join(stack)