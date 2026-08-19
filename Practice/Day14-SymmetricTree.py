class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        # Base Case 1: Both are empty -> Symmetric
        if not t1 and not t2: 
            return True
        # Base Case 2: One is empty, the other isn't -> Not symmetric
        if not t1 or not t2: 
            return False
        # Base Case 3: Values don't match -> Not symmetric
        if t1.val != t2.val: 
            return False
        
        # Check outer pairs and inner pairs recursively
        return self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)
