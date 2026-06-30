class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        max_so_far_to_right = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            max_so_far_to_right_new = max(max_so_far_to_right, arr[i])
            arr[i] = max_so_far_to_right
            max_so_far_to_right = max_so_far_to_right_new

        arr[-1] = -1
        return arr
