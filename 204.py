# https://leetcode.com/problems/count-primes/
class Solution:
	def countPrimes(self, n: int) -> int:
		if n < 2:
			return 0
		# Create a sieve 
		nums = list(range(n))
		for i in nums[2:]:
			if i != 0:
				j = i * 2
				while j < n:
					nums[j] = 0
					j += i
		count = len(set(nums)) - 2
		return count

