# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Inorder traversal: 
        # Follow left branch until you reach the end, then return the value.
        # Then return the parent value, then go to right branch and repeat. 
        
        traversal = []
        
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            traversal.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return traversal