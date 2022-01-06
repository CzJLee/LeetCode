class Solution:
	def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
		# Turns out that sort will actually subsort sublists as well. 
		stops = []
		for trip in trips:
			stops.append([trip[1], trip[0]])
			stops.append([trip[2], -trip[0]])
		
		stops.sort()

		for stop in stops:
			capacity -= stop[1]
			if capacity < 0:
				return False
		
		return True

if __name__ == "__main__":
	sol = Solution()
	trips = [[2,5,7],[3,1,5]]
	capacity = 4
	print(sol.carPooling(trips, capacity))