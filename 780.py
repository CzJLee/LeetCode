import time
# https://leetcode.com/problems/reaching-points/
class Solution:
	# Working backward, mod variant to speed up time complexity
	def reachingPoints(self, sx, sy, tx, ty):
		while tx >= sx and ty >= sy:
			if tx == ty:
				break
			elif tx > ty:
				if ty > sy:
					tx %= ty
				else:
					return (tx - sx) % ty == 0
			else:
				if tx > sx:
					ty %= tx
				else:
					return (ty - sy) % tx == 0

		return tx == sx and ty == sy