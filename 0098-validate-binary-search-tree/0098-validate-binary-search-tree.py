# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def check(root , l = float('-inf') , h = float('inf')):
            if not root:
                return True
            
            if root.val <= l or root.val >= h:
                return False
            
            return check(root.left  , l , root.val ) and check(root.right , root.val , h)
        
        return check(root )
        
        
        
