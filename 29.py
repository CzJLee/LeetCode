# https://leetcode.com/problems/divide-two-integers/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Implement floor division

        # Check edge case
        if dividend == -(2**31) and divisor == -1:
            return (2**31 - 1)
        
        # XOR
        negative = (dividend >= 0) ^ (divisor >= 0)
        
        a = abs(dividend)
        b = abs(divisor)
        
        if a - b < 0:
            return 0

        def log_div(a, b, n):
            if a - b - b < 0:
                return a - b, n
            else:
                remainder, quotient = log_div(a, b+b, n+n)
                if remainder >= b:
                    remainder -= b
                    quotient += n
                    return remainder, quotient
                else:
                    return remainder, quotient
        
        _, q = log_div(a, b, 1)
        
        if negative:
            return -q
        else:
            return q
        