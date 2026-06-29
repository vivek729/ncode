from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(Counter(s))
        print(type(Counter(s)))
        return Counter(s) == Counter(t)