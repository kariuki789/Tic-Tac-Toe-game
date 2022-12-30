class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
    
    def print_board(self):
        for row in self.board:
            print(' | '.join(row))
        print()

class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = 'X'
        self.status = 'ongoing'
    
    def make_move(self, row, col):
        if self.board.board[row][col] != ' ':
            print("That space is already occupied. Please try again.")
            return
        self.board.board[row][col] = self.current_player
        if self.check_win():
            self.status = self.current_player + ' wins'
        elif self.check_draw():
            self.status = 'draw'
        else:
            self.current_player = 'O' if self.current_player == 'X' else 'X'
    def check_draw(self):
        for row in self.board.board:
            for cell in row:
                if cell == ' ':
                    return False
        return not self.check_win()
    
    def check_win(self):
        # Check rows
        for row in self.board.board:
            if row[0] != ' ' and row[0] == row[1] == row[2]:
                return True
        # Check columns
        for col in range(3):
            if self.board.board[0][col] != ' ' and self.board.board[0][col] == self.board.board[1][col] == self.board.board[2][col]:
                return True
        # Check diagonals
        if self.board.board[0][0] != ' ' and self.board.board[0][0] == self.board.board[1][1] == self.board.board[2][2]:
            return True
        if self.board.board[0][2] != ' ' and self.board.board[0][2] == self.board.board[1][1] == self.board.board[2][0]:
            return True
        return False
game = Game()

while game.status == 'ongoing':
    # Print the current state of the board
    game.board.print_board()
    
    # Get the current player's move
    row = int(input("Enter a row (0-2): "))
    col = int(input("Enter a column (0-2): "))
    
    # Make the move and check for a win or draw
    game.make_move(row, col)

# Print the final result
if game.status == 'X wins':
    print("X wins!")
elif game.status == 'O wins':
    print("O wins!")
else:
    print("It's a draw.")


