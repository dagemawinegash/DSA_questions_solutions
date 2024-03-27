class Solution:
    def compress(self, chars: list[str]) -> int:
        p1, p2 = 0, 1
        nums = 1
        arr = []
        while p1 < len(chars):
            if p2 == len(chars) or chars[p1] != chars[p2]:
                if nums > 1:
                    arr.append(chars[p1])
                    if nums < 10: 
                        arr.append(str(nums))
                    elif nums >= 10:
                        nums_str = str(nums)
                        for digit in nums_str:
                            arr.append(digit)                
                else:
                    arr.append(chars[p1])
                nums = 1
            elif chars[p1] == chars[p2]:
                nums += 1
            p1 += 1
            p2 += 1     
        for i in range(0, len(arr)):
            chars[i] = arr[i]
        del chars[len(arr):]
        return len(arr)
        

                