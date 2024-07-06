from collections import deque

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        queue = deque([("0000", 0)])
        visited = set(deadends)
        visited.add("0000")

        def helper(s):
            neighbors = []
            for i in range(4):
                num = int(s[i])
                neighbors.append(s[:i] + str((num + 1) % 10) + s[i+1:])
                neighbors.append(s[:i] + str((num - 1 + 10) % 10) + s[i+1:])
            return neighbors

        while queue:
            lock, steps = queue.popleft()
            if lock == target:
                return steps

            for neighbor in helper(lock):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
        
        return -1
