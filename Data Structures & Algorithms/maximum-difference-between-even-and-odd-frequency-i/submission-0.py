class Solution:
    def maxDifference(self, s: str) -> int:
        freqs = Counter(s)
        odds = (x for x in freqs.values() if x % 2 != 0)
        evens = (x for x in freqs.values() if x % 2 == 0)

        return max(odds) - min(evens)