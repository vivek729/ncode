from collections import namedtuple



class Solution:

    def get_nos(self, lst):
        nos = [no for no in lst if no != "."]
        return nos

    def get_block_nos(self, block, board):
        nos = []
        for r in range(block.rs, block.re + 1):
            for c in range(block.cs, block.ce + 1):
                if board[r][c] != ".":  # Easy to miss
                    nos.append(board[r][c])
        return nos


    def is_row_valid(self, row, board):
        return len(set(self.get_nos(board[row]))) == len(self.get_nos(board[row]))

    def is_col_valid(self, col, board):
        nos = self.get_nos([board[i][col] for i in range(0, 9)])
        return len(set(nos)) == len(nos)

    def is_block_valid(self, block, board):
        nos = self.get_block_nos(block, board)
        return len(set(nos)) == len(nos)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        are_rows_valid = all(self.is_row_valid(row, board) for row in range(0, 9))
        if not are_rows_valid:
            return False

        are_cols_valid = all(self.is_col_valid(col, board) for col in range(0, 9))
        if not are_cols_valid:
            return False


        Block = namedtuple('Block', ['rs', 're', 'cs', 'ce'])
        blocks = [
            Block(rs=0, re=2, cs=0, ce=2),
            Block(rs=0, re=2, cs=3, ce=5),
            Block(rs=0, re=2, cs=6, ce=8),

            Block(rs=3, re=5, cs=0, ce=2),
            Block(rs=3, re=5, cs=3, ce=5),
            Block(rs=3, re=5, cs=6, ce=8),

            Block(rs=6, re=8, cs=0, ce=2),
            Block(rs=6, re=8, cs=3, ce=5),
            Block(rs=6, re=8, cs=6, ce=8),
        ]

        # blocks = [Block(rs=rs, re=rs+2, cs=cs, ce=cs+2) for rs in [0, 3, 6] for cs in [0, 3, 6]]

        are_blocks_valid = all(self.is_block_valid(b, board) for b in blocks)
        are_blocks_valid = all(self.is_block_valid(block, board) for block in blocks)
        if not are_blocks_valid:
            return False

        return True


