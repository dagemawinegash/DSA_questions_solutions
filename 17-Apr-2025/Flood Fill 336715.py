# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])

        def inbound(i, j):
            return 0 <= i < rows and 0 <= j < cols
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        start = image[sr][sc]
        def helper(i, j):
            if not inbound(i, j) or image[i][j] == color or image[i][j] != start:
                return
            image[i][j] = color
            for x, y in directions:
                new_x, new_y = x + i, y + j
                helper(new_x, new_y)
        helper(sr, sc)
        return image
