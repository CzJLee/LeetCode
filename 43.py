# https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Follow the method taught in elementary school 
        if num1 == 0 or num2 == 0:
            return "0"
        n1 = list(num1)
        n2 = list(num2)
        
        product = 0
        
        n1.reverse()
        n2.reverse()
        
        for i, x in enumerate(n1):
            for j, y in enumerate(n2):
                product += ((int(x) * 10 ** i) * (int(y) * 10 ** j))
        
        return str(product)