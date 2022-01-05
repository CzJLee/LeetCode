class Solution:
	def maxArea(self, height):
		# A possible greedy algorithm?
		if len(height) <= 1:
			# If height is empty
			return 0

		# Start with pointers on each end. 
		start = 0
		end = len(height) - 1
		areas = set()
		areas.add((end - start) * min(height[start], height[end]))

		# Keep going until pointers cross
		while start < end:
			if height[start] < height[end]:
				start += 1
				areas.add((end - start) * min(height[start], height[end]))
			else:
				end -= 1
				areas.add((end - start) * min(height[start], height[end]))
		
		return max(areas)

# if __name__ == "__main__":
# 	solution = Solution()
# 	print(solution.maxArea([2, 2]))