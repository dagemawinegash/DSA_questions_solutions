# Problem: Design browser history  - https://leetcode.com/problems/design-browser-history/

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = Node(homepage)
        self.backward_count = 0
        self.forward_count = 0
        
    def visit(self, url: str) -> None:
        temp = Node(url)
        self.curr.next = temp
        temp.prev = self.curr
        self.curr = temp
        self.backward_count += 1
        self.forward_count = 0
        
    def back(self, steps: int) -> str:
        for _ in range(min(steps, self.backward_count)):
            self.curr = self.curr.prev
            self.backward_count -= 1
            self.forward_count += 1
            
        return self.curr.val

    def forward(self, steps: int) -> str:
        for _ in range(min(steps, self.forward_count)):
            self.curr = self.curr.next
            self.backward_count += 1
            self.forward_count -= 1

        return self.curr.val


        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)