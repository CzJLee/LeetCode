class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
#         # Solve by using sets
#         values = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        
#         possible_values = [[values.copy() if board[i][j] == "." else {board[i][j]} for j in range(9)] for i in range(9)]
        
#         seen = set()
        
#         queue = []
#         for i in range(9):
#             for j in range(9):
#                 if len(possible_values[i][j]) == 1:
#                     queue.append((i, j))
                    
#         while queue:
#             i, j = queue.pop(0)
#             if (i, j) in seen:
#                 continue
#             seen.add((i, j))
#             print((i, j))
            
#             neighbors = []
#             for x in range(9):
#                 neighbors.append((x, j))
#                 neighbors.append((i, x))
#             qi = i // 3
#             qj = j // 3
#             for x in range(3):
#                 for y in range(3):
#                     neighbors.append((qi * 3 + x, qj * 3 + y))
            
#             for neighbor in neighbors:
#                 if neighbor not in seen:
#                     possible_values[neighbor[0]][neighbor[1]] -= possible_values[i][j]
#                     if len(possible_values[neighbor[0]][neighbor[1]]) == 1 and neighbor not in seen:
#                         queue.append(neighbor)
        
#         print(possible_values)
        
#         for i in range(9):
#             for j in range(9):
#                 board[i][j] = possible_values[i][j].pop()

        # Solve using backtracking
        values = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        
        # Find spot with unfilled value
        # Get list of possible values
        # Insert value
        # Move to next spot
        # If no possible values, go back to previous spot and try next value
        
        unfilled_squares = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    unfilled_squares.append((i, j))
        
        def get_neighbors_values(node):
            i, j = node
            values = set()
            for x in range(9):
                values.add(board[x][j])
                values.add(board[i][x])
            qi = i // 3
            qj = j // 3
            for x in range(3):
                for y in range(3):
                    values.add(board[qi * 3 + x][qj * 3 + y])
            return values
        
        def backtrack(board):
            if len(unfilled_squares) == 0:
                return board
            node = unfilled_squares.pop()
            i, j = node
            
            neighbor_values = get_neighbors_values(node)
            possible_values = values.difference(neighbor_values)
            
            for value in possible_values:
                board[i][j] = value
                result = backtrack(board)
                if result is None:
                    continue
                else:
                    return result
            
            board[i][j] = "."
            unfilled_squares.append(node)
            return None
        
        return backtrack(board)
            
            
        
            
                    
        
        