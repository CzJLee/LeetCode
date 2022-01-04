class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		# Fine, O(n^2) solution it is then
		pointer_start = 0
		pointer_end = int(len(nums) - 1)

		while pointer_end > 0:
			if nums[pointer_start] + nums[pointer_end] == target:
				return [pointer_start, pointer_end]
			else:
				pointer_start += 1
				if pointer_start >= pointer_end:
					pointer_end -= 1
					pointer_start = 0
		
		return None