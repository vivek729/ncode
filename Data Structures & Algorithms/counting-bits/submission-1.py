class Solution:
    def countBits(self, n: int) -> List[int]:
        def count1(k):
            cnt = 0
            while k:
                if k % 2 == 1:
                    cnt += 1
                k //= 2
            return cnt

        res = []
        for i in range(0, n + 1):
            ones = count1(i)
            res.append(ones)
        return res