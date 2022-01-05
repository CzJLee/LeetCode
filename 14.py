class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		pref = ""

		# Find min length of strings
		min_length = len(strs[0])
		for string in strs:
			if len(string) < min_length:
				min_length = len(string)

		for i in range(min_length):
			match = strs[0][i]
			for string in strs:
				if string[i] != match:
					return pref
			pref += match
		
		return pref