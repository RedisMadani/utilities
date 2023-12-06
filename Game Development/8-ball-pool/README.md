# 8 Ball Pool Game

![8ball](https://github.com/RedisMadani/8-ball-pool/assets/136177376/d4fa31db-6ab1-4456-a925-6d64c190f5b5)

This is a simple implementation of the classic game "8 Ball Pool" using Pygame. The game features a pool table, balls, pockets, and a cue stick. The objective of the game is to pocket all the balls using the cue ball.

## How to Play

1. Install Python and Pygame.
   - Make sure you have Python installed on your system. You can download Python from the official website: https://www.python.org/downloads/
   - To install Pygame, open your command prompt or terminal and run the following command:
     ```
     pip install pygame
     ```

2. Clone the repository or download the source code.
   - Clone the repository by running the following command in your command prompt or terminal:
     ```
     git clone [https://github.com/RedisMadani/8-ball-pool.git]
     ```
   - Alternatively, you can download the source code as a ZIP file and extract it.

3. Run the game.
   - Navigate to the directory where the source code is located.
   - Open the `main.py` file in a text editor and make any desired modifications (optional).
   - Run the game by executing the following command:
     ```
     python main.py
     ```

4. Gameplay Controls:
   - Use the mouse to control the cue stick.
   - Click and hold the left mouse button to adjust the power and direction of your shot.
   - Release the left mouse button to strike the cue ball and initiate the shot.

5. Game Rules:
   - The player starts by placing the cue ball behind the white line.
   - The objective is to pocket all the solid or striped balls depending on the assigned category.
   - Players take turns and continue shooting until they fail to pocket a ball or commit a foul.
   - Pocketing the cue ball or scratching is considered a foul.
   - After a foul, the opposing player gets a chance to place the cue ball anywhere on the table.
   - The game ends when all the balls of a player's assigned category are pocketed, followed by pocketing the 8-ball.

## Game Features

- Realistic physics simulation for ball movement and collision.
- Multiple colored balls including solid, striped, and the black 8-ball.
- Interactive cue stick control for aiming and shooting.
- Visual representation of pockets to pocket balls.
- Score tracking and turn-based gameplay.

## Dependencies

- Python 3.x
- Pygame

## Acknowledgements

This game is developed using the Pygame library, which provides a simple and intuitive framework for building games in Python.

## License

The source code is available under the [MIT License](LICENSE).

