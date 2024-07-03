class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        initial_color = image[sr][sc]
        
        if initial_color == color:
            return image
        
        def inbound(i, j):
            return 0 <= i < len(image) and 0 <= j < len(image[0])
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(i, j):
            if not inbound(i, j) or image[i][j] != initial_color:
                return
            
            image[i][j] = color

            for x, y in directions:
                new_x, new_y = i + x, j + y
                dfs(new_x, new_y)
        
        dfs(sr, sc)
        return image

