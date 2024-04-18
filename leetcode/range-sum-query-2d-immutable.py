class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        R = len(matrix)
        C = len(matrix[0])
        self.psa = [[0 for _ in range(C+1)] for _ in range(R+1)]
        for i in range(1, R+1):
            for j in range(1, C+1):
                self.psa[i][j] = self.psa[i-1][j] + self.psa[i][j-1] - self.psa[i-1][j-1] + matrix[i-1][j-1]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.psa[row2+1][col2+1] - self.psa[row1][col2+1] - self.psa[row2+1][col1] + self.psa[row1][col1]

