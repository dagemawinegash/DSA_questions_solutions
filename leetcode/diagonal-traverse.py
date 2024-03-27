class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        rows = len(mat)
        cols = len(mat[0])
        ans = []
        going_up = True
        cur_row, cur_col = 0,0
        while len(ans)!= rows*cols:
            if going_up:
                while cur_col < cols and cur_row >=0:
                    ans.append(mat[cur_row][cur_col])
                    cur_col+=1
                    cur_row-=1
                if cur_col == cols:
                    cur_col-=1
                    cur_row+=2
                else:
                    cur_row+=1
                going_up = False
            else:
                while cur_row < rows and cur_col >=0:
                    ans.append(mat[cur_row][cur_col])
                    cur_row+=1
                    cur_col-=1
                if cur_row == rows:
                    cur_col+=2
                    cur_row-=1
                else:
                    cur_col+=1
                going_up = True
        return ans
        