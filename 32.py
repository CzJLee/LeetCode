def create_mountains(s):
    # Create list of numbers representing the position and height on the x-y axis
    # If "(", add 1
    # If ")", subtract 1
    # If mountain is negative, split list
    
    # ((()())(()))
    #             
    #   /\/\  /\
    #  /    \/  \
    # /          \
    
    mountain_range = []
    mountain = [0]
    height = 0
    for char in s:
        if char == "(":
            height += 1
        elif char == ")":
            height -= 1

        if height >= 0:
            mountain.append(height)
        elif len(mountain) > 1:
                mountain_range.append(mountain)
                mountain = [0]
        if height < 0:
            height = 0
    
    mountain_range.append(mountain)
    return mountain_range

def print_mountain(mountain):
    max_height = max(mountain)
    display = [[" "] * (len(mountain)-1) for _ in range(max_height)]
    height = 0
    parens = ""
    for i, step in enumerate(mountain[1:]):
        if step > height:
            display[max_height - step][i] = "/"
            parens += "("
        else:
            display[max_height - height][i] = "\\"
            parens += ")"
        height = step

    for row in display:
        print("".join(row))
    print("".join(map(lambda x: str(x), mountain[1:])))
    print(parens)
    

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = []
        stack.append(-1)
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len