# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def helper(node, parent, grandparent):
            nonlocal ans
            if not node:
                return
            if grandparent and not grandparent.val % 2:
                ans += node.val
            helper(node.left, node, parent)
            helper(node.right, node, parent)
        helper(root, None, None)
        return ans
        

            