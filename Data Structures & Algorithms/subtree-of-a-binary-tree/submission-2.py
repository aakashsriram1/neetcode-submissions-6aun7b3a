# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(a,b):
            if not a and not b: 
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            return helper(a.left,b.left) and helper(a.right,b.right)
        if not subRoot:
            return True 
        if not root:
            return False
        if helper(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 
            