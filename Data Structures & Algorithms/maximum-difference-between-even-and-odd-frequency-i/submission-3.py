class Solution:
    def maxDifference(self, s: str) -> int:
        freqs = Counter(s)
        max_odd = max(v for k, v in freqs.items() if v % 2 != 0)
        min_even = min(v for k, v in freqs.items() if v % 2 == 0)

        return max_odd - min_even