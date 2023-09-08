class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def check_win(self):
        # Check rows, columns and diagonals
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True

        return False

    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def change_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        while True:
            self.print_board()
            print(f"It's {self.current_player}'s turn!")
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))

            if self.board[row][col] == ' ':
                self.board[row][col] = self.current_player

                if self.check_win():
                    self.print_board()
                    print(f"Player {self.current_player} wins!")
                    break

                if self.check_draw():
                    self.print_board()
                    print("It's a draw!")
                    break

                self.change_player()
            else:
                print("Cell already occupied. Try again.")

# Start the game
game = TicTacToe()
game.play()
