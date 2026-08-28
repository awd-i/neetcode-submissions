from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        connectedComponent = 0
        seen = set()

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(num):
            seen.add(num)
            for child in graph[num]:
                if child not in seen:
                    dfs(child)
        
        for i in range(n):
            if i not in seen:
                connectedComponent += 1
                dfs(i)
        
        return connectedComponent
        
        
        
        