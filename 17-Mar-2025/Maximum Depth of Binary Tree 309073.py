# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root:
                return 0
            option1 = 1 + helper(root.left)
            option2 = 1 + helper(root.right)
            return max(option1, option2)
        return helper(root)

                

        