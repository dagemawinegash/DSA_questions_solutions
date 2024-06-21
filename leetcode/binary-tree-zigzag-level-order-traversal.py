from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        
        queue = deque([root])
        ans = []
        flag = False
        
        while queue:
            arr = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                arr.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            if flag:
                arr.reverse()
            
            ans.append(arr)
            flag = not flag
                
        return ans

        