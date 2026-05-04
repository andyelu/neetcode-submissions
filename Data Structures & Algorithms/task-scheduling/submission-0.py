class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()  # each element is (-count, idle time)

        count = Counter(tasks)
        max_heap = [-val for val in count.values()]
        heapq.heapify(max_heap)

        time = 0

        while max_heap or q:
            time += 1

            if max_heap:
                max_count = heapq.heappop(max_heap) + 1
        
                if max_count < 0:
                    q.append((max_count, time+n))

            # check if an idle task can be picked again
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time

