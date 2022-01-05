import itertools as itr
class Solution:
	def letterCombinations(self, digits: str) -> List[str]:
		if digits == "":
			return []
		
		phone_letter = {"2": ["a", "b", "c"], 
						"3": ["d", "e", "f"],
						"4": ["g", "h", "i"], 
						"5": ["j", "k", "l"],
						"6": ["m", "n", "o"],
						"7": ["p", "q", "r", "s"],
						"8": ["t", "u", "v"],
						"9": ["w", "x", "y", "z"]}
		
		list_of_digit_letters = []
		for digit in digits:
			list_of_digit_letters.append(phone_letter[digit])
		
		# Combine all possible combos
		return ["".join(perm) for perm in itr.product(*list_of_digit_letters)]

