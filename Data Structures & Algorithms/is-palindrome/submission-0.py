class Solution:
    def isPalindrome(self, s: str) -> bool:
        mod_s = ''.join(c for c in s if c.isalnum()).lower()
        print(mod_s)
        lb = 0
        ub = len(mod_s) - 1
        while lb < ub:
            if mod_s[lb] != mod_s[ub]:
                return False
            lb += 1
            ub -= 1

        return True
