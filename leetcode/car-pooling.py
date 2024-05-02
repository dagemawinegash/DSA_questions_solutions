class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        passengers = [0] * 1001

        for num, start, end in trips:
            passengers[start] += num
            passengers[end] -= num

        curr_nums = 0
        
        for i in range(1001):
            curr_nums += passengers[i]
            if curr_nums > capacity:
                return False
        return True