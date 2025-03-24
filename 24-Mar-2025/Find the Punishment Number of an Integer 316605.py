# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0
        def helper(i, num, s, path):
            if i >= len(s):
                # print(path)
                if sum(path) == num:
                    return True
                return False

            for j in range(i, len(s)):
                path.append(int(s[i : j + 1]))
                if helper(j + 1, num, s, path):
                    return True
                path.pop()
            return False

        for num in range(1, n + 1):
            if helper(0, num, str(num * num), []):
                ans += num * num
        return ans
        
        