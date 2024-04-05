class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        if k == len(points):
            return points
        else:
            points = sorted(points, key = lambda point: point[0]**2 + point[1]**2)
            return points[:k]