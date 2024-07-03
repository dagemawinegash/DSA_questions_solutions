class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        max_depth = 0
        
        def dfs(node, depth):
            nonlocal max_depth
            if not node.children:
                max_depth = max(max_depth, depth)
                
            for child in node.children:
                dfs(child, depth + 1)

        dfs(root, 1)
        return max_depth
