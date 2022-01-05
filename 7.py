import math
class Solution:
	def reverse(self, x: int) -> int:
		if x == 0:
			return x

		is_negative = True if x < 0 else False
		if is_negative:
			x *= -1
		
		reverse = 0
		num_digits = math.floor(math.log(x, 10) + 1)
		for _ in range(num_digits):
			x, ones = divmod(x, 10)
			# Can only overflow if number has 10 digits (2^31 has 10 digits)
			if num_digits == 10:
				if reverse > 214748364:
					return 0
			reverse = reverse * 10 + ones
		
		if is_negative:
			reverse *= -1
		
		return reverse