class Solution:
    def isPalindrome(self, s: str) -> bool:
        def advance_i(i):
            while i < len(s) and not s[i].isalnum():
                i += 1
            return i

        def decrement_j(j):
            while j >= 0 and not s[j].isalnum():
                j -= 1
            return j

        if not s:
            return False
        i = 0
        j = len(s) - 1
        while(i < j):
            i = advance_i(i)
            j = decrement_j(j)
            if i > j:
                break
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True