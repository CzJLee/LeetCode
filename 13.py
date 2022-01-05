class Solution:
	def romanToInt(self, s: str) -> int:
		roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
		num = 0
		# Take the front digit. If the following digit is smaller or equal, add the front digit. 
		# If the following digit is larger, then handle that condition \
		while s:
			if len(s) == 1:
				num += roman[s]
				s = s[1:]
			elif roman[s[1]] <= roman[s[0]]:
				num += roman[s[0]]
				s = s[1:]
			else:
				num += roman[s[1]] - roman[s[0]]
				s = s[2:]
		
		return num