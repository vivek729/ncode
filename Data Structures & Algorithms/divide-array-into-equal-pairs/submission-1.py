class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        values = freq.values()
        res = all(v % 2 == 0 for v in values)
        return res
