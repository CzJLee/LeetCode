"""
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

 

Example 1:


Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
Example 2:


Input: root = [2,1,3]
Output: [2,1,3]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 105
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def traverse_tree(self, root) -> list[int]:
        node_values = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            node_values.append(node.val)
            dfs(node.right)
        
        dfs(root)

        return node_values
    
    def build_binary_tree(self, values: list[int]) -> TreeNode:
        if not values:
            return None
        if len(values) == 1:
            return TreeNode(values[0])
        
        # Get middle index
        i = len(values) // 2
        root = TreeNode(
            val = values[i],
            left = self.build_binary_tree(values[:i]),
            right = self.build_binary_tree(values[i+1:])
        )
        return root

    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Rebuild a tree going in order.
        node_values = self.traverse_tree(root)
        return self.build_binary_tree(node_values)
