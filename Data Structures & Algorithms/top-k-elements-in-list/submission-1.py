class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        buckets = [[] for i in range(len(nums) + 1)]

        for i in nums:
            count[i] = 1 + count.get(i, 0)
        for num, count in count.items():
            buckets[count].append(num)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
