"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import functools


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Dynamic programming
        # On each node, starting from bottom up, calculate the max sum to any of its children on each side.
        # Then calculate the sum going across node (left + right + val)
        # Then do the same for each node above
        # Keep track of max sum encountered

        @functools.cache
        def branch_sum(node):
            """Needs to return the max sum of this node and descendants."""
            if node is None:
                return 0

            x = max(
                branch_sum(node.left) + node.val,
                branch_sum(node.right) + node.val,
                node.val,
            )
            # print(x)

            return x

        max_sum = root.val
        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            if node is None:
                continue

            max_sum = max(
                max_sum,
                branch_sum(node.left) + node.val,
                branch_sum(node.right) + node.val,
                branch_sum(node.left) + branch_sum(node.right) + node.val,
                node.val,
            )

            stack.append(node.left)
            stack.append(node.right)

        return max_sum
