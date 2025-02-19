# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0] * (len(s) + 1)

        for i, j, num in shifts:
            if num == 0:
                arr[i] -= 1
                arr[j + 1] += 1
            else:
                arr[i] += 1
                arr[j + 1] -= 1
                
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]
        
        ans = []

        for i, char in enumerate(s):
            new_char = ((ord(char) - ord("a") + arr[i]) % 26) + ord("a")
            ans.append(chr(new_char))
        return "".join(ans)
        