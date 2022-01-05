class Solution:
	def isValid(self, s: str) -> bool:
		stack = []

		for char in s:
			if char in {"(", "[", "{"}:
				stack.append(char)
			elif stack:
				# Remove from stack
				if char == ")":
					if stack.pop() != "(":
						return False
				elif char == "]":
					if stack.pop() != "[":
						return False
				elif char == "}":
					if stack.pop() != "{":
						return False
			else:
				# Stack is empty, but we have char
				return False

		return not stack
