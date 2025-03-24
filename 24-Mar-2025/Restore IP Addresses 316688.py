# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        ans = []
        def helper(i, path):
            if i >= n:
                if len(path) == 4:
                    ans.append(".".join(path))
                return 
            if len(path) > 4:
                return

            for j in range(i, n):
                curr_str = s[i : j + 1]
                if str(int(curr_str)) != curr_str or not (0 <= int(curr_str) <= 255):
                    continue
                path.append(curr_str)
                helper(j + 1, path)
                path.pop()
        
        helper(0, [])
        return ans


