# https://leetcode.com/problems/count-and-say/
import functools 

class Solution:
    @functools.cache
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            n = list(str(self.countAndSay(n-1)))
            out = ""
            count = 0
            value = 0
            for i in n:
                if value != i:
                    out += str(count)
                    out += str(value)
                    count = 1
                    value = i
                else:
                    count += 1
            out += str(count)
            out += str(value)
            return out[2:]