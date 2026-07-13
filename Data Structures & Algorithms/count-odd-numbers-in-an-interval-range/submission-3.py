class Solution:
    def is_both_even(self, n1, n2):
        return (n1 % 2 == 0) and (n2 % 2 == 0)
    def is_both_odd(self, n1, n2):
        return (n1 % 2 != 0) and (n2 % 2 != 0) 
    
    def countOdds(self, low: int, high: int) -> int:
        """
        1, 3 - 2; o o nO - 1 = 3 // 2 + 1
                  o o nE -> X

        2, 4 - 1  e e nO - 1 = 3 // 2
                  e e nE -> X  

        1, 4, - 2 o e nE- 2 = 4 // 2
                  o e nO -> X

        2, 5 - 2 e o nE - 2 = 4 // 2
                 e o nO -> X
        """
        if low == high:
            return int(low % 2 != 0)
        n = high - low + 1
        if self.is_both_odd(low, high):
            return n // 2 + 1
        else:
            return n // 2