# Rock Paper Scissors Game

This script allows you to play the classic game of Rock Paper Scissors against the computer. You can specify the number of games you want to play, and the script will keep track of your score and the computer's score.

## Usage

1. Run the script using a Python environment.
2. Enter the number of games you want to play when prompted.
3. Enter your choice for each game by typing 'R' for Rock, 'P' for Paper, or 'S' for Scissors. The script will take the first character of your input.
4. The computer will randomly select its choice (Rock, Paper, or Scissors).
5. The script will determine the winner for each game based on the Rock Paper Scissors rules:

   - Rock beats Scissors
   - Scissors beats Paper
   - Paper beats Rock

6. The script will display the current score after each game.
7. After playing the specified number of games, the final score will be displayed.
8. The script will announce the winner: either you, the computer, or if it's a tie.

## Note

- The script handles invalid input by printing "INVALID INPUT" and allowing you to enter a valid choice again.
- The user's input is not case-sensitive. It accepts both uppercase and lowercase characters.
- The computer's choice is randomly generated using the `random.choice()` function.
- The script uses a dictionary (`my_dict`) to map the input characters to their corresponding choices (Rock, Paper, or Scissors).

## License

This script is licensed under the [MIT License](LICENSE).