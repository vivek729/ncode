class Solution:
    def isPalindrome(self, s: str) -> bool:
        def inc_till_valid_i(s, i):
            while i < len(s) and not s[i].isalnum():
                i += 1
            return i

        def dec_till_valid_j(s, j):
            while j >= 0 and not s[j].isalnum():
                j -= 1
            return j

        i = 0
        j = len(s) - 1
        i = inc_till_valid_i(s, i)
        j = dec_till_valid_j(s, j)

        while i < j:
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
            i = inc_till_valid_i(s, i)
            j = dec_till_valid_j(s, j)

        return True
