# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            try:
                top = stack.pop()
                
                if top[0] == char:
                    if top[1] >= k-1:
                        top[1] -= k-1
                        if top[1] > 0:
                            stack.append(top)
                    else:
                        top[1] += 1
                        stack.append(top)
                else:
                    stack.append(top)
                    top = [char, 1]
                    stack.append(top)

            except IndexError:
                top = [char, 1]
                stack.append(top)
            
        # Join stack
        char_list = []
        for char in stack:
            for _ in range(char[1]):
                char_list.append(char[0])
        return "".join(char_list)