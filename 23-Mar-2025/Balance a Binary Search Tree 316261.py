# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nums = []
        def helper(root):
            if root:
                helper(root.left)
                nums.append(root.val)
                helper(root.right)
        helper(root)
        
        def construct_tree(l, r):
            if l > r:
                return None
            
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = construct_tree(l, mid - 1)
            root.right = construct_tree(mid + 1, r)
            return root
            
        return construct_tree(0, len(nums) - 1)