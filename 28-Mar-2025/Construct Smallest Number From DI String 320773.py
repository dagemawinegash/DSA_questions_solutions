# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        checked = [False] * 10  

        def helper(i, curr_str):
            if len(curr_str) == n + 1:
                return curr_str  

            for j in range(1, 10): 
                if checked[j]:  
                    continue
                
                if pattern[i] == "I" and curr_str[-1] >= str(j):
                    continue
                if pattern[i] == "D" and curr_str[-1] <= str(j):
                    continue

                checked[j] = True
                res = helper(i + 1, curr_str + str(j))
                if res: 
                    return res
                checked[j] = False 
            
            return ""
                
        for i in range(1, 10):
            checked[i] = True
            ans = helper(0, str(i)) 
            if ans:
                return ans
            checked[i] = False
