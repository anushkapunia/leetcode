# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        self.p = None
        self.f = None
        self.s = None
        def inorder(root):
            if root is None:
                return None
            
            inorder(root.left)
            
            if self.p and self.p.val > root.val:
                if self.f is None:
                    self.f = self.p
                self.s = root
            self.p = root
            
            inorder(root.right)
            
        inorder(root)
        
        self.f.val , self.s.val = self.s.val , self.f.val
            
            
      
        