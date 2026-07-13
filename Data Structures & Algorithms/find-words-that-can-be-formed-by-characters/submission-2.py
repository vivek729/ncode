from collections import Counter, defaultdict

class Solution:
    def can_form_word(self, word, chars_freq):
        word_char_freq = defaultdict(int)
        for c in word:
            if c not in chars_freq:
                return False
            word_char_freq[c] += 1
            if word_char_freq[c] > chars_freq[c]:
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