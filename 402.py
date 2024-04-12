"""
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
 

Constraints:

1 <= k <= num.length <= 105
num consists of only digits.
num does not have any leading zeros except for the zero itself.
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Create a stack of length len(num) - k
        # This will hold the final number
        # Start stack from end of num and iterate to the front
        # For each new number encountered, if n <= top of stack
        # Then compare it to the stack.
        # Remove the last increasing element.
        # Fill the stack

        num = list(num)
        stack = []
        # Initialize stack
        if len(num) == k:
            return "0"
        for i in range(len(num) - k):
            stack.append(num.pop())
        
        while num:
            n = num.pop()
            if n <= stack[-1]:
                # Find the first non increasing element of the stack.
                if len(stack) < 2:
                    stack.pop(-1)
                
                else:
                    to_pop_value = "0"
                    to_pop_index = -1
                    for i in range(-1, -(len(stack)+1), -1):
                        if stack[i] < to_pop_value:
                            break
                        else:
                            to_pop_value = stack[i]
                            to_pop_index = i
                    stack.pop(to_pop_index)

                stack.append(n)
        
        # Reverse stack to produce string
        stack.reverse()
        new_num = "".join(stack).lstrip("0")
        return new_num if new_num else "0"
