# using a max heap of size k to keep the heap's binary tree short, making each
# insertion worst case log(k) instead of log(n). We will insert to the max heap,
# and if lenght is greater than k, we pop from it. This leaves us with the smallest
# k elements in the end

import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_dists = []

        for p in points:
            dist = -(p[0] ** 2 + p[1] ** 2)

            heapq.heappush(max_dists, (dist, p[0], p[1]))

            if len(max_dists) > k:
                heapq.heappop(max_dists)

        return [[x,y] for _,x,y in max_dists]