from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        arr = []
        
        def helper(node, depth):
            if node:
                if depth == len(arr): 
                    arr.append(node.val)
                
                helper(node.right, depth + 1)
                helper(node.left, depth + 1)
        
        helper(root, 0)
        return arr