class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        times_val = [(n, v) for n, v in freq.items()]
        times_val.sort(key=lambda x: x[1], reverse=True)
        res = []

        if k > len(times_val):
            raise Exception("not enough distinct elements in nums")

        for i in range(k):
            res.append(times_val[i][0])
        return res