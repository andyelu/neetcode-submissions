class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(numCourses)}
        for c,p in prerequisites:
            adj_list[c].append(p)
        visited_path = set()
        
        # here we should be able to see that if you verify a node cannot have a
        # cycle from it's edges, we don't need to process it further -- we can mark
        # it as safe, which in this case is just making it neighborless in the AL
        def dfs(root):
            if root in visited_path:
                return False
            if not adj_list[root]:  # this node is cycle free if there are no edges
                return True

            visited_path.add(root)
            for c in adj_list[root]:
                if not dfs(c):
                    return False
            visited_path.remove(root)  # remove from visited set after exploring all branches
            adj_list[root] = []  # we know this node is cycle free, just remove edges
                                 # to mark as safe (instead of using a new safe set or something)

            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

            