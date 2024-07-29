from collections import deque
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append((root, 1, 0))  
        ans = 0
        level = 0
        start_pos = 1
        
        while queue:
            node, pos, curr_level = queue.popleft()
            
            if curr_level > level:
                level = curr_level
                start_pos = pos
            
            ans = max(ans, pos - start_pos + 1)
            
            if node.left:
                queue.append((node.left, pos * 2, curr_level + 1))
            if node.right:
                queue.append((node.right, pos * 2 + 1, curr_level + 1))
        
        return ans