# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, p, i):
        if not p or not i :
            return None
        
        r = TreeNode(p[0])
        m = i.index(r.val)
        r.left = self.buildTree( p[1:m+1] , i[:m])
        r.right = self.buildTree( p[m+1:] , i[m+1:])
        
        return r
        
        
        
        