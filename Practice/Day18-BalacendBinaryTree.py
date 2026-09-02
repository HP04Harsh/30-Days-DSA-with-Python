# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_height(node: Optional[TreeNode]) -> int:
            # Base case: an empty node has a height of 0
            if not node:
                return 0
            
            # Recursively get the height of left subtree
            left_height = check_height(node.left)
            if left_height == -1:  # Left subtree is unbalanced
                return -1
            
            # Recursively get the height of right subtree
            right_height = check_height(node.right)
            if right_height == -1: # Right subtree is unbalanced
                return -1
            
            # If height difference is > 1, this node is unbalanced
            if abs(left_height - right_height) > 1:
                return -1
            
            # Return actual height of current node
            return max(left_height, right_height) + 1

        # Tree is balanced if helper function doesn't return -1
        return check_height(root) != -1