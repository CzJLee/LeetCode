# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
class Solution:
	def findMinArrowShots(self, points: List[List[int]]) -> int:
		dart_count = 0 
		points.sort()
		while points:
			print(points)
			target_val = None
			target_num_bloons = 0
			# Get position with highest bloon pop count
			for x1, x2 in points:
				num_bloons_x1 = 0
				num_bloons_x2 = 0
				for point in points:
					if x1 < point[0]:
						break
					if x1 <= point[1]:
						num_bloons_x1 += 1
				for point in points:
					if x2 < point[0]:
						break
					if x2 <= point[1]:
						num_bloons_x2 += 1
				if num_bloons_x1 >= num_bloons_x2 and num_bloons_x1 > target_num_bloons:
					target_val = x1
					target_num_bloons = num_bloons_x1
				elif num_bloons_x2 > num_bloons_x1 and num_bloons_x2 > target_num_bloons:
					target_val = x2
					target_num_bloons = num_bloons_x2
			print(target_val)
			print(target_num_bloons)
			# Pop bloons
			new_points = []
			last_index = None
			for i, point in enumerate(points):
				if point[0] > target_val:
					last_index = i
					break
				if point[1] < target_val:
					new_points.append(point)
			if last_index:
				new_points.extend(points[last_index:])
			points = new_points
			dart_count += 1
		return dart_count

