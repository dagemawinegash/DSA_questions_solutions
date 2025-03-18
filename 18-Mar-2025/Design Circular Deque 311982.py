# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:
    def __init__(self, k: int):
        self.size = k
        self.q = [None] * self.size
        self.front = 0
        self.rear = -1
        self.count = 0

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.front = (self.front - 1) % self.size  
            self.q[self.front] = value
            self.count += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.rear = (self.rear + 1) % self.size  
            self.q[self.rear] = value
            self.count += 1
            return True
        return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.front = (self.front + 1) % self.size  
            self.count -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.rear = (self.rear - 1) % self.size
            self.count -= 1
            return True
        return False

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.q[self.front]
        return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.q[self.rear]
        return -1

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size


# Example usage:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
