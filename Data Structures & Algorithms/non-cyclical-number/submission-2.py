class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(k):
            ss = 0
            while k > 0:
                ss += (k % 10) ** 2
                k //= 10

            return ss

        slow = sum_of_squares(n)
        fast = sum_of_squares(sum_of_squares(n))

        while True:
            if slow == 1 or fast == 1:
                return True
            if slow == fast:
                return False
            slow = sum_of_squares(slow)
            fast = sum_of_squares(sum_of_squares(fast))
