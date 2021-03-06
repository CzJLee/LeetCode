# https://leetcode.com/problems/trapping-rain-water/

# Double stack method
class Solution:
    def trap(self, height: List[int]) -> int:
        # Consider a creative stack approach 
        # Add elements until you find one equal to or larger than the rest of the stack
        # At the end of stack, pop element, if larger than last, count water, otherwise move on to next
        # Actually the last element in the stack will be the tallest point, so you can run the algorithm in reverse on the stack 
        
        total = 0

        if len(height) <= 2:
            return 0

        stack = [height.pop(0)]

        for _ in range(2):
            for x in height:
                if x >= stack[0]:
                    # Process elements
                    
                    # Get water level height
                    water_level = min(x, stack[0])
                    # Get width of water channel
                    dist = len(stack) - 1
                    # Calculate elevation
                    elevation_area = sum(stack[1:])
                    # Calculate added water
                    total += (water_level * dist) - elevation_area
                    
                    # Clear stack
                    stack = [x]
                else:
                    # Add to stack
                    stack.append(x)
                
            # After one pass, the stack should contain the greatest element on the left, and everything to the right should be smaller 
            
            # Reverse the process on the remaining stack
            if len(stack) <= 2:
                return total
            else:
                height = list(stack[::-1])
                stack = [height.pop(0)]