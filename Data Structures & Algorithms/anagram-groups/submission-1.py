from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramroot_words_pairs = []
        for word in strs:
            croot = Counter(word)
            root_exists = False
            for root, word_pairs in anagramroot_words_pairs:
                if croot == root:
                    root_exists = True
                    word_pairs.append(word)
            
            if not root_exists:
                anagramroot_words_pairs.append([croot, [word]])

        res = []
        for _, words in anagramroot_words_pairs:
            res.append(words)
        return res
