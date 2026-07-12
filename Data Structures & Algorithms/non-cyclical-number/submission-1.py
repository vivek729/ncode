class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            sum_of_squares = 0
            while n > 0:
                d = n % 10
                sum_of_squares += (d ** 2)
                n //= 10
    
            if sum_of_squares == 1:
                return True
            if sum_of_squares in seen:
                return False 
            n = sum_of_squares
            seen.add(sum_of_squares)
