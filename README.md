# Tic-Tac-Toe-game
Tic-Tac-Toe-game using python

The code consists of two classes: Board and Game.

The Board class has a single method, print_board, which iterates through the cells of the game board and prints them to the command line. The board is represented as a 2D list, with each cell containing either an 'X', an 'O', or a space character (' ') depending on whether it has been played by player X, player O, or is still available for play.

The Game class has several methods:

__init__: This method is called when a new instance of the Game class is created. It initializes the game board, sets the current player to 'X', and sets the game status to 'ongoing'.

make_move: This method is called when a player makes a move. It updates the game board to reflect the move, and then checks if the game has ended in a win or a draw. If the game is still ongoing, it switches the current player.

check_draw: This method checks if the game is a draw, i.e., if the game board is full and there is no winner. It returns True if the game is a draw, and False otherwise.

check_win: This method checks if the game has ended in a win for either player. It checks each row, column, and diagonal of the game board to see if any of them are filled with the same player's symbol. If it finds a winning combination, it returns True. Otherwise, it returns False.

The main code creates an instance of the Game class and enters a while loop to allow the players to take turns making moves. It uses the input function to get the player's move and the print_board method to display the current state of the board. The loop continues until the game is over, and then a message is printed to indicate the final result.
