# Python Curses Snake Game

## Introduction
This project is a simple implementation of the classic Snake game using Python and the `curses` library. The game, played in a terminal window, features a snake that the player controls to eat food and grow in length.

## Key Features
- Text-based Snake game in the terminal.
- Dynamic speed increase as the snake grows.
- Simple keyboard controls using arrow keys.

## Installation and Running the Game

### Requirements
- Python 3.x
- `curses` package (pre-installed on Unix/Linux systems)
- `windows-curses` package for Windows

### Installation on Windows
Windows users need to install `windows-curses`:
```bash
pip install windows-curses
```

### Running the Game
Execute the Python script in your terminal:
```bash
python snake_game.py
```

## Key Decisions in Development

1. **Using the `curses` Library**: 
   - Chosen for its ability to handle keyboard input and render a text-based user interface in the terminal.

2. **Dynamic Speed Adjustment**:
   - The speed of the snake increases with its length to maintain challenge and engagement.

3. **Simple Keyboard Controls**:
   - Arrow keys are used for movement, making the game intuitive and easy to play.

## Computer Concepts Explained

1. **Game Loop**:
   - At the heart of many games is the "game loop," a continuous cycle that keeps the game running. It repeatedly checks for user inputs (like keyboard presses), updates the game state (like the snake's position), and renders the updated game screen. This loop runs many times per second, making the game interactive and responsive.

2. **Event Handling**:
   - An "event" is any significant action, usually initiated by the user, like pressing a key. In our game, we handle keyboard events to control the snake. When you press an arrow key, the game detects this event and changes the snake's direction accordingly.

3. **Collision Detection**:
   - This is a technique to determine when two objects in the game (like the snake and the wall or food) intersect or come into contact. In our Snake game, we check if the snake's head has collided with the wall or itself, which affects the game's outcome.

4. **Modular Code Structure**:
   - Writing code in a modular way means organizing it into separate sections (functions, classes, modules) where each part handles a specific aspect of the game. This makes the code easier to read, understand, and maintain, especially important for beginners.

5. **Conditional Logic**:
   - Used extensively in game development, conditional logic allows the game to make decisions based on certain conditions, like changing the snake's direction based on which arrow key is pressed, or ending the game if the snake hits a wall.

6. **Variables and Data Types**:
   - Variables store data, like the snake's position or the game score, which can change over time. Different types of data (like numbers, characters, or lists) are used in the game to represent different things, such as the snake, food, or the game window.

## Controls
- Use the arrow keys (`↑`, `↓`, `←`, `→`) to control the snake's direction.
- Press `ESC` to exit the game.

## Conclusion
This Snake game project is an excellent introduction to programming in Python. It demonstrates fundamental concepts in a fun and interactive way, providing a solid foundation for new programmers to build upon.

