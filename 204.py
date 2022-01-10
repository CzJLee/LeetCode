# https://leetcode.com/problems/count-primes/
import math
class Solution:
	def countPrimes(self, n: int) -> int:
		if n <= 2:
			return 0
		# Create a sieve 
		nums = list(range(n))
		for i in range(2, int(math.sqrt(n)) + 1):
			if nums[i] != 0:
				j = i ** 2
				while j < n:
					nums[j] = 0
					j += i
		count = len(set(nums)) - 2
		return count


