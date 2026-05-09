class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(numCourses)}
        for c,p in prerequisites:
            adj_list[c].append(p)
        visited_path = set()

        def dfs(root):
            if root in visited_path:
                return False
            if not adj_list[root]:
                return True

            visited_path.add(root)
            for c in adj_list[root]:
                if not dfs(c):
                    return False
            visited_path.remove(root)
            adj_list[root] = []

            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

            