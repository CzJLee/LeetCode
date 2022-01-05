class Solution:
    def myAtoi(self, s: str) -> int:
        # 1 Strip whitespace
        s = s.strip()
        if s == "":
            return 0
        
        # 2 Detect + or -
        if s[0] == "-":
            is_negative = True 
        else:
            is_negative = False
        if s[0] == "+" or s[0] == "-":
            s = s[1 :]
        
        # 3 Read numbers
        num_string = ""
        while len(s) > 0 and s[0].isdigit():
            num_string += s[0]
            s = s[1 :]
        
        # 4 Convert string to number
        if num_string == "":
            num = 0
        else:
            num = int(num_string)
            
        # 5 Consider sign and clamp
        if is_negative:
            num *= -1
        if num < -(2 ** 31):
            num = -(2 ** 31)
        elif num > (2 ** 31) - 1:
            num = (2 ** 31) - 1
        
        # 6 Return
        return num
        
            
            