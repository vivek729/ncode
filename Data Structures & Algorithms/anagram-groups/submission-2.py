class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)
        for word in strs:
            char_counts = [0] * 26
            for c in word:
                char_counts[ord(c) - ord('a')] += 1
            grouped[tuple(char_counts)].append(word)

        return list(grouped.values())
