class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        placements = []
        res = []
        diag_bslash = set()
        diag_fslash = set()
        cols = set()

        def solve(row):
            if row == n:
                board = []
                for r, c in enumerate(placements):  # careful, don't user `row` as var name here to avoid same name as parmameter
                    board.append(f"{c * '.'}Q{(n - 1 - c) * '.'}")
                res.append(board)

            for col in range(n):
                if is_safe(row, col):
                    placements.append(col)
                    diag_fslash.add(row + col)
                    diag_bslash.add(row - col)
                    cols.add(col)
                    solve(row + 1)
                    # clear states
                    placements.pop()
                    diag_fslash.remove(row + col)
                    diag_bslash.remove(row - col)
                    cols.remove(col)

        def is_safe(r, c):
            if r + c in diag_fslash:
                return False
            if r - c in diag_bslash:
                return False
            if c in cols:
                return False
            return True

        solve(0)
        return res