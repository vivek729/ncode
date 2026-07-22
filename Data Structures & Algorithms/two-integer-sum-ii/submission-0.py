class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if numbers is None:
            raise TypeError('`numbers`: List[int], got None')
        if len(numbers) < 2:
            raise ValueError('len < 2')
        lb = 0
        ub = len(numbers) - 1
        while(lb < ub):
            sum2 = numbers[lb] + numbers[ub]
            if sum2 == target:
                return [lb + 1, ub + 1]
            if sum2 < target:
                lb += 1
            else:
                ub -= 1

        return False