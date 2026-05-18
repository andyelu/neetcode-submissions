class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        square_sets = [set() for _ in range(9)]

        # populate and check
        for i in range(9):
            for j in range(9):
                if not board[i][j].isnumeric():
                    continue
                if board[i][j] in row_sets[i]:
                    return False
                row_sets[i].add(board[i][j])

                if board[i][j] in col_sets[j]:
                    return False
                col_sets[j].add(board[i][j])

                square_i = i // 3
                square_j = j // 3
                curr_square = square_i * 3 + square_j

                if board[i][j] in square_sets[curr_square]:
                    return False
                square_sets[curr_square].add(board[i][j])

        return True
                
