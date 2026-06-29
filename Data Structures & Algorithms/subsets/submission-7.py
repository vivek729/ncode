class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def get_subsets(nums, i, running_subset):
            if i == len(nums):
                all_subsets.append(running_subset.copy())
                return

            get_subsets(nums, i + 1, running_subset)
            
            running_subset.append(nums[i])
            get_subsets(nums, i + 1, running_subset)
            running_subset.pop()
        
        all_subsets = []
        get_subsets(nums, 0, [])
        return all_subsets
