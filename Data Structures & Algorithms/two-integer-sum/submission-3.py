class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        snums = sorted([(i, num) for i, num in enumerate(nums)], key=lambda x: x[1])
        
        lb = 0
        ub = len(snums) - 1
        while lb < ub:
            cur_sum = snums[lb][1] + snums[ub][1]
            if cur_sum == target:
                return sorted([snums[lb][0], snums[ub][0]])
            elif cur_sum < target:
                lb += 1
            else:
                ub -= 1
