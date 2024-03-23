# Time complexity O(N)
# Space complexity O(1)
class Solution:
    def wateringPlants(self, plants: list[int], capacity: int) -> int:
        current_capacity = capacity
        steps = 0
        for i in range(len(plants)):
            if plants[i] <= current_capacity:
                steps += 1
                current_capacity -= plants[i]
            else:
                current_capacity = capacity
                steps += (i * 2 + 1)
                current_capacity -= plants[i]
        return steps