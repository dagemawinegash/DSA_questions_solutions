# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(root, curr_min, curr_max):
            if not root:
                return curr_max - curr_min

            curr_min = min(root.val, curr_min)
            curr_max = max(root.val, curr_max)

            left_side = helper(root.left, curr_min, curr_max)
            right_side = helper(root.right, curr_min, curr_max)
            
            return max(left_side, right_side)
        
        return helper(root, float("inf"), float("-inf"))