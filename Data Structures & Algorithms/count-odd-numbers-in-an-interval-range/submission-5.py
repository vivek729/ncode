class Solution: 
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
        n = high - low + 1
        if low % 2 != 0 and n % 2 != 0:
            return n // 2 + 1
        else:
            return n // 2