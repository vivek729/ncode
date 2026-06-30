class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        cur_s_index = 0
        t_index = 0
        while cur_s_index < len(s) and t_index < len(t):
            if t[t_index] == s[cur_s_index]:
                cur_s_index += 1
            t_index += 1
        if cur_s_index < len(s):
            return False
        return True
        