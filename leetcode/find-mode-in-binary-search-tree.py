from typing import Optional
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []

        freq = defaultdict(int)
        
        def in_order(node):
            if not node:
                return
            in_order(node.left)
            freq[node.val] += 1
            in_order(node.right)
        
        in_order(root)
        
        max_freq = max(freq.values())
        
        ans = []
        for val, num in freq.items():
            if num == max_freq:
                ans.append(val)
        
        return ans