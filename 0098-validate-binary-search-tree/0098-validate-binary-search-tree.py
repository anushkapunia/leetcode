# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        s = []
        p = float('-inf')
        c = root
        
        while c or s:
            while c :
                s.append(c)
                c = c.left
            c = s.pop()
            if c.val <= p:
                return False
            
            p = c.val
            c = c.right
            
        return True
            
        
        