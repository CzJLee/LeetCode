# https://leetcode.com/problems/rotate-image/
import math
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Slice range
        h_max = len(matrix) // 2
        w_max = math.ceil(len(matrix) / 2)
        
        # Center offset 
        c = [(len(matrix) - 1) / 2] * 2
        
        def rotate(v):
            # Use 90º rotation matrix
            w = [v[0] - c[0], v[1] - c[1]]
            w = [w[1], -w[0]]
            return [int(w[0] + c[0]), int(w[1] + c[1])]
        
        # Get indices
        for h in range(h_max):
            for w in range(w_max):
                v1 = [h, w]
                v2 = rotate(v1)
                v3 = rotate(v2)
                v4 = rotate(v3)
                # print(v1, v2, v3, v4)
                
                # Swap
                matrix[v1[0]][v1[1]], matrix[v2[0]][v2[1]], matrix[v3[0]][v3[1]], matrix[v4[0]][v4[1]] = matrix[v4[0]][v4[1]], matrix[v1[0]][v1[1]], matrix[v2[0]][v2[1]], matrix[v3[0]][v3[1]]
        
        return matrix