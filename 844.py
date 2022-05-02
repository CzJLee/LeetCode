# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def typed(self, s):
        s_list = []

        for char in s:
            if char == "#":
                if len(s_list) > 0:
                    s_list.pop()
            else:
                s_list.append(char)
            
        return "".join(s_list)

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.typed(s) == self.typed(t)

