class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = { char:set() for word in words for char in word }

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visit = {} # False = visited, True = current path
        result = []

        def dfs(char):
            if char in visit:
                return visit[char]

            visit[char] = True

            for neighbor in adj[char]:
                if dfs(neighbor):
                    return True
            
            visit[char] = False
            result.append(char)
        
        for char in adj:
            if dfs(char):
                return ""

        result.reverse()
        return "".join(result)