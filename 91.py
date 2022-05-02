# https://leetcode.com/problems/decode-ways/

from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        
        @cache
        def recursiveDecode(s: str):
            if s == "":
                return 0
            elif s[0] == "0":
                return 0
            elif len(s) == 1:
                return 1
            elif len(s) == 2 and int(s) <= 26:
                if s[1] == "0":
                    return 1
                else:
                    return 2

            elif s[0] == "1":
                return recursiveDecode(s[1:]) + recursiveDecode(s[2:])
            elif s[0] == "2" and int(s[1]) <= 6:
                return recursiveDecode(s[1:]) + recursiveDecode(s[2:])
            else:
                return recursiveDecode(s[1:])
                
        return recursiveDecode(s)