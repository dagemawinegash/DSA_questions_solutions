# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_min(curr):
            while curr and curr.left:
                curr = curr.left
            return curr.val
            
        def helper(root, key):
            if not root:
                return None

            if key < root.val:
                root.left = helper(root.left, key)
            elif key > root.val:
                root.right = helper(root.right, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    min_val = find_min(root.right)
                    root.val = min_val
                    root.right = helper(root.right, min_val)
            return root
        
        return helper(root, key)


