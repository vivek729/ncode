class Solution:
    def get_contf(self, s):
        last_char = s[0]
        contf = []
        cur_count = 0
        for c in s:
            if c == last_char:
                cur_count += 1
                last_char = c
            else:
                contf.append(cur_count)
                last_char = c
                cur_count = 1
        if cur_count:
            contf.append(cur_count)
        return contf

    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s and not t:
            return True
        if not s and t:
            return False
        if s and not t:
            return False
        if len(set(s)) != len(set(t)):
            return False
        contf1 = self.get_contf(s)
        contf2 = self.get_contf(t)

        return sorted(contf1) == sorted(contf2)
