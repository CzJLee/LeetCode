import math
class Solution:
	# Alice is throwing n darts on a very large wall. You are given an array darts where darts[i] = [xi, yi] is the position of the ith dart that Alice threw on the wall.

	# Bob knows the positions of the n darts on the wall. He wants to place a dartboard of radius r on the wall so that the maximum number of darts that Alice throws lies on the dartboard.

	# Given the integer r, return the maximum number of darts that can lie on the dartboard.

	def numPoints(self, darts: list[list[int]], r: int) -> int:
		# Use the hint: If there is an optimal solution, you can always move the circle so that two points lie on the boundary of the circle.

		# For any two points, (x1, y1), (x2, y2), as long as (x1, y1) != (x2, y2), and the distance between the points is less than the diameter, you can draw up to two circles that pass through the points. 

		# 0 Circles if the points are too far away
		# 1 Circle if the points have a distance equal to the diameter
		# 2 Circles if the points have a distances less than the diameter

		# There is a finite number of point pairs, we can calculate all of them. 

		# The first step then should be to determine the equation of a circle that passes through two points.
		# self.find_circle(p1, p2, r)

		# Now, for every pair of points, find the center. 
		centers = []
		for p1 in range(len(darts)):
			for p2 in range(p1, len(darts)):
				center = self.find_circle_trig(darts[p1], darts[p2], r)
				centers.extend(center)
		
		# Test how many points are inside the circle, centered at every center. 
		tolerance = 1 / (2**16)
		max_num_points = 0
		for cx, cy in centers:
			num_points_contained = 0
			for dx, dy in darts:
				if (cx - dx) ** 2 + (cy - dy) ** 2 <= r ** 2 + tolerance:
					num_points_contained += 1
			max_num_points = max(max_num_points, num_points_contained)
		
		return max_num_points
	
	def find_circle_trig(self, p1, p2, r):
		"""
		Return a list of center coordinates for a circle with radius r that passes through the given two points.

		Args:
			p1 (tuple): First point
			p2 (tuple): Second point
			r (float): Radius of circle

		Returns:
			tuple: List of coordinates of center of circle
		"""
		center = []

		x1, y1 = p1[0], p1[1]
		x2, y2 = p2[0], p2[1]

		dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)

		if dist > r*2:
			# No points possible
			return center

		# Determine the center point between the two points. 
		center_point = ( (x1+x2)/2, (y1+y2)/2 )

		if dist == r*2 or dist == 0:
			# One point possible, circle is in the center of the points. 
			# Or if dist == 0, then points overlap
			center.append(center_point)
			return center
		
		# Find the equation of a circle that passes through both points. 
		# Okay, So I know that the center of the circle has to be on the line perpendicular to the line connecting the two points. 
		# We actually have a right triangle, where the hypotenuse is the radius of the circle. One side length is half the distance of the chord, and we can use pythag theorm to find the last side length. 

		chord_perp_dist = math.sqrt(r**2 - (dist/2)**2)
		
		# So now we have a distance from the center point along the line perp to the chord. We can find the center points of the circle by traveling that distance. We want to use the slope of this line. 

		# Needs a handler if the chord slope is vertical. 
		if x2 - x1 == 0:
			angle = 0
		elif (y2 - y1) == 0:
			angle = math.pi/2
		else:
			chord_slope = (y2 - y1) / (x2 - x1)
			perp_slope = - 1 / chord_slope
			angle = math.atan(perp_slope)

		# The center can be determined by moving a distance chord_perp_dist along the perp_chord line. 
		# You can use trig and angles to get the travel distance from the center point
		circle_center_x1 = center_point[0] + chord_perp_dist * math.cos(angle)
		circle_center_x2 = center_point[0] - chord_perp_dist * math.cos(angle)
		circle_center_y1 = center_point[1] + chord_perp_dist * math.sin(angle)
		circle_center_y2 = center_point[1] - chord_perp_dist * math.sin(angle)

		center = [(circle_center_x1, circle_center_y1), (circle_center_x2, circle_center_y2)]
		return center

	def find_circle(self, p1, p2, r):
		"""
		Return a list of center coordinates for a circle with radius r that passes through the given two points.

		Args:
			p1 (tuple): First point
			p2 (tuple): Second point
			r (float): Radius of circle

		Returns:
			tuple: List of coordinates of center of circle
		"""
		center = []

		x1, y1 = p1[0], p1[1]
		x2, y2 = p2[0], p2[1]

		dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)

		if dist > r*2:
			# No points possible
			return center

		# Determine the center point between the two points. 
		center_point = ( (x1+x2)/2, (y1+y2)/2 )

		if dist == r*2 or dist == 0:
			# One point possible, circle is in the center of the points. 
			# Or if dist == 0, then points overlap
			center.append(center_point)
			return center
		
		# Find the equation of a circle that passes through both points. 
		# Okay, So I know that the center of the circle has to be on the line perpendicular to the line connecting the two points. 
		# So, given an equation of the line, can I find the points on the line that are some distance away from a point? 
		# If I have some point, (x1, y1) and I have a distance, say r, that I want to be r units away from (x2, y2), then 
		# dist = r = sqrt( (x1-x2)**2 + (y1-y2)**2 )
		# And if I have some line, y = m*x + b, then I can write one of the points in terms of the other. Then I am remaining with one unknown which I can solve for. 

		# Determine the line that passes through the points. 
		# Needs a handler if the chord slope is vertical. 
		if x2 - x1 == 0:
			chord_slope = None
			perp_slope = 0
		else:
			chord_slope = (y2 - y1) / (x2 - x1)

		# Needs a handler if chord_slope == 0, to avoid a divide by zero
		# If this is the case, perp_slope == infinity, or in other words, you have a line x = constant. 
		if chord_slope == 0:
			x = center_point[0]

			# Then solve the easier, r^2 = (a-x)^2 + (b-y)^2 for y
			a = x1
			b = y1
			
			# y == b - Sqrt[-a^2 + r^2 + 2 a x - x^2]
			# y == b + Sqrt[-a^2 + r^2 + 2 a x - x^2]

			circle_center_y1 = b - math.sqrt(-a**2 + r**2 + 2*a*x - x**2)
			circle_center_y2 = b + math.sqrt(-a**2 + r**2 + 2*a*x - x**2)
			circle_center_x1 = x
			circle_center_x2 = x

		else:
			if chord_slope is not None:
				perp_slope = - 1 / chord_slope

			# b = y - m*x
			y_int = (center_point[1]) - (perp_slope) * (center_point[0])

			# Solve r^2 = (a - x)**2 + (b - y)**2
			# Using y = perp_slope * x + y_int
			# Solve for x
			# WolframAlpha gives
			# x == (a + b m - d m - Sqrt[-b^2 + 2 b d - d^2 + 2 a b m - 2 a d m - a^2 m^2 + r^2 + m^2 r^2])/(1 + m^2)
			# x == (a + b m - d m + Sqrt[-b^2 + 2 b d - d^2 + 2 a b m - 2 a d m - a^2 m^2 + r^2 + m^2 r^2])/(1 + m^2)

			m = perp_slope
			d = y_int
			a = x1
			b = y1

			circle_center_x1 = (a + b*m - d*m - math.sqrt(-b**2 + 2*b*d - d**2 + 2*a*b*m - 2*a*d*m - a**2 * m**2 + r**2 + m**2 * r**2))/(1 + m ** 2)
			circle_center_x2 = (a + b*m - d*m + math.sqrt(-b**2 + 2*b*d - d**2 + 2*a*b*m - 2*a*d*m - a**2 * m**2 + r**2 + m**2 * r**2))/(1 + m ** 2)
			circle_center_y1 = m * circle_center_x1 + d
			circle_center_y2 = m * circle_center_x2 + d

		center = [(circle_center_x1, circle_center_y1), (circle_center_x2, circle_center_y2)]
		return center

# if __name__ == "__main__":
# 	sol = Solution()
# 	p1 = (0, -1)
# 	p2 = (0, 1)
# 	r = 2
# 	center = sol.find_circle(p1, p2, r)
# 	print(center)
