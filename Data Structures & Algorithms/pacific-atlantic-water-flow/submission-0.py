class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(row, col, visit, prevHeight):
            if ((row, col) in visit or 
            row < 0 or col < 0 or row == ROWS or col == COLS or
            heights[row][col] < prevHeight):
                return
            visit.add((row, col))
            dfs(row + 1, col, visit, heights[row][col])
            dfs(row - 1, col, visit, heights[row][col])
            dfs(row, col + 1, visit, heights[row][col])
            dfs(row, col - 1, visit, heights[row][col])

        for col in range(COLS):
            dfs(0, col, pac, heights[0][col]) # first row, which is pacific
            dfs(ROWS - 1, col, atl, heights[ROWS - 1][col]) # last row, which is atlantic
        for row in range(ROWS):
            dfs(row, 0, pac, heights[row][0]) # first column
            dfs(row, COLS - 1, atl, heights[row][COLS - 1]) # last column

        # every single position in grid:
        result = []
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in pac and (row, col) in atl:
                    result.append([row, col])
        return result