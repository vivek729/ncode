# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         def get_subsets(nums, i, running_subset):
#             if i == len(nums):
#                 all_subsets.append(running_subset)
#                 return

#             # included_i = running_subset.append(nums[i])  # Don't do this; append returns None
#             get_subsets(nums, i + 1, running_subset[:])  # excluded case first, as if include first then item gets added to same list object
            
#             # get_subsets(nums, i + 1, running_subset.append(nums[i])) # Don't do this, again, None passed
#             running_subset.append(nums[i])
#             get_subsets(nums, i + 1, running_subset)  # included i
            
        
#         all_subsets = []
#         get_subsets(nums, 0, [])
#         return all_subsets


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def get_subsets(nums, i, running_subset):
            if i == len(nums):
                all_subsets.append(running_subset.copy())
                return

            running_subset.append(nums[i])
            get_subsets(nums, i + 1, running_subset)
            # included_i = running_subset.append(nums[i])  # Don't do this; append returns None
            running_subset.pop()
            get_subsets(nums, i + 1, running_subset)  # excluded case first, as if include first then item gets added to same list object
            
            # get_subsets(nums, i + 1, running_subset.append(nums[i])) # Don't do this, again, None passed
              # included i
            
        
        all_subsets = []
        get_subsets(nums, 0, [])
        return all_subsets
