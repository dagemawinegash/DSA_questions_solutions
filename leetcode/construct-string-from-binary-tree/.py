from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if not node:
                return ""
            
            res = str(node.val)
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left or right:
                res += "(" + left + ")"
            
            if right:
                res += "(" + right + ")"
            
            return res
        
        return dfs(root)

        