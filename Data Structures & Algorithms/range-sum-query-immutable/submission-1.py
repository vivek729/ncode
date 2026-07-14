class NumArray:

    def __init__(self, nums: List[int]):
        self._nums = nums
        self._prefix_sums = None
        self._set_prefix_sums()

    def _set_prefix_sums(self):
        self._prefix_sums = [0]
        for n in self._nums:
            self._prefix_sums.append(self._prefix_sums[-1] + n)
        

    def sumRange(self, left: int, right: int) -> int:
        return self._prefix_sums[right + 1] - self._prefix_sums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)