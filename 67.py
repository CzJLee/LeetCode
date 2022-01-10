# https://leetcode.com/problems/add-binary/
class Solution:
	def addBinary(self, a, b) -> str:
		# Bit Manipulation Magic
		a, b = int(a, 2), int(b, 2)
		while b:
			a, b = a ^ b, (a & b) << 1
		return bin(a)[2:]
