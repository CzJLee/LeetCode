# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# BFS First Try

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # The values are unqiue, we simply have to find the node with the matching value
        # Do a search DFS or BFS
        
        target_val = target.val
        
        queue = [cloned]
        
        while queue:
            node = queue.pop(0)
            if node.val == target_val:
                return node
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)