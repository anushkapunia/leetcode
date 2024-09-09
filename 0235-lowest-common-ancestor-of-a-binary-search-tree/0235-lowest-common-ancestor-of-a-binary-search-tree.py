# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
   
        if root is None:
            return None  # Return None explicitly if root is None (tree is empty)
        
        # If both nodes are smaller than the current node, search in the left subtree
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # If both nodes are larger than the current node, search in the right subtree
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # If the nodes are on different sides, or one node is the current root, return the root
        else:
            return root