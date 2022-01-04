import math
class Solution: 
	def longestPalindrome(self, s: str) -> str:
		# Move along s, and check sides.
		# If pal, keep moving, else move to next index
		longest_pal = ""

		for i in range(len(s) * 2):
			left_index = math.floor(i / 2)
			right_index = math.ceil(i / 2)
			test_str = s[left_index : right_index + 1]
			while test_str[0] == test_str[-1]:
				if len(test_str) > len(longest_pal):
					longest_pal = test_str
				
				# Check next
				left_index -= 1
				right_index += 1
				if left_index >= 0 and right_index < len(s):
					test_str = s[left_index : right_index + 1]
				else:
					break
		
		return longest_pal