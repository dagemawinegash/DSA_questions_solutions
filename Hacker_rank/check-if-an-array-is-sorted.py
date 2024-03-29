class Solution:
    def arraySortedOrNot(self, arr, n):
        i,j = 0,1
        while i < j and j < n:
            if arr[i] <= arr[j]:
                pass
            else:
                return False
            i+=1
            j+=1
        return True