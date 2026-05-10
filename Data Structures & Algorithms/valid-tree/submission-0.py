class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:  # assuming one connected component, for it to be
                               # acyclic, it must have n-1 edges
            return False

        visited = set()
        adj_list = {i: [] for i in range(n)}

        for n1,n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        def dfs(node):
            visited.add(node)
            for nei in adj_list[node]:
                if nei not in visited:
                    dfs(nei)

        dfs(0)
        
        return len(visited) == n

