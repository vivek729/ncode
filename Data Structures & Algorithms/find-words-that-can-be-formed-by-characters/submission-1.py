from collections import Counter

class Solution:
    def can_form_word(self, word, chars_freq):
        cf = chars_freq.copy() # prerve original
        for c in word:
            try:
                cf[c] -= 1
                if cf[c] < 0:
                    return False
            except KeyError:
                return False
        return True


    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        chars_freq = Counter(chars)
        for word in words:
            if self.can_form_word(word, chars_freq):
                # print(f'can form {word}')
                res += len(word)

        return res