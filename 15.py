class Solution:
	def threeSum(self, nums: list[int]) -> list[list[int]]:
		if len(nums) < 3:
			return []
		elif len(nums) == 3 and sum(nums) == 0:
			return [nums]

		sol_set = []

		for i in range(len(nums)):
			div_set = nums[i+1:]
			target = 0 - nums[i]
			two_sol = self.twoSum(div_set, target)
			if two_sol:
				for j, k in two_sol:
					if sorted([nums[i], div_set[j], div_set[k]]) not in sol_set:
						sol_set.append(sorted([nums[i], div_set[j], div_set[k]]))
		
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