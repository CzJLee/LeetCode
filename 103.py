"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Collect BFS, then apply zigzag

        zigzag = collections.defaultdict(list)
        queue = []
        queue.append((root, 0))

        while queue:
            node, depth = queue.pop(0)
            if node is None:
                continue
            zigzag[depth].append(node.val)
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))
        
        traversal = []
        for i in range(len(zigzag)):
            # The even rows are Zig, no change.
            if i % 2 == 0:
                traversal.append(zigzag[i])
            # Zag the odd rows
            else:
                traversal.append(zigzag[i][::-1])

        return traversal