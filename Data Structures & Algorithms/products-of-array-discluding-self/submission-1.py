from functools import cache

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        2 3 4  5
      1 2 6 24 120 : prefix
        120 60  20 5  1  : suffix 

    i: 0-> len(output) - 1
    ouput[i] = prefix[i] * suffix[i + 1]
         
        """
        if not nums:
            return []
        prefix_prods = [1] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix_prods[i + 1] = prefix_prods[i] * nums[i]

        suffix_prods = [1] * (len(nums) + 1)
        for i in range(len(nums) - 1, -1, -1):
            suffix_prods[i] = suffix_prods[i + 1] * nums[i]
        
        output = []
        for i in range(len(nums)):
            output.append(prefix_prods[i] * suffix_prods[i + 1])

        return output
