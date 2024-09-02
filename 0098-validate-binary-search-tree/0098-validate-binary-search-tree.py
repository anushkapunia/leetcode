# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
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
        for i in range(1,len(l)):
            if l[i] <= l[i-1]:
                return False
            
        return True
        
                
        