class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        # not started with str, as repeated concat to same string - one char at a time is O(n**2)
        encoded = []
        for s in strs:
            encoded.append(f'{len(s)}#{s}')
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        decoded = []
        scan_from = 0
        while scan_from < len(s):
            next_delim_index = s[scan_from:].find('#')
            next_delim_index = scan_from + next_delim_index  # Convert to absolute index
            lt = int(s[scan_from : next_delim_index])

            str_start = next_delim_index + 1
            str_end_open_ub = str_start + lt
            decoded.append(s[str_start : str_end_open_ub])
            scan_from = str_end_open_ub

        return decoded


