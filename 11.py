class Solution:
	def maxArea(self, height):
		# Brute force O(n^2), compute all possibilities
		areas = set()
		for i in range(len(height)):
			for j in range(i, len(height)):
				area = (j-i) * min(height[i], height[j])
				areas.add(area)
		
		return max(areas)

if __name__ == "__main__":
	solution = Solution()
	print(solution.maxArea([1, 1]))