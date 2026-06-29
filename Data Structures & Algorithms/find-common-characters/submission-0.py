from collections import Counter

class Solution:
    def merge_dicts(self, dict1, dict2):
        commons = set(dict1.keys()) & set(dict2.keys())
        merged_dict = {k : min(dict1[k], dict2[k]) for k in commons}
        return merged_dict

    def commonChars(self, words: List[str]) -> List[str]:
        merged_dict = Counter(words[0]) 

        for word in words[1:]:
            merged_dict = self.merge_dicts(merged_dict, Counter(word))
        
        res = []
        for k in merged_dict:
            v = merged_dict[k]
            while v > 0:
                res.append(k)
                v -= 1
        return res
