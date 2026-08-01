class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        q = deque()

        def addRoom(row, col):
            if (row < 0 or row == ROWS or col < 0 or col == COLS or grid[row][col] == -1 or (row, col) in visit):
                return
            visit.add((row, col))
            q.append([row, col])

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append([row, col])
                    visit.add((row, col))

        distance = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = distance
                addRoom(row + 1, col)
                addRoom(row - 1, col)
                addRoom(row, col + 1)
                addRoom(row, col - 1)
            
            distance += 1