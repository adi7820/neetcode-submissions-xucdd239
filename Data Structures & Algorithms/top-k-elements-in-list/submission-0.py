class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        bucket = []

        for _ in range(len(nums) + 1):
            bucket.append([])

        for num, f in freq.items():
            bucket[f].append(num)

        res = []
        for i in range(len(bucket)-1, 0, -1):
            if bucket[i]:
                for item in bucket[i]:
                    res.append(item)

                    if len(res) == k:
                        return res


        