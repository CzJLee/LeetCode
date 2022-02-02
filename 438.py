# https://leetcode.com/problems/find-all-anagrams-in-a-string/
from collections import Counter
class Solution:
	def check_anagram(self, s, p):
		s_count = Counter(s)
		p_count = Counter(p)
		return s_count == p_count

	def findAnagrams(self, s: str, p: str) -> List[int]:
		# First check inclusiveness, then check anagram
		p_set = set(list(p))
		p_len = len(p)
		s_len = len(s)
		anagrams = []
		counter = 0
		i = 0
		while i < s_len:
			c = s[i]
			if counter == p_len:
				if self.check_anagram(s[i-p_len:i], p):
					anagrams.append(i-p_len)
				counter -= 1
				continue
			elif c in p_set:
				counter += 1
			else:
				counter = 0
			i += 1
		# Final check
		if counter == p_len:
			if self.check_anagram(s[i-p_len:i], p):
				anagrams.append(i-p_len)
		
		return anagrams