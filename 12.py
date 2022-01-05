class Solution:
	# Symbol        Value
	# I             1
	# V             5
	# X             10
	# L             50
	# C             100
	# D             500
	# M             1000

	# Constraints 1 <= num <= 3999
	# Lol the constraints are small enough that you could use a lookup table
	def intToRoman(self, num: int) -> str:
		roman = ""

		m, remainder = divmod(num, 1000)
		roman += "M"*m

		c, remainder = divmod(remainder, 100)
		if c == 4:
			roman += "CD"
		elif c == 9:
			roman += "CM"
		elif c >= 5:
			roman = roman + "D" + "C"*(c-5)
		else:
			roman += "C"*c

		x, remainder = divmod(remainder, 10)
		if x == 4:
			roman += "XL"
		elif x == 9:
			roman += "XC"
		elif x >= 5:
			roman = roman + "L" + "X"*(x-5)
		else:
			roman += "X"*x
		
		if remainder == 4:
			roman += "IV"
		elif remainder == 9:
			roman += "IX"
		elif remainder >= 5:
			roman = roman + "V" + "I"*(remainder-5)
		else:
			roman += "I"*remainder

		return roman
