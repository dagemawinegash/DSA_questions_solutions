# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = list(range(1, n + 1))

        def helper(current_idx):
            if len(circle) == 1:
                return circle[0]
            remove_idx = (current_idx + k - 1) % len(circle)
            circle.pop(remove_idx)
            return helper(remove_idx)
            
        return helper(0)
        