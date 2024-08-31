# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        s = []
        l = []
        
        c = root
        
        while(True):
            if c is not None:
                s.append(c)
                c = c.left
                
            elif len(s) > 0:
                c = s.pop()
                l.append(c.val)
                c = c.right
                
            else: 
                break
                
        return l
                
                
      
        