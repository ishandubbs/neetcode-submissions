class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0


        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        def dfs(row, col):
            if (row < 0 or row == ROWS or col < 0 or col == COLS or grid[row][col] == 0 or (row, col) in visit):
                return 0
            visit.add((row, col))
            return (1 + dfs(row + 1, col) +
                        dfs(row - 1, col) +
                        dfs(row, col + 1) +
                        dfs(row, col - 1))
        area = 0
        for row in range(ROWS):
            for col in range(COLS):
                area = max(area, dfs(row, col))
        return area