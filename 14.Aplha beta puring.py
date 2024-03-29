class GameState:
    def __init__(self, board, player):
        self.board = board
        self.player = player

    def get_possible_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '-':
                    moves.append((i, j))
        return moves

    def make_move(self, move):
        i, j = move
        new_board = [row[:] for row in self.board]
        new_board[i][j] = self.player
        return GameState(new_board, 'X' if self.player == 'O' else 'O')

    def is_winner(self):
        # Check rows
        for row in self.board:
            if row.count(row[0]) == 3 and row[0] != '-':
                return True
        # Check columns
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] and self.board[0][j] != '-':
                return True
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '-':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != '-':
            return True
        return False

    def is_terminal(self):
        return self.is_winner() or not any('-' in row for row in self.board)

    def utility(self):
        if self.is_winner():
            return 1 if self.player == 'X' else -1
        return 0


def alpha_beta_pruning(state, alpha, beta):
    if state.is_terminal():
        return state.utility()

    if state.player == 'X':  # Maximizing player
        value = float('-inf')
        for move in state.get_possible_moves():
            new_state = state.make_move(move)
            value = max(value, alpha_beta_pruning(new_state, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:  # Minimizing player
        value = float('inf')
        for move in state.get_possible_moves():
            new_state = state.make_move(move)
            value = min(value, alpha_beta_pruning(new_state, alpha, beta))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value


def find_best_move(state):
    best_move = None
    best_value = float('-inf')
    for move in state.get_possible_moves():
        new_state = state.make_move(move)
        value = alpha_beta_pruning(new_state, float('-inf'), float('inf'))
        if value > best_value:
            best_value = value
            best_move = move
    return best_move


def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


def main():
    board = [['-' for _ in range(3)] for _ in range(3)]
    state = GameState(board, 'X')
    print("Initial Board:")
    print_board(board)

    while not state.is_terminal():
        if state.player == 'X':
            move = find_best_move(state)
        else:
            print("Player O's turn.")
            i, j = map(int, input("Enter row and column: ").split())
            move = (i, j)

        state = state.make_move(move)
        print_board(state.board)

    if state.utility() == 1:
        print("X wins!")
    elif state.utility() == -1:
        print("O wins!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    main()
