class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        path = set() # can't revisit the same character again

        def dfs(row, col, i):
            if i == len(word):
                return True
            if (row < 0 or col < 0 or         # out of bounds
                row >= ROWS or col >= COLS or # out of bounds
                word[i] != board[row][col] or # characters are not equal
                (row, col) in path):          # tuple is inside of our set
                return False
            
            path.add((row, col)) # add current position to path
            result = (dfs(row + 1, col, i + 1) or
                      dfs(row - 1, col, i + 1) or
                      dfs(row, col + 1, i + 1) or
                      dfs(row, col - 1, i + 1))
            path.remove((row, col)) # no longer at that position
            return result
        
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True
        return False

        # O(n * m * dfs) 4^len(word) = dfs