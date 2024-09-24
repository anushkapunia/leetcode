# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if root is None :
            return root
        q = deque()
        q.appendleft(root)
        
        while q:
            c = q.pop()
            c.left , c.right = c.right , c.left
            
            if c.left:
                q.append(c.left)
            if c.right:
                q.append(c.right)
                
        return root
    
            
            