class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)  # Input nums preserved as sorted nums return new list
        res = set()
        for i in range(len(nums)):
            sum3 = nums[i]
            sum2_target = -nums[i]  # 0 - nums[i]
            j = i + 1
            k = len(nums) - 1
            while(j < k):
                if nums[j] + nums[k] == sum2_target:
                    cand = (nums[i], nums[j], nums[k])
                    res.add(cand)
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < sum2_target:
                    j += 1
                else:
                    k -= 1

        return list((list(t)for t in res))