class Solution:
	def isMatch(self, s: str, p: str) -> bool:
		if not p:
			return not s

		# Recursive approach
		first_char_match = bool(s) and (p[0] == s[0] or p[0] == ".")
		
		# Check if the pattern has a folowing * char
		if len(p) >= 2 and p[1] == "*":
			# Either keep matching text or Text does not match, move on
			return (first_char_match and self.isMatch(s[1:], p)) or self.isMatch(s, p[2:])
		else:
			# No * to worry about, move on as normal
			return first_char_match and self.isMatch(s[1:], p[1:])