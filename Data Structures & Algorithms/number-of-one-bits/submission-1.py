class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        while n:
            # clears away lowest set bit
            n &= (n - 1)
            ones += 1
        return ones