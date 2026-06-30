
# TC - O(|t| + k*|t| + |s|); k = distinct chars in t, |t| = len(t), |s| = len(s)
# = O(k*|t| + |s|)

# SC - O(k*|t|)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s and not t:
            return True
        if not s and t:
            return True
        if s and not t:
            return False
        if len(s) > len(t):
            return False

        distinct_tchars = set(t)
        map_tc_next = {c: [len(t)] * (len(t) + 1) for c in distinct_tchars}

        for i in range(len(t) - 1, -1, -1):
            tc = t[i]
            map_tc_next[tc][i] = i
            for c in map_tc_next:
                if c == tc:
                    continue
                map_tc_next[c][i] = map_tc_next[c][i + 1]


        cur_t_index = 0
        for c in s:
            try:
                ind_in_t = map_tc_next[c][cur_t_index]
            except KeyError:  # c not in t OR cur_t_index == len(t)
                return False
            if ind_in_t == len(t):
                return False
            cur_t_index = ind_in_t + 1

        return True

