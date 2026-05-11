class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # need to check if the graph is connected and acyclic
        visited = set()
        adj_list = {i: [] for i in range(n)}

        for n1,n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for nei in adj_list[node]:
                if nei != parent and not dfs(nei, node):
                    return False

            return True

        # if fully connected, then visited size should be n
        return dfs(0, -1) and len(visited) == n
        
        

