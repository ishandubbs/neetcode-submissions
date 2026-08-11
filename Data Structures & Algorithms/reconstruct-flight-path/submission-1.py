class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        # Sort tickets in reverse order so we can pop the lexical smallest from the end
        tickets.sort(reverse=True)
        for src, dst in tickets:
            adj[src].append(dst)
            
        res = []
        def dfs(curr):
            while adj[curr]:
                next_dest = adj[curr].pop()
                dfs(next_dest)
            res.append(curr)
            
        dfs("JFK")
        return res[::-1]