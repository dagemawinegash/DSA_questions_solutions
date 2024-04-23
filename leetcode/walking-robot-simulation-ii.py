class Robot:
    def __init__(self, width: int, height: int):
        self.width = width - 1
        self.height = height - 1
        self.perimeter = (self.width + self.height) * 2
        self.x = 0
        self.y = 0
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.cardinalDir = ["East", "North", "West", "South"]
        self.currDir = 0

    def step(self, num: int) -> None:
        num %= self.perimeter
        if num == 0 and self.x == 0 and self.y == 0:
            self.currDir = 3

        for _ in range(num):
            dx = self.x + self.directions[self.currDir][0]
            dy = self.y + self.directions[self.currDir][1]

            if dx > self.width or dx < 0 or dy > self.height or dy < 0:
                self.currDir = (self.currDir + 1) % 4
                dx = self.x + self.directions[self.currDir][0]
                dy = self.y + self.directions[self.currDir][1]

            self.x = dx
            self.y = dy

    def getPos(self) -> list[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.cardinalDir[self.currDir]