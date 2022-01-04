class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		max_len = 0
		if s == "":
			return max_len

		for i in range(len(s)):
			substring = s[i]
			for j in range(i + 1, len(s)):
				if s[j] not in substring:
					substring += s[j]
				else: 
					break
			max_len = max(max_len, len(substring))

		return max_len
