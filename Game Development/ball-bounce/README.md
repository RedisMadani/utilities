# Ball Bounce Simulation

![gif](https://github.com/RedisMadani/ball-bounce/assets/136177376/a4446f42-9718-41ae-981b-8dac4613d1c9)

This Python program simulates the bouncing behavior of five balls under gravitational acceleration. The balls also undergo elastic collisions with the walls of the container, creating an engaging visual experience.

## Prerequisites
- Python 3.x
- Pygame library

## Installation
1. Make sure you have Python installed on your system.
2. Install the Pygame library by running the following command:
   ```
   pip install pygame
   ```

## Usage
1. Place the provided images (`background-img.jpg`, `ball.png`) in the same directory as the script file.
2. Run the script using the following command:
   ```
   python ball_bounce.py
   ```
3. Enjoy watching the simulation of the bouncing balls within the window.

## Features
- Simulates the motion of five balls in a container.
- The balls experience gravitational acceleration, causing them to fall downward.
- Elastic collisions occur when the balls hit the walls of the container, resulting in changes in their velocities.
- The simulation is displayed using the Pygame library, providing an interactive graphical experience.

## Customization
You can customize aspects of the simulation according to your preferences:
- Screen Size: The screen size is currently set to 800 pixels (width) by 600 pixels (height). You can modify it by changing the values in the `pygame.display.set_mode()` function call.
- Ball Properties: You can adjust various properties of the balls, such as initial velocity, position, and gravity, by modifying the corresponding attributes in the `ball` class.
- Images: If you want to use different background and ball images, replace the provided image files with your own files, ensuring they have the same filenames.

## Notes
- The simulation uses a basic physics model without accounting for factors like air resistance or friction.
- The balls are initially placed at random positions within the container.
- The simulation runs until the window is closed by clicking the close button.
- The program includes a brief delay (`time.sleep(0.02)`) between frames to control the animation speed.

## License
This script is released under the MIT License. Feel free to modify and use it according to your needs.
