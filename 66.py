# https://leetcode.com/problems/plus-one/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        carry = 1
        
        for i in range(len(digits)):
            digits[i] += carry
            if digits[i] == 10:
                carry = 1
                digits[i] = 0
            else:
                carry = 0
            
            if carry == 0:
                break
        
        if carry == 1:
            digits.append(1)
                
        digits.reverse()
        return digits
            