class Solution:
    
    def encode(self, strs: List[str]) -> str:
        """
        4 3 2
        0 3, 4 6, 7, 8
        0 4, 4 7, 7  8
        0 4 7 8 

        """
        if not strs:
            return ""
        res = ""
        lengths = [len(s) for s in strs]
        cum_len = [0] * (len(lengths) + 1)
        for i in range(1, len(lengths) + 1):
            cum_len[i] = cum_len[i - 1] + lengths[i - 1]
        cum_len = [str(x) for x in cum_len]
        cum_len = ",".join(cum_len)
        mergedstr = "".join(strs)
        res = f'{cum_len};{mergedstr}'
        return res

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        delim_index = s.find(';')
        cum_len, mergedstr = s[0 : delim_index], s[delim_index + 1 : ]
        cum_len = cum_len.split(',')
        orig = []
        for i in range(0, len(cum_len) - 1):
            orig.append(mergedstr[int(cum_len[i]) : int(cum_len[i + 1])])

        return orig
