# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        if root is None:
            return []

        s = []
        s.append(root)
        l = []
        while len(s) >0:
            p = s.pop()
            
            l.append(p.val)
            
            if p.right:
                s.append(p.right)
                
            if p.left:
                s.append(p.left)
                
        return l
        