# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr_sum = 0
        def helper(root):
            nonlocal curr_sum
            if not root:
                return 
            
            helper(root.right)
            curr_sum += root.val
            root.val = curr_sum
            helper(root.left)
        
        helper(root)
        return root
            