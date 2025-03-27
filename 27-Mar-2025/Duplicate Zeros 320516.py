# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        temp = []
        
        for num in arr:
            temp.append(num)
            if num == 0:
                temp.append(0)
            
            if len(temp) >= len(arr):
                break

        arr[:] = temp[:len(arr)]

        