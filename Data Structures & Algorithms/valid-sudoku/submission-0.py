class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if len(board) != 9:
            return false # edge case
            #Hash map lets us know if there are any duplicates. 
            #Key is the row col pairs (row/3, col/3), and 
            #value is the hash set where if we have any duplicates or not.
        # Hash map:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) #key = (r / 3, c / 3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue #empty space
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False 
                    #this checks if there are any duplicates
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True