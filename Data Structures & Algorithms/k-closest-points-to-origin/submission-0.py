import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_dists = []
        heapq.heapify(max_dists)
        dist_map = {}
        res = []

        for p in points:
            dist = -math.sqrt(p[0] ** 2 + p[1] ** 2)

            heapq.heappush(max_dists, dist)

            if dist not in dist_map:
                dist_map[dist] = []
            dist_map[dist].append(p)

            if len(max_dists) > k:
                max_dist = heapq.heappop(max_dists)
                dist_map[max_dist].pop()

        for k,v in dist_map.items():
            if not v:
                continue

            res += v

        return res