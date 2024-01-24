import curses
from random import randint

def main(win):
    # Set up a new window with 20 rows, 60 columns, starting at the top-left of the screen
    win = curses.newwin(20, 60, 0, 0) 

    # Configure the window
    win.keypad(1)  # Enable keypad mode to capture key presses
    curses.noecho()  # Turn off automatic echoing of keys to the window
    curses.curs_set(0)  # Make the cursor invisible
    win.border(0)  # Draw a border around the window
    win.nodelay(1)  # Make getch() non-blocking

    # Initialize the snake and food
    snake = [(4, 10), (4, 9), (4, 8)]  # Starting coordinates of the snake
    food = (10, 20)  # Coordinates of the first food item

    # Set of allowed movement keys (arrow keys)
    allowed_moves = (curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN)

    # Mapping of each move to its opposite
    opposite_moves = {
        curses.KEY_LEFT: curses.KEY_RIGHT,
        curses.KEY_RIGHT: curses.KEY_LEFT,
        curses.KEY_UP: curses.KEY_DOWN,
        curses.KEY_DOWN: curses.KEY_UP
    }

    # Place the first food item on the screen
    win.addch(food[0], food[1], '*')

    # Game logic setup
    score = 0  # Initialize score
    ESC = 27  # ASCII value of the Escape key
    key = curses.KEY_RIGHT  # Initial movement direction of the snake

    try:
        while key != ESC:
            # Display the score at the top of the window
            win.addstr(0, 2, 'Score: ' + str(score) + ' ')

            # Set the speed of the game
            win.timeout(150 - (len(snake)) // 5 + len(snake) // 10 % 120)

            prev_key = key  # Store the previous key pressed
            event = win.getch()  # Get the current key pressed
            key = event if event in allowed_moves else prev_key  # Update key if it's an allowed move

            # Check if the new key is not the opposite of the previous key
            if event in allowed_moves:
                if opposite_moves[key] != prev_key:
                    key = event
                else:
                    key = prev_key

            # Calculate the new head position of the snake
            y = snake[0][0]
            x = snake[0][1]
            if key == curses.KEY_DOWN:
                y += 1
            if key == curses.KEY_UP:
                y -= 1
            if key == curses.KEY_LEFT:
                x -= 1
            if key == curses.KEY_RIGHT:
                x += 1

            # Insert the new head position of the snake
            snake.insert(0, (y, x))

            # Check for collisions with the border or the snake itself
            if y == 1 or y == 18 or x == 0 or x == 58 or snake[0] in snake[1:]:
                break  # End the game if a collision occurs

            # Check if the snake has gotten the food
            if snake[0] == food:
                score += 1  # Increase score
                # Generate new food position
                food = ()
                while food == ():
                    food = (randint(1, 18), randint(1, 58))
                    if food in snake:
                        food = ()
                win.addch(food[0], food[1], '*')  # Place new food
            else:
                # Move the snake
                last = snake.pop()  # Remove the last segment of the snake
                win.addch(last[0], last[1], ' ')  # Clear the last segment from the screen

            # Draw the new head of the snake
            win.addch(snake[0][0], snake[0][1], '#')

    except Exception as e:
        print("error", e)

curses.wrapper(main)
