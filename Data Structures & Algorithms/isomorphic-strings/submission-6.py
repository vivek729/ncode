class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def both_new_chars(cs, ct):
            if cs not in map_st and ct not in seent:
                return True
            return False

        def both_old_chars(cs, ct):
            if cs in map_st and ct in seent:
                return True
            return False

        if not s and not t:
            return True
        if not s or not t:
            return False
        if len(s) != len(t):
            return False

        map_st = {}
        seent = set()
    
        for i, c in enumerate(s):
            if both_new_chars(c, t[i]):
                map_st[c] = t[i]
                seent.add(t[i])
            elif both_old_chars(c, t[i]) and map_st[c] == t[i]:
                continue
            else:
                return False

        return True
