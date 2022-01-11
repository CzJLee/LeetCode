# https://leetcode.com/problems/largest-palindrome-product/
class Solution:
	def largestPalindrome(self, n: int) -> int:
		# Math
		# https://medium.com/@d_dchris/largest-palindrome-product-problem-brilliant-approach-using-mathematics-python3-leetcode-479-b3f2dd91b1aa
		if n == 1: return 9
		for z in range(2, 2 * (9 * 10**n) - 1):
			left = 10**n - z
			right = int(str(left)[::-1])
			root_1, root_2 = 0, 0
		
			# no root
			if z**2 - 4*right < 0:
				continue
			# at least one root
			else:
				root_1 = 1/2 * (z + (z**2-4*right)**0.5)
				root_2 = 1/2 * (z - (z**2-4*right)**0.5)
				if root_1.is_integer() or root_2.is_integer():
					return (10**n*left+right) %1337