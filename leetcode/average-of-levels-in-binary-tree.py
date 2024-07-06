from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> list[float]:
        if not root:
            return []

        queue = deque([root])
        ans = []
        
        while queue:
            level_len = len(queue)
            level_sum = 0
            
            for _ in range(level_len):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ans.append(level_sum / level_len)
        
        return ans
        