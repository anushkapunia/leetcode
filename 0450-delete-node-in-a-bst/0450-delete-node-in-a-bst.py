# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def findLastRight(self, root):
        if root.right is None:
            return root
        return self.findLastRight(root.right)

    # Helper function to delete the node
    def helper(self, root):
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        rightChild = root.right
        lastRight = self.findLastRight(root.left)
        lastRight.right = rightChild
        return root.left

    # Function to delete a node in BST
    def deleteNode(self, root, key):
        if root is None:
            return None
        
        # Traverse the tree to find the node to delete
        if root.val == key:
            return self.helper(root)
        
        dummy = root
        while root:
            if key < root.val:
                if root.left and root.left.val == key:
                    root.left = self.helper(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right and root.right.val == key:
                    root.right = self.helper(root.right)
                    break
                else:
                    root = root.right

        return dummy
