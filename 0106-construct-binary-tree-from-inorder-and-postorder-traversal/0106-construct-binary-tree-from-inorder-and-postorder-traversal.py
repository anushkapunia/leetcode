# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, i, p):
        if not i or not p:
            return None
        
        n = len(p)
        r = TreeNode(p[n-1])
        m = i.index(r.val)
        
        r.left = self.buildTree( i[:m] , p[:m])
        r.right = self.buildTree( i[m+1:] , p[m : n-1])
        
        return r
        