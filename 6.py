class Solution:
	# P     I    N
	# A   L S  I G
	# Y A   H R
	# P     I
	def convert(self, s: str, numRows: int) -> str:
		if numRows == 1:
			return s
		# The numbers in the columns are always equidistant 
		dist = ((numRows - 1) * 2)

		zigzag = ""
		# First Row
		for i in range(0, len(s), dist):
			zigzag += s[i]
		
		# Middle Rows
		for row in range(1, numRows - 1):
			for i in range(row, len(s), dist):
				zigzag += s[i]
				if i + dist - (row * 2) < len(s):
					zigzag += s[i + dist - (row * 2)]
		
		# Last Row
		for i in range(numRows - 1, len(s), dist):
			zigzag += s[i]
		
		return zigzag
