class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        ones_count = [0] * (n + 1)
        ones_count[0] = 0
        ones_count[1] = 1

        last_pow_of_2 = 1

        for i in range(2, n + 1):
            if i == 2 * last_pow_of_2:
                last_pow_of_2 = i
                ones_count[i] = 1
            else:
                ones_count[i] = ones_count[last_pow_of_2] + ones_count[i - last_pow_of_2]
        
        return ones_count
