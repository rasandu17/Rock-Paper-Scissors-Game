# Rock, Paper, Scissors Game

A simple console-based Rock, Paper, Scissors game implemented in Python.

## Rules of the Game

- Rock vs Paper -> Paper wins
- Rock vs Scissors -> Rock wins
- Paper vs Scissors -> Scissor wins

## How to Play

1. Clone the repository to your local machine.
2. Run the script in your preferred Python environment.
3. Follow the on-screen instructions to enter your choice (Rock, Paper, or Scissors).
4. See the result of the game - whether you win, lose, or it's a tie.
5. Choose to play again or exit the game.

## Code Structure

- `print_rules()`: Prints the rules of the game.
- `get_user_choice()`: Takes user input for their choice and ensures it is valid.
- `get_computer_choice()`: Generates a random choice for the computer, avoiding a draw with the user.
- `get_result(user_choice, comp_choice)`: Determines the winner of the game.
- `print_result(result, user_choice, comp_choice)`: Prints the result of the game.
- `play_game()`: Initiates and controls the game loop.

## Usage

Run the script and enjoy playing Rock, Paper, Scissors against the computer!

```bash
python rock_paper_scissors.py
