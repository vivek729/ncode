from functools import cache

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        2    3   4  5
      1 2    6   24 120    : prefix
        120  60  20 5   1  : suffix 
        """
        if not nums:
            return []

        prefix = 1
        output = [1] * len(nums)

        for i in range(len(output)):
            output[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(output) - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output
