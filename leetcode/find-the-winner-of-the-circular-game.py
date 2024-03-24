class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = list(range(1, n + 1))
        current_index = 0 
        while len(circle) > 1: 
            remove_index = (current_index + k - 1) % len(circle)
            circle.pop(remove_index)
            current_index = remove_index % len(circle)
        return circle[0]
            