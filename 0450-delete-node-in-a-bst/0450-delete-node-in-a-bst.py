# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):

        if not root:
            return root

        # Search for the node to delete
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node to be deleted is found
            
            # Case 1: Node with only one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Case 2: Node with two children
            # Find the in-order successor (smallest in the right subtree)
            min_larger_node = self.findMin(root.right)
            root.val = min_larger_node.val

            # Delete the in-order successor
            root.right = self.deleteNode(root.right, min_larger_node.val)

        return root

    def findMin(self, node):
        current = node
        while current.left:
            current = current.left
        return current

        