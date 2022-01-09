import numpy as np

class Solution:
	# I think you just have to check for symmetry. If the robot does not end up at the origin after four iterations, then I don't think it is possible for it to be bounded. 
	def isRobotBounded(self, instructions: str) -> bool:
		pos = np.array([0, 0])
		dir = np.array([0, 1])
		left = np.array([[0, -1], [1, 0]])
		right = np.array([[0, 1], [-1, 0]])

		for inst in instructions:
			if inst == "G":
				pos = np.add(pos, dir)
			elif inst == "L":
				dir = np.matmul(left, dir)
			elif inst == "R":
				dir = np.matmul(right, dir)
		
		return np.array_equal(np.array([0, 0]), pos) or not np.array_equal(np.array([0, 1]), dir)