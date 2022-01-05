class Solution:
	def threeSum(self, nums: list[int]) -> list[list[int]]:
		if len(nums) < 3:
			return []

		target = 0
		
		sol_set = []

		nums.sort()

		for i in range(len(nums)):
			if nums[i] > target:
				break
			else:
				two_sols = self.twoSum(nums[i+1:], target - nums[i])
			if two_sols:
				for j, k in two_sols:
					sol = sorted([nums[i], nums[i+j+1], nums[i+k+1]])
					if sol not in sol_set:
						sol_set.append(sol)

		return sol_set
			

	def twoSum(self, nums: list[int], target: int) -> list[int]:
		# Use dict to quickly find indices of values
		nums_hash = {}
		sol_set = []

		for i in range(len(nums)):
			# Starting with a value nums[i], we know that we want to look for a value that is target - nums[i]
			desired_value = target - nums[i]

			if desired_value in nums_hash:
				# If the sum is found, append it
				sol_set.append( [i, nums_hash[desired_value]] )

			# Otherwise, add nums[i] to the hash.
			nums_hash[nums[i]] = i
		
		return sol_set