# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(first, second):
            if not first and not second:
                return True
            if not first or not second:
                return False
            if first.val != second.val:
                return False
            return helper(first.left, second.right) and helper(first.right, second.left)
        return helper(root.left, root.right)
        
