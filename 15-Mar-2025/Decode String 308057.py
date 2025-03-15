# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        n = len(s)
        curr = ""
        num = 0
        stack = []
        while i < n:
            temp_num = ""
            if s[i].isdigit():
                while s[i].isdigit():
                    temp_num += s[i]
                    i += 1
                i -= 1
                num = int(temp_num)
            elif s[i] == "[":
                stack.append(curr)
                stack.append(num)
                num = 0
                curr = ""
            elif s[i] == "]":
                temp_num = stack.pop() 
                prev = stack.pop()
                curr = prev + temp_num * curr
            else:
                curr += s[i]
            i += 1
        return curr




        