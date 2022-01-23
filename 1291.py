# https://leetcode.com/problems/sequential-digits/
class Solution:
	def get_all(self):
		digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
		all = []
		for i in range(2, 10):
			for d in range(1, 11 - i):
				all.append(digits[d:d+i])
		seq_digits = [int("".join(num)) for num in all]
		return sorted(seq_digits)
	def sequentialDigits(self, low: int, high: int) -> List[int]:
		seq_digits = [12, 23, 34, 45, 56, 67, 78, 89, 123, 234, 345, 456, 567, 678, 789, 1234, 2345, 3456, 4567, 5678, 6789, 12345, 23456, 34567, 45678, 56789, 123456, 234567, 345678, 456789, 1234567, 2345678, 3456789, 12345678, 23456789, 123456789]
		selected = [num for num in seq_digits if num >= low and num <= high]
		return selected