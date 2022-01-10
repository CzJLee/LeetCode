# https://leetcode.com/problems/count-primes/
import math
import numpy as np
class Solution:
	def countPrimes(self, n: int) -> int:
		if n <= 2:
			return 0
		# Create a sieve 
		nums = np.arange(n, dtype=np.int32)
		for i in range(2, int(math.sqrt(n)) + 1):
			if nums[i] != 0:
				nums[i**2:n:i] = 0
		count = len(np.unique(nums)) - 2
		return count