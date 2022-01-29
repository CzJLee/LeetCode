# https://leetcode.com/problems/largest-rectangle-in-histogram/
class Solution:
	def largestRectangleArea(self, heights: List[int]) -> int:
		if len(heights) == 0:
			return 0

		min_height = min(heights)
		min_index = heights.index(min_height)

		return max(min_height * len(heights), self.largestRectangleArea(heights[:min_index]), self.largestRectangleArea(heights[min_index+1:]))