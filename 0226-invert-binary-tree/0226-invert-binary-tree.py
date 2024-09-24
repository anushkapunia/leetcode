# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if root is None :
            return None
        
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        
        root.right , root.left = root.left , root.right
        
        return root
            