# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.size = capacity
        self.left = Node(0, -1)
        self.right = Node(0, -1)
        self.left.next = self.right
        self.right.prev = self.left
    
    def add(self, node):
        last = self.right.prev  
        last.next = node  
        node.prev = last 
        node.next = self.right  
        self.right.prev = node 
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.d:
            self.remove(self.d[key])
            self.add(self.d[key])
            return self.d[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove(self.d[key])
        self.d[key] = Node(key, value)
        self.add(self.d[key])

        if len(self.d) > self.size:
            lru = self.left.next  
            self.remove(lru)  
            del self.d[lru.key]  

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)