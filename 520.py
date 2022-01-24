# https://leetcode.com/problems/detect-capital/
class Solution:
	def detectCapitalUse(self, word: str) -> bool:
		if not (word == word.upper() or word == word.lower() or word == word.title()):
			return False
		return True