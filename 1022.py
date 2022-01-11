# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
		
		def sum_root_recursion(node, binary_string):
			binary_string += str(node.val)
			# Apparently there can be null values... That wasn't in the description. 
			if node.left is None and node.right is None:
				# No children
				# Return the value of the binary string
				return int(binary_string, 2)
			elif node.left is not None and node.right is None:
				# Only one left child
				return sum_root_recursion(node.left, binary_string)
			elif node.right is not None and node.left is None:
				# Only one child
				return sum_root_recursion(node.right, binary_string)
			else:
				# Two children
				return sum_root_recursion(node.left, binary_string) + sum_root_recursion(node.right, binary_string)
		
		binary_string = ""
		return sum_root_recursion(root, binary_string)
