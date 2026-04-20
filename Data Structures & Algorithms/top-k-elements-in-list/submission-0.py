class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = []

        for i in range(len(nums)):
            buckets.append([])

        h_map = {}

        for n in nums:
            if n not in h_map:
                h_map[n] = 0

            h_map[n] += 1

        for key,val in h_map.items():
            buckets[val-1].append(key)

        print(buckets)

        res = []

        for i in range(len(nums)-1, -1, -1):
            for j in range(len(buckets[i])):
                res.append(buckets[i][j])
                if len(res) == k:
                    return res