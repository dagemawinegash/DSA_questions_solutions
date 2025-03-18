# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def helper(root, curr_path):
            nonlocal ans
            if not root:
                return 
            
            curr_path += str(root.val)

            if not root.left and not root.right:
                ans += int(curr_path)
                return

            helper(root.left, curr_path)
            helper(root.right, curr_path)
        
        helper(root, "")
        return ans

            

        
