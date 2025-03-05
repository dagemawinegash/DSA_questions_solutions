# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for char in logs:
            if stack and  char == "../":
                stack.pop()
            elif char not in {"./", "../"}:
                stack.append(char)
        return len(stack)
        