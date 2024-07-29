class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        def inbound(i, j):
            return 0 <= i < rows and 0 <= j < cols

        def backtrack(i, j, k):
            if not inbound(i, j) or board[i][j] != word[k] or (i, j) in visited:
                return False
            
            if k == len(word) - 1:
                return True
            
            visited.add((i, j))

            for x, y in directions:
                new_x, new_y = i + x, j + y
                if backtrack(new_x, new_y, k + 1):
                    return True

            visited.remove((i, j))
            return False
        
        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True
        
        return False
