class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(board)
        cols = len(board[0])
        
        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols
        
        def dfs(x, y):
            if not inbound(x, y) or board[x][y] != "O":
                return
            
            board[x][y] = "#"

            for r, c in directions:
                new_x = r + x
                new_y = c + y
                dfs(new_x, new_y)
        
        for i in range(rows):
            for j in range(cols):
                if (board[i][j] == "O") and (i in [0, rows - 1] or j in [0, cols - 1]):
                    dfs(i, j)
                
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "#":
                    board[i][j] = "O"
