# Problem: Same Tree - https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(p, q):
            if not p and not q:
                return True
            if not p or not q or (p.val != q.val):
                return False
            left_side = helper(p.left, q.left)
            right_side = helper(p.right, q.right)
            return left_side and right_side
        return helper(p, q)