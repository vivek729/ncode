class Solution:
    def countBits(self, n: int) -> List[int]:
        ones_count = [0] * (n + 1)
        ones_count[0] = 0
        for i in range(1, n + 1):
            ones_count[i] = (i & 1) + ones_count[i >> 1]

        return ones_count
