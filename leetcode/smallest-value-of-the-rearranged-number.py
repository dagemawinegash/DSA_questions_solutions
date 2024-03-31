class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        if num > 0:
            Min = float('inf')
            list_nums = [x for x in str(num)]
            for x in list_nums:
                if int(x)!=0:
                    Min = min(Min, int(x))
            MIN = Min
            list_nums.remove(str(Min))
            list_nums.sort()
            return int(str(MIN) + "".join(list_nums))
        elif num < 0:
            list_nums = [x for x in str(num) if x!= "-"]
            list_nums.sort(reverse=True)
            return int("-"+"".join(list_nums))