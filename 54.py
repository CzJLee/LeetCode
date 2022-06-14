import numpy as np
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        matrix = np.array(matrix)
        m, n = np.shape(matrix)
        
        # [0, n] -> [1, m] -> [n-1, 0] -> [m-1, 1]
        
        # Recursive 
        
        # Base cases
        if m == 0 or n == 0:
            return []
        if m == 1:
            return list(matrix[0])
        if n == 1:
            return [x[0] for x in matrix]
        
        # Get outside elements 
        outside_element_list = []
        # Top row
        for i in range(n):
            outside_element_list.append(matrix[0, i])
        # Right col
        for i in range(1, m):
            outside_element_list.append(matrix[i, n-1])
        # Bottom row
        for i in reversed(range(0, n-1)):
            outside_element_list.append(matrix[m-1, i])
        # Left col
        for i in reversed(range(1, m-1)):
            outside_element_list.append(matrix[i, 0])
        
        return outside_element_list + self.spiralOrder(matrix[1:-1, 1:-1])