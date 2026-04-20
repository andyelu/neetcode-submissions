class Solution:
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.visited = set()
        self.adj_list = {}

        cc_counter = 0

        # construct an adjacency list
        for e in edges:
            # e = [a,b]
            a = e[0]
            b = e[1]

            if a not in self.adj_list:
                self.adj_list[a] = set()
            self.adj_list[a].add(b)

            if b not in self.adj_list:
                self.adj_list[b] = set()
            self.adj_list[b].add(a)

        for n_val in range(n):
            if n_val in self.visited:
                continue

            self.dfs(n_val)

            cc_counter += 1

        return cc_counter

    def dfs(self, n):
        self.visited.add(n)
        
        if n in self.adj_list:
            for val in self.adj_list[n]:
                if val not in self.visited:
                    self.dfs(val)


