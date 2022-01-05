class Solution:
	def maxArea(self, height):
		# A possible greedy algorithm?
		if len(height) <= 1:
			# If height is empty
			return 0

		# Start with pointers on each end. 
		start = 0
		end = len(height) - 1
		max_area = (end - start) * min(height[start], height[end])

		# Keep going until pointers cross
		new_best_found = True
		while new_best_found == True:
			new_best_found = False
			# The only way you can find a bigger area than the bounds, is if you find a height inbetween the end points that is greater than the closest boundary.

			# Move the start pointer
			pointer = start
			min_height = height[pointer]
			while pointer < end:
				pointer += 1
				if height[pointer] > min_height:
					# Computer new area
					area = (end - pointer) * min(height[pointer], height[end])
					if area > max_area:
						max_area = area
						start = pointer
						new_best_found = True
						break

			pointer = end
			min_height = height[pointer]
			while pointer > start:
				pointer -= 1
				if height[pointer] > min_height:
					# Computer new area
					area = (pointer - start) * min(height[start], height[pointer])
					if area > max_area:
						max_area = area
						end = pointer
						new_best_found = True
						break

		return max_area

if __name__ == "__main__":
	solution = Solution()
	print(solution.maxArea([2, 2]))