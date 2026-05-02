class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones[:] = [-x for x in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            # pop 2 stones -- these are the top 2 heaviest
            # then if difference, add back to heap

            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            if stone1 == stone2:
                continue

            diff = abs(stone2 - stone1)

            heapq.heappush(stones, -diff)

        return 0 if not stones else -stones[0]