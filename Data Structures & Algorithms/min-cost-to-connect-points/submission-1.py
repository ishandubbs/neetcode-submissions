class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        adj = { i:[] for i in range(n) }
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([distance, j])
                adj[j].append([distance, i])

        # Prim's
        result = 0
        visit = set()
        minH = [[0, 0]] # [cost, point]
        while len(visit) < n:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            result += cost
            visit.add(i)
            for neighborCost, neighbor in adj[i]:
                if neighbor not in visit:
                    heapq.heappush(minH, [neighborCost, neighbor])
        return result