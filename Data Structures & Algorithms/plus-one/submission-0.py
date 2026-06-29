class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            sumd = digits[i] + carry
            print(f'looking at {digits[i]}, carry = {carry}')
            if sumd >= 10:
                last_digit = sumd % 10
                carry = 1
            else:
                last_digit = sumd
                carry = 0
            digits[i] = last_digit
        if carry == 1:
            digits.insert(0, 1)
        return digits