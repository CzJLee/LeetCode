# https://leetcode.com/problems/reaching-points/
class Solution:
	def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
		# Try a recursive search
		if (sx, sy) == (tx, ty):
			return True
		elif sx > tx or sy > ty:
			# Stopping point is if you exceed values
			return False
		else:
			return self.reachingPoints(sx + sy, sy, tx, ty) or self.reachingPoints(sx, sx + sy, tx, ty)
		
