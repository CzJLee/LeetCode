# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Using inorder traversal
        traversal = []
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            traversal.append(node.val)
            inorder(node.right)
        inorder(root)
        
        # Check if in right order and no duplicate values 
        return traversal == sorted(list(set(traversal)))