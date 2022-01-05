class Solution:
	def maxArea(self, height):
		# A possible greedy algorithm?
		
		# Start with pointers on each end. 
		start = 0
		end = len(height) - 1
		max_area = (end - start) * min(height[start], height[end])

		# Keep going until pointers cross
		while start < end:
			if height[start] < height[end]:
				start += 1
				area = (end - start) * min(height[start], height[end])
				if area > max_area:
					max_area = area
			else:
				end -= 1
				area = (end - start) * min(height[start], height[end])
				if area > max_area:
					max_area = area
		
		return max_area

# if __name__ == "__main__":
# 	solution = Solution()
# 	print(solution.maxArea([2, 2]))