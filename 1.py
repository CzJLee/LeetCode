class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		# Use dict to quickly find indices of values
		nums_hash = {}

		for i in range(len(nums)):
			# Starting with a value nums[i], we know that we want to look for a value that is target - nums[i]
			desired_value = target - nums[i]

			if desired_value in nums_hash:
				# If the sum is found, return it
				return [i, nums_hash[desired_value]]

			# Otherwise, add nums[i] to the hash.
			nums_hash[nums[i]] = i