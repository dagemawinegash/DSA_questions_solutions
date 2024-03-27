class Solution:
    def dividePlayers(self, arr: list[int]) -> int:
        arr.sort()
        n = len(arr)
        target_sum = sum(arr) // (n // 2)  
        p1, p2 = 0, n - 1
        ans = 0
        counter = 0
        while p1 < p2:
            curr_sum = arr[p1] + arr[p2]
            if curr_sum == target_sum:
                ans += arr[p1] * arr[p2]
                p1 += 1
                p2 -= 1
                counter+=1
            elif curr_sum < target_sum:
                p1 += 1
            else:
                p2 -= 1
        if counter==n//2:
            return ans 
        else:
            return -1 