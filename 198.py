class Solution:
	# This is the problem used in the Dynamic Programing section
	def rob(self, nums: list[int]) -> int:
		# For some house n, you can either chose to rob the house, or skip the house. 
		# If you rob the house, you'd get the money of this house, and all of the houses n-2 before, since you can not take n-1. 
		# If you do not rob the house, you'd be robbing house n-1 instead. 
		# The goal is to find the max of the sum of these.  

		memo = {}

		def rob_house(nums, n):
			# If there is only one house, then you rob that house. 
			# If there are two houses, you pick the max. 

			memo[0] = nums[0]
			memo[1] = max(nums[0], nums[1])
			
			if n in memo:
				return memo[n]
			else:
				memo[n] = max(rob_house(nums, n-1), (nums[n] + rob_house(nums, n-2)))
			
			return memo[n]
		
		return rob_house(nums + [0], len(nums))

if __name__ == "__main__":
	sol = Solution()
	print(sol.rob([2,7,9,3,1]))