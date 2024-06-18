from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        arr = []
        
        def dfs(node, depth):
            if node:
                if depth == len(arr): 
                    arr.append(node.val)
                
                dfs(node.right, depth + 1)
                dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return arr