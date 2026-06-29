import copy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        allowed = [[1 for _ in range(n)] for _ in range(n)]

        res_boards = []
        def get_boards(board, allowed, row): 
            if row == -1:
                res_boards.append(format_board(board))
                return
            if not any(allowed[row][j] for j in range(n)):
                return  # Don't call for row-1 as need to place all n queens; and already we got a row where none of spots are allowed
            for j in range(n):
    
                if allowed[row][j]:
                    board_copy = copy.deepcopy(board)
                    allowed_copy = copy.deepcopy(allowed)

                    board[row][j] = 'Q'
                    update_allowed((row, j), board, allowed)

                    get_boards(board, allowed, row - 1)

                    board = board_copy
                    allowed = allowed_copy


        def update_allowed(q_pos, board, allowed):
            # update vertical up, diagonal left n right,horizontal left n right(optional)
            row = q_pos[0]
            col = q_pos[1]
            # vertical up
            for i in reversed(range(row)):
                allowed[i][col] = 0


            # diagonal left
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                allowed[i][j] = 0
                i -= 1
                j -= 1

            # diagonal right
            i = row - 1
            j = col + 1
            while i >= 0 and j < len(board):
                allowed[i][j] = 0
                i -= 1
                j += 1

        def format_board(board):
            new_board = [''.join(row) for row in board]
            return new_board

        get_boards(board, allowed, n - 1)
        return res_boards
