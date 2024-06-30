# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        
        stack = [(root, float("-inf"), float("inf"))]
        while stack:
            currentNode, minValue, maxValue = stack.pop()
            if not currentNode:
                continue

            if currentNode.val <= minValue or currentNode.val >= maxValue:
                return False
                            
            stack.append((currentNode.left, minValue, currentNode.val))
            stack.append((currentNode.right, currentNode.val, maxValue))

        return True
