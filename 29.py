# https://leetcode.com/problems/divide-two-integers/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Implement floor division
        
        # XOR
        negative = (dividend >= 0) ^ (divisor >= 0)
        
        a = abs(dividend)
        b = abs(divisor)
        
        if a - b < 0:
            return 0
            
        def log_div(a, b, n):
            if a - b < 0:
                return 0, 0
            else:
                remainder, quotient = log_div(a, b+b, n+n)
                if quotient == 0:
                    return a - b, n
                elif remainder >= b:
                    remainder -= b
                    quotient += n
                    return remainder, quotient
                else:
                    return remainder, quotient
        
        _, q = log_div(a, b, 1)
        
        if negative:
            q = -q
            if q < -(2 ** 31):
                return -(2 ** 31)
            return q
        else:
            if q > (2 ** 31 - 1):
                return 2 ** 31 - 1
            return q
        