# Space Game

![space_game](https://github.com/RedisMadani/space-game/assets/136177376/0becbfd1-250e-4228-8d27-b05d23e07b47)

This is a simple 2D space game where players control a spaceship and try to avoid colliding with falling space rocks. The goal is to earn as many points as possible by clicking on the falling squares.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/RedisMadani/space-game.git
   ```

2. Navigate to the project directory:
   ```
   cd space-game
   ```

3. Compile the game using CMake:
   ```
   cmake .
   make
   ```

4. Run the game:
   ```
   ./space-game
   ```

## Gameplay

- Use the left and right arrow keys to move the spaceship horizontally.
- The spaceship automatically shoots bullets upwards.
- Clicking on falling squares will earn you points based on their size.
- Smaller squares are worth more points.
- Be careful not to collide with the falling space rocks, as it will decrease your number of lives.
- The game will end when you run out of lives.

## Dependencies

- [SFML](https://www.sfml-dev.org) - Simple and Fast Multimedia Library
  - Installation instructions can be found on the SFML website.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
