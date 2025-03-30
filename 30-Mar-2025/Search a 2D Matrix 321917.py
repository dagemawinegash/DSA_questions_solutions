# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        row_num = -1

        while l <= r:
            mid = l + (r - l) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row_num = mid
                break
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                r = mid - 1
        # print(row_num)
        row = matrix[row_num]
        l = 0
        r = len(row) - 1
        ans = -1
        while l <= r:
            mid = l + (r - l) // 2
            if row[mid] == target:
                return True
            elif target > row[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return False