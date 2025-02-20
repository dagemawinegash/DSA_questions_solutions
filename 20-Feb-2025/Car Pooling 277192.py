# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = [0] * 1001
        for x, y, z in trips:
            arr[y] += x
            arr[z] -= x
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]
        return max(arr) <= capacity

