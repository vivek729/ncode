class Solution:
    
    def encode(self, strs: List[str]) -> str:
        """
        4 3 2

        decode:
        0 3, 4 6, 7, 8
        """
        if not strs:
            return ""
        res = ""
        lengths = [str(len(s)) for s in strs]
        lengths = ",".join(lengths)
        mergedstr = "".join(strs)
        res = f'{lengths};{mergedstr}'
        return res

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        delim_index = s.find(';')
        lengths, mergedstr = s[0 : delim_index], s[delim_index + 1 : ]
        lengths = lengths.split(',')
        orig = []
        open_ub = 0
        for lt in lengths:
            cur_lb = open_ub
            open_ub = cur_lb + int(lt)
            orig.append(mergedstr[cur_lb : open_ub])
            # cur_lb = open_ub

        return orig
