class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        count = 0
        
        for row in matrix:
            for j in range(1, cols):
                row[j] += row[j - 1]
        
        for left in range(cols):
            for right in range(left, cols):
                prefix_sums = {0: 1}  
                curr_sum = 0 
                
                for i in range(rows):
                    if left > 0:
                        curr_sum += matrix[i][right] - matrix[i][left - 1]
                    else:
                        curr_sum += matrix[i][right]
                    
                    if curr_sum - target in prefix_sums:
                        count += prefix_sums[curr_sum - target]
                    
                    prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
        
        return count
