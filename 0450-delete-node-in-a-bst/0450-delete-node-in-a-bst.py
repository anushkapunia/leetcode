# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, r, k):
        if not r:
            return r
        
        if k < r.val:
            r.left = self.deleteNode(r.left , k)
        elif k > r.val:
            r.right = self.deleteNode(r.right , k)
        else:
            if r.left is None:
                return r.right
            if r.right is None:
                return r.left
            
            m = self.find(r.right )
            r.val = m.val
            r.right = self.deleteNode(r.right , m.val)
            
        return r

            
    
    def find(self , c):
        while c.left:
            c = c.left
        return c