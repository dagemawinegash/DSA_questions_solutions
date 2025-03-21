# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def avg_calculate(root):
            count = 0
            curr_sum = 0
            def solve(root):
                nonlocal count
                nonlocal curr_sum
                if not root:
                    return 0
                curr_sum += root.val
                count += 1
                solve(root.left)
                solve(root.right)
                
            solve(root)
            print(curr_sum // count)
            return curr_sum // count
            
        ans = 0

        def helper(root):
            nonlocal ans
            if not root:
                return
            
            if root.val == avg_calculate(root):
                ans += 1
            helper(root.left)
            helper(root.right)
        
        helper(root)
        return ans