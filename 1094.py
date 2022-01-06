import numpy as np
class Solution:
	def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
		# Convert list to array
		trips = np.array(trips, dtype=np.int32)

		num_trips = trips.shape[0]

		# Rearrange format of trips so that it is easier to sequentially step through
		stops = np.ones(shape = (num_trips * 2, 2), dtype=np.int32)

		# Add pickups and dropoffs
		stops[:num_trips, :] = np.column_stack((trips[:, 0], trips[:, 1])) # pickups
		stops[num_trips:, :] = np.column_stack((trips[:, 0] * -1, trips[:, 2])) # dropoffs

		# Sort by location, with subsort sorting dropoffs first
		# https://stackoverflow.com/questions/2828059/sorting-arrays-in-numpy-by-column
		stops = stops[stops[:,0].argsort()] # First sort doesn't need to be stable.
		stops = stops[stops[:,1].argsort(kind='stablesort')]

		for stop in stops:
			# At every stop, reduce capacity if people get in, gain capacity if people leave.
			capacity -= stop[0]
			# If capacity drops below zero, trip fails. 
			if capacity < 0:
				return False
		
		return True

if __name__ == "__main__":
	sol = Solution()
	trips = [[2,5,7],[3,1,5]]
	capacity = 4
	print(sol.carPooling(trips, capacity))