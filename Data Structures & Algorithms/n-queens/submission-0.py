class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        column = set()
        positiveDiagonal = set() # (r + c)
        negativeDiagonal = set() # (r - c)

        result = []
        board = [["."] * n for i in range(n)] # dot indicates an empty spot

        def backtrack(row):
            if row == n: # base case
                copy = ["".join(row) for row in board]
                result.append(copy)
                return

            for col in range(n):
                if col in column or (row + col) in positiveDiagonal or (row - col) in negativeDiagonal:
                    continue
                column.add(col)
                positiveDiagonal.add(row + col)
                negativeDiagonal.add(row - col)
                board[row][col] = "Q"

                backtrack(row + 1)

                column.remove(col)
                positiveDiagonal.remove(row + col)
                negativeDiagonal.remove(row - col)
                board[row][col] = "."
        backtrack(0)
        return result