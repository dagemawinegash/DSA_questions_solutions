class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        n = len(weights)
        arr = []
        
        for i in range(n - 1):
            arr.append(weights[i] + weights[i + 1])
        
        arr.sort()
        
        min_sum, max_sum = 0, 0
        for i in range(k - 1):
            min_sum += arr[i]
            max_sum += arr[n - i - 2]
        
        return max_sum - min_sum

  