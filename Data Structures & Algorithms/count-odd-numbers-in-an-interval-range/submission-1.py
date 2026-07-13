class Solution:
    def is_both_even(self, n1, n2):
        return (n1 % 2 == 0) and (n2 % 2 == 0)
    def is_both_odd(self, n1, n2):
        return (n1 % 2 != 0) and (n2 % 2 != 0) 
    
    def countOdds(self, low: int, high: int) -> int:
        """
        1, 3 - 1; o e
        2, 4 - 2  e e
        1, 4, - 2 o o
        2, 5 - 2 e o
        """
        if low == high:
            return int(low % 2 != 0)
        n = high - low + 1
        if self.is_both_even(low, high) or self.is_both_odd(low, high):
            return n // 2 + 1
        else:
            return n // 2