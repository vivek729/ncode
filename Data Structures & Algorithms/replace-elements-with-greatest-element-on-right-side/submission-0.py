from math import inf

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if not arr:
            return []

        greatest_arr_from_back = [None] * len(arr)
        greatest_so_far = -inf

        for i in range(len(arr) - 1, -1, -1):
            greatest_so_far = max(greatest_so_far, arr[i])
            greatest_arr_from_back[i] = greatest_so_far

        for i in range(len(arr) - 1):
            arr[i] = greatest_arr_from_back[i + 1]

        arr[-1] = -1

        return arr