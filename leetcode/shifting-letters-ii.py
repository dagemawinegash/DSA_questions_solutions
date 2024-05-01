class Solution:
    def shiftingLetters(self, s, shifts):
        n = len(s)
        total_shifts = [0] * len(s)
    
        for start, end, direction in shifts:
            total_shifts[start] += 1 if direction == 1 else -1
            if end + 1 < n:
                total_shifts[end + 1] += -1 if direction == 1 else 1
                
        cumulative_shifts = 0
        result = ''
        for i in range(n):
            cumulative_shifts += total_shifts[i]
            shifted_char = chr((ord(s[i]) - ord('a') + cumulative_shifts) % 26 + ord('a'))
            result += shifted_char

        return result