class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		# Sort the list
		sorted_nums = sorted(nums)
		# Start by adding the largest and smallest. 
		# If the sum is larger than the target, move on to the next value. 
		# If the sum is smaller than the target, try the next value larger than smallest.
		start_pointer = 0
		end_pointer = int(len(sorted_nums) - 1)

		while start_pointer < end_pointer:
			if sorted_nums[start_pointer] + sorted_nums[end_pointer] > target:
				start_pointer = 0
				end_pointer -= 1
			elif sorted_nums[start_pointer] + sorted_nums[end_pointer] < target:
				start_pointer += 1
			else:
				return [start_pointer, end_pointer]
		
		return None

