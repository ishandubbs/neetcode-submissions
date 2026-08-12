class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        minHeight = [[grid[0][0], 0, 0]] # (time/max_height, r, c)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0, 0))
        while minHeight:
            t, r, c = heapq.heappop(minHeight)
            if r == n - 1 and c == n - 1:
                return t
            for dr, dc in directions:
                neighborR, neighborC = r + dr, c + dc
                if (neighborR < 0 or neighborC < 0 or
                    neighborR == n or neighborC == n or
                    (neighborR, neighborC) in visit):
                    continue
                visit.add((neighborR, neighborC))
                heapq.heappush(minHeight, [max(t, grid[neighborR][neighborC]), neighborR, neighborC])