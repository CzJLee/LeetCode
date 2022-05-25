import numpy as np

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check if all rows, columns, and grids have unique values 
        board = np.array(board)
        
        def check_unique_counts(a):
            unique_counts = np.unique(a, return_counts = True)
            # print(unique_counts)
            if unique_counts[0][0] == ".":
                if len(unique_counts[0]) > 1:
                    if np.amax(unique_counts[1][1:]) > 1:
                        return False
            else:
                if np.amax(unique_counts[1]) > 1:
                    return False
            return True
            
        print("Checking Rows")
        for row in board:
            if check_unique_counts(row) is False:
                return False
           
        print("Checking Columns")
        for column in np.transpose(board):
            if check_unique_counts(column) is False:
                return False
        
        print("Checking Grids")
        for i in range(3):
            for j in range(3):
                if check_unique_counts(board[i*3:(i+1)*3, j*3:(j+1)*3]) is False:
                    return False
                
        return True