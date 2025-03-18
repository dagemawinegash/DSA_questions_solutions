# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def helper(first, second, odd):
            if not first:
                return

            if odd:
                temp = second.val
                second.val = first.val
                first.val = temp
                
            odd = not odd
            helper(first.left, second.right, odd)
            helper(first.right, second.left, odd)
            return root
        
        if not root or not root.left:
            return root
        return helper(root.left, root.right, True)

