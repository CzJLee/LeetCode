# https://leetcode.com/problems/pour-water/
class Solution:
	def pourWater(self, heights: list[int], volume: int, k: int) -> list[int]:
		# Brute force
		for _ in range(volume):
			# Get current level
			level = heights[k]
			# Check left
			deposit = k
			i = k - 1
			while i >= 0:
				if heights[i] > level:
					# If the wall is higher, can't go any further
					break
				elif heights[i] < level:
					# If the left is lower, deposit there, and keep searching
					deposit = i
					level = heights[deposit]
				i -= 1
			
			# Check right
			if deposit == k:
				# Water did not find a place to settle, check right
				i = k + 1
				while i < len(heights):
					if heights[i] > level:
						# If the wall is higher, can't go any further
						break
					elif heights[i] < level:
						# If the left is lower, deposit there, and keep searching
						deposit = i
						level = heights[deposit]
					i += 1
			
			# Deposit the water where it settles
			heights[deposit] += 1
		
		return heights