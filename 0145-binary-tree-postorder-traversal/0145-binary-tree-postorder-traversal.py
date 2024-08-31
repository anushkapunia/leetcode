# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        if root is None:
            return []
        s1 = []
        s2 = []
        l = []
        
        s1.append(root)
        
        while s1:
            r = s1.pop()
            s2.append(r)
            
            if r.left:
                s1.append(r.left)
                
            if r.right:
                s1.append(r.right)
                
        while s2:
            v = s2.pop()
            l.append(v.val)
            
        return l
        