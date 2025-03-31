# Problem: N-Queens II - https://leetcode.com/problems/n-queens-ii/description/

class Solution:
    def totalNQueens(self, n: int) -> int:
        def checker(row, col, columns, main_dig, anti_dig):
            if col in columns or (row + col) in main_dig or (row - col) in anti_dig:
                return False
            return True

        def helper(row, columns, main_dig, anti_dig, board):
            nonlocal ans
            if row == n:
                ans += 1

            for col in range(n):
                if not checker(row, col, columns, main_dig, anti_dig):
                    continue
                    
                # placing the queen on the current row and col
                board[row][col] = "Q"
                columns.add(col)
                main_dig.add(row + col)
                anti_dig.add(row - col)

                helper(row + 1, columns, main_dig, anti_dig, board)

                # backtrack to thr upper row 
                board[row][col] = "."
                columns.remove(col)
                main_dig.remove(row + col)
                anti_dig.remove(row - col)
        
        ans = 0
        board = [["."] * n for _ in range(n)]
        helper(0, set(), set(), set(), board)
        return ans