class Solution:
	def isMatch(self, s: str, p: str) -> bool:
		if s == p:
			return True
		elif s == "" or p == "":
			return False
		
		s_len = len(s)
		p_len = len(p)
		s_pointer = 0
		p_pointer = 0

		while s_pointer < s_len and p_pointer < p_len:
			if p[p_pointer] == "*":
				letter_to_match = p[p_pointer - 1]
			else:
				letter_to_match = p[p_pointer]
			
			if s[s_pointer] == letter_to_match or letter_to_match == ".":
				# Match
				# Move pointers
				s_pointer += 1
				if p[p_pointer] != "*":
					p_pointer += 1
			elif s[s_pointer] != p[p_pointer] and p[p_pointer] == "*":
				# Check next digit of p
				p_pointer += 1
			elif s[s_pointer] != p[p_pointer] and p[p_pointer + 1] == "*"
			else:
				return False

		# If both pointers exit at the same time, we have a match. 
		# Otherwise, there are still left over values to check, meaning no match.
		if p_pointer == p_len - 1 and p[p_pointer] == "*":
			# Edge case where p exits on "*"
			p_pointer += 1
		if s_pointer == s_len and p_pointer == p_len:
			return True
		else:
			return False
