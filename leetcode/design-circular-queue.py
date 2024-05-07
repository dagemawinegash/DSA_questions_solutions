class MyCircularQueue:
    def __init__(self, k: int):
        self.size = k
        self.queue = [None] * k
        self.front = 0
        self.rear = -1
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
            self.count += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.front = (self.front + 1) % self.size
            self.count -= 1
            return True
        else:
            return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[self.front]
        else:
            return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.queue[self.rear]
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size

      
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()