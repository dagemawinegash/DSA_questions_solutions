# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.count = 0
        self.q = deque()
        
    def consec(self, num: int) -> bool:
        if len(self.q) == self.k:
            if self.q[0] == self.value:
                self.count -= 1
            self.q.popleft()
        
        self.q.append(num)
        if num == self.value:
            self.count += 1
        return self.count == self.k
        

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)