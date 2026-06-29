class Solution:
    def is_open(self, b):
        if b in ('[', '{', '('):
            return True
        return False

    def isValid(self, s: str) -> bool:
        if not s:
            return True 

        closed_to_open_map = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        stack = []

        for b in s:
            if self.is_open(b):
                stack.append(b)
            else:
                if not stack:
                    return False  # expecting open bracket on stack but stack empty
                expected = closed_to_open_map[b]
                got = stack.pop()
                if expected != got:
                    return False

        if stack:
            return False

        return True
