# https://leetcode.com/problems/largest-rectangle-in-histogram/
class Solution:
	def largestRectangleArea(self, heights: List[int]) -> int:
		if len(heights) == 1:
			return heights[0]

		areas = set()
		all_heights = sorted(list(set(heights)))
		heights = [list(heights)]
		
		# Start at bottom and rise up
		def split(heights, value):
			split_heights = []
			segment = []
			for x in heights:
				for height in x:
					if height > value:
						segment.append(height)
					elif height == value:
						if len(segment) >= 1:
							split_heights.append(segment)
						segment = []
				if len(segment) >= 1:
					split_heights.append(segment)
				segment = []
			return split_heights

		current_height = all_heights[0]
		while len(all_heights) > 0:
			# print(heights)
			# Calculate all areas of segments
			for segment in heights:
				area = current_height * len(segment)
				areas.add(area)
			# Cut off bottom
			heights = split(heights, current_height)
			# Rise level
			all_heights.pop(0)
			if len(all_heights) > 0:
				current_height = all_heights[0]
		
		return max(areas)


