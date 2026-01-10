---
title: PyGame Tutorial – How to Build a Bouncing Ball Game
subtitle: ''
author: Juan P. Romano
co_authors: []
series: null
date: '2024-01-23T22:46:54.000Z'
originalURL: https://freecodecamp.org/news/pygame-tutorial-build-a-bouncing-game
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/bouncing_ball.png
tags:
- name: Game Development
  slug: game-development
- name: pygame
  slug: pygame
- name: Python
  slug: python
seo_title: null
seo_desc: 'In this tutorial, you''ll learn how to create a simple yet funny bouncing
  ball game using the PyGame library.

  Whether you''re a beginner seeking to grasp the fundamentals of game development
  or an enthusiast eager to explore PyGame''s capabilities, this...'
---

In this tutorial, you'll learn how to create a simple yet funny bouncing ball game using the PyGame library.

Whether you're a beginner seeking to grasp the fundamentals of game development or an enthusiast eager to explore PyGame's capabilities, this article is your guide to crafting a simple yet engaging game.

You just need to break down the steps, read the code, and enjoy the ride!

At the end of this tutorial, your game should look like this:

![Image](https://www.freecodecamp.org/news/content/images/2024/01/bouncing_game.png align="left")

## Table of Contents

1. [How to set up the development environment](#heading-how-to-set-up-the-development-environment)
    
2. [Defining the game concept](#heading-defining-the-game-concept)
    
3. [App initialization](#heading-app-initialization)
    
4. [How to create a PyGame instance](#heading-how-to-create-a-pygame-instance)
    
5. [How to create the game screens](#heading-how-to-create-the-game-screens)
    
6. [Main game loop](#heading-main-game-loop)
    
7. [Conclusion](#heading-conclusion)
    

## How to Set Up the Development Environment

### Tools and Software

Before you get into the coding adventure, let's talk about the tools that will fuel your creativity.

#### Python

You'll be using Python, a versatile and beginner-friendly programming language. Its clean syntax and extensive library support make it an excellent choice for game development.

If you don't have Python installed, head over to [python.org](https://www.python.org/) to download and install the latest version.

#### PyGame

Your secret weapon for this project. PyGame, a set of Python modules, simplifies game development by handling multimedia elements like images and sounds. It's the engine that will power your game.

To install PyGame, you can use the following command in your terminal or command prompt:

```bash
pip install pygame
```

#### Text Editor

Whether it's VSCode, PyCharm, or Thonny, these environments offer features like syntax highlighting and debugging tools. Choose the one you're most comfortable with, and let's get ready to write some code!

I will be using VSCode but feel free to use whichever you like. If you feel adventurous, you can try Thonny!

Now that you're armed with the right tools, let's jump into the code and bring your game to life.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/screenshot-1.png align="left")

*This is Thonny*

## Defining the Game Concept

### Game Concept and Mechanics

Let's break down the core concepts and mechanics you'll be implementing.

**Platform Control:**

* Objective: Use arrow keys to move the platform left or right.
    
* Implementation: Your platform moves horizontally based on key input.
    
* Limitations: Ensure the platform stays within the screen boundaries.
    

**Bouncing Ball Dynamics:**

* Objective: Guide the bouncing ball across the screen.
    
* Implementation: The ball moves independently, bouncing off walls and the platform.
    
* Interaction: Score points each time the ball successfully bounces off the platform.
    

**Scoring System:**

* Objective: Accumulate points based on successful bounces.
    
* Implementation: Your coding determines the scoring system.
    
* Challenge: Optimize the scoring mechanism for higher scores.
    

**Level Progression:**

* Objective: Advance through levels as your score reaches milestones.
    
* Implementation: With every 10 points, you progress to a new level.
    
* Challenge: Expect increased difficulty and complexity with each level.
    

**Dynamic Platform Color:**

* Objective: Platform color changes with each level, adding a visual dynamic.
    
* Implementation: Colors are randomly generated upon reaching a new level.
    
* Aesthetic Touch: Adds variety and excitement to the gaming experience.
    

**Lives and Game Over:**

* Objective: Avoid letting the ball fall off the screen to maintain lives.
    
* Implementation: Lives decrease with missed bounces. Game over occurs when lives run out (you have only 3 lives).
    
* Restart: After game over, restart with three lives and a fresh score.
    

## How to Code the Game

### App initialization

In this section, you'll define constants such as screen dimensions, ball and platform properties, and colors.

You'll also initialize PyGame, set up the display screen, and create a clock object to control the frame rate.

Then you'll initialize variables for the game, including ball position, speed, platform position, speed, score, lives, and current level.

Here's the code to do all that:

```python
import pygame
import sys
import random

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 20
PLATFORM_WIDTH, PLATFORM_HEIGHT = 100, 10
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
LIGHT_BLUE = (173, 216, 230)  # Light blue color for the level indicator
```

Let's break down the code step by step:

**Importing Libraries:**

* `import pygame`: Imports the Pygame library, which is used for developing games in Python.
    
* `import sys`: Imports the sys module, providing access to some variables used or maintained by the interpreter and functions that interact with the interpreter.
    

**Constants:**

* `WIDTH, HEIGHT = 800, 600`: Defines the dimensions of the game window.
    
* `BALL_RADIUS = 20`: Specifies the radius of the bouncing ball.
    
* `PLATFORM_WIDTH, PLATFORM_HEIGHT = 100, 10`: Sets the dimensions of the platform.
    
* `FPS = 60`: Defines the frames per second, controlling the speed of the game.
    
* Various color constants like `BLACK`, `WHITE`, `RED`, `YELLOW`, `ORANGE`, and `LIGHT_BLUE` represent RGB values for colors used in the game.
    

## How to Create a PyGame Instance

Now you're going to create the PyGame window and define some global variables that you'll use for every level of the game:

```python
# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Game")
font = pygame.font.Font(None, 36)

# Clock to control the frame rate
clock = pygame.time.Clock()

# Initialize variables for the game
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_speed = [random.uniform(2, 4), random.uniform(2, 4)]  # Faster starting speed
platform_pos = [WIDTH // 2 - PLATFORM_WIDTH // 2, HEIGHT - PLATFORM_HEIGHT - 10]
platform_speed = 10
score = 0
lives = 3
current_level = 1
platform_color = ORANGE  # Initialize platform color
```

**Pygame Initialization:**

* `pygame.init()`: Initializes the Pygame library.
    

**Create the Game Window:**

* `screen = pygame.display.set_mode((WIDTH, HEIGHT))`: Creates the game window with the specified dimensions.
    
* `pygame.display.set_caption("Bouncing Ball Game")`: Sets the title of the game window.
    
* `font = pygame.font.Font(None, 36)`: Initializes a font object for rendering text.
    

**Clock for Frame Rate Control:**

* `clock = pygame.time.Clock()`: Creates a clock object to control the frame rate.
    

**Game Variables Initialization:**

* `ball_pos = [WIDTH // 2, HEIGHT // 2]`: Initializes the starting position of the ball at the center of the screen.
    
* `ball_speed = [random.uniform(2, 4), random.uniform(2, 4)]`: Initializes the starting speed of the ball with random values.
    
* `platform_pos = [WIDTH // 2 - PLATFORM_WIDTH // 2, HEIGHT - PLATFORM_HEIGHT - 10]`: Initializes the starting position of the platform.
    
* `platform_speed = 10`: Sets the speed at which the platform moves.
    
* `score = 0`: Initializes the player's score.
    
* `lives = 3`: Initializes the number of lives the player has.
    
* `current_level = 1`: Initializes the current level of the game.
    
* `platform_color = ORANGE`: Initializes the color of the platform.
    

## How to Create the Game Screens

You will create at least three screens, one for start the game, one for winning the game, and one for losing the game. You can use the following code to do all that:

```python
# Functions for screens
def start_screen():
    screen.fill(BLACK)
    show_text_on_screen("Bouncing Ball Game", 50, HEIGHT // 4)
    show_text_on_screen("Press any key to start...", 30, HEIGHT // 3)
    show_text_on_screen("Move the platform with arrow keys...", 30, HEIGHT // 2)
    pygame.display.flip()
    wait_for_key()

def game_over_screen():
    screen.fill(BLACK)
    show_text_on_screen("Game Over", 50, HEIGHT // 3)
    show_text_on_screen(f"Your final score: {score}", 30, HEIGHT // 2)
    show_text_on_screen("Press any key to restart...", 20, HEIGHT * 2 // 3)
    pygame.display.flip()
    wait_for_key()

def victory_screen():
    screen.fill(BLACK)
    show_text_on_screen("Congratulations!", 50, HEIGHT // 3)
    show_text_on_screen(f"You've won with a score of {score}", 30, HEIGHT // 2)
    show_text_on_screen("Press any key to exit...", 20, HEIGHT * 2 // 3)
    pygame.display.flip()
    wait_for_key()

def wait_for_key():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

def show_text_on_screen(text, font_size, y_position):
    font = pygame.font.Font(None, font_size)
    text_render = font.render(text, True, WHITE)
    text_rect = text_render.get_rect(center=(WIDTH // 2, y_position))
    screen.blit(text_render, text_rect)

def change_platform_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
```

Let's go through the functions:

`start_screen()` Function:

* Clears the screen with a black background using `screen.fill(BLACK)`.
    
* Displays the game title and instructions using `show_text_on_screen`.
    
* Flips the display to make the changes visible with `pygame.display.flip()`.
    
* Calls `wait_for_key()` to wait for a key press before proceeding.
    

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-105.png align="left")

`game_over_screen()` Function:

* Clears the screen with a black background.
    
* Displays the game over message, the final score, and instructions for restarting.
    
* Flips the display.
    
* Calls `wait_for_key()` to wait for a key press.
    

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-106.png align="left")

`victory_screen()` Function:

* Clears the screen with a black background.
    
* Displays a congratulatory message, the final score, and instructions for exiting.
    
* Flips the display.
    
* Calls `wait_for_key()` to wait for a key press.
    

`wait_for_key()` Function:

* Waits for either a quit event (closing the game window) or a key press event.
    
* If the event is quitting, it exits the game using `pygame.quit()` and `sys.exit()`.
    
* If the event is a key press, it breaks out of the waiting loop.
    

`show_text_on_screen(text, font_size, y_position)` Function:

* Renders text on the screen with the specified font size and Y position.
    
* Uses the `pygame.font.Font` class to create a font object.
    
* Renders the text onto a surface with the specified color (white in this case).
    
* Positions the text in the center of the screen at the specified Y position.
    
* Blits (draws) the text onto the game screen.
    

`change_platform_color()` Function:

* Returns a random RGB color for changing the platform color.
    

These functions handle different aspects of the game screens, user interactions, and display of text. They contribute to the overall structure and user experience of the game.

## Main Game Loop

And now, you'll code the main loop of the game with it's applied mechanics. Let's check out the code first and then the explanation.

This is the longest block of code in this tutorial, so be patient – it's worth it.

```python
# Main game loop
start_screen()
game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    keys = pygame.key.get_pressed()

    # Move the platform
    platform_pos[0] += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * platform_speed
    platform_pos[1] += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * platform_speed

    # Ensure the platform stays within the screen boundaries
    platform_pos[0] = max(0, min(platform_pos[0], WIDTH - PLATFORM_WIDTH))
    platform_pos[1] = max(0, min(platform_pos[1], HEIGHT - PLATFORM_HEIGHT))

    # Move the ball
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Bounce off the walls
    if ball_pos[0] <= 0 or ball_pos[0] >= WIDTH:
        ball_speed[0] = -ball_speed[0]

    if ball_pos[1] <= 0:
        ball_speed[1] = -ball_speed[1]

    # Check if the ball hits the platform
    if (
        platform_pos[0] <= ball_pos[0] <= platform_pos[0] + PLATFORM_WIDTH
        and platform_pos[1] <= ball_pos[1] <= platform_pos[1] + PLATFORM_HEIGHT
    ):
        ball_speed[1] = -ball_speed[1]
        score += 1

    # Check if the player advances to the next level
    if score >= current_level * 10:
        current_level += 1
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_speed = [random.uniform(2, 4), random.uniform(2, 4)]  # Randomize the ball speed
        platform_color = change_platform_color()

    # Check if the ball falls off the screen
    if ball_pos[1] >= HEIGHT:
        # Decrease lives
        lives -= 1
        if lives == 0:
            game_over_screen()
            start_screen()  # Restart the game after game over
            score = 0
            lives = 3
            current_level = 1
        else:
            # Reset the ball position
            ball_pos = [WIDTH // 2, HEIGHT // 2]
            # Randomize the ball speed
            ball_speed = [random.uniform(2, 4), random.uniform(2, 4)]

    # Clear the screen
    screen.fill(BLACK)

    # Draw the ball
    pygame.draw.circle(screen, WHITE, (int(ball_pos[0]), int(ball_pos[1])), BALL_RADIUS)

    # Draw the platform
    pygame.draw.rect(screen, platform_color, (int(platform_pos[0]), int(platform_pos[1]), PLATFORM_WIDTH, PLATFORM_HEIGHT))

    # Display information
    info_line_y = 10  # Adjust the vertical position as needed
    info_spacing = 75  # Adjust the spacing as needed

    # Draw the score in an orange rectangle at the top left
    score_text = font.render(f"Score: {score}", True, WHITE)
    score_rect = score_text.get_rect(topleft=(10, info_line_y))
    pygame.draw.rect(screen, ORANGE, score_rect.inflate(10, 5))
    screen.blit(score_text, score_rect)

    # Draw the level indicator in a light-blue rectangle at the top left (next to the score)
    level_text = font.render(f"Level: {current_level}", True, WHITE)
    level_rect = level_text.get_rect(topleft=(score_rect.topright[0] + info_spacing, info_line_y))
    pygame.draw.rect(screen, LIGHT_BLUE, level_rect.inflate(10, 5))
    screen.blit(level_text, level_rect)

    # Draw the lives in a red rectangle at the top left (next to the level)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    lives_rect = lives_text.get_rect(topleft=(level_rect.topright[0] + info_spacing, info_line_y))
    pygame.draw.rect(screen, RED, lives_rect.inflate(10, 5))
    screen.blit(lives_text, lives_rect)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
```

Alright, that was a lot – but here's what we did in the above code:

**Initialization and Start Screen:**

* Calls `start_screen()` to display the initial screen with instructions.
    
* Sets `game_running` to `True` to initiate the main game loop.
    

**Main Game Loop:**

* Continues until `game_running` becomes `False` (for example, when the user closes the game window).
    

**Event Handling:**

* Checks for events using `pygame.event.get()`.
    
* If a quit event (closing the game window) is detected, sets `game_running` to `False` to exit the loop.
    

**Platform Movement:**

* Reads the state of the arrow keys using `pygame.key.get_pressed()`.
    
* Adjusts the platform position based on arrow key inputs.
    
* Ensures the platform stays within the screen boundaries.
    

**Ball Movement and Bouncing:**

* Updates the ball's position based on its speed.
    
* Implements bouncing off the walls by reversing the speed when reaching the screen edges.
    

**Collision Detection:**

* Checks if the ball hits the platform by comparing positions.
    
* If a collision occurs, the ball's vertical speed is reversed, and the player scores a point.
    

**Level Progression:**

* Checks if the player has scored enough points to advance to the next level.
    
* If so, increments the level, resets the ball's position, randomizes its speed, and changes the platform color.
    

**Checking for Game Over:**

* Monitors if the ball falls off the screen.
    
* Decreases the number of lives if the ball is below the screen.
    
* If lives run out, displays the game over screen, restarts the game, and resets score, lives, and level.
    

**Screen Rendering:**

* Clears the screen with a black background.
    
* Draws the ball and platform on the screen.
    
* Displays score, level, and lives information in rectangles with specific colors.
    

**Display Update and Frame Rate Control:**

* Updates the display to show the changes.
    
* Controls the frame rate with `clock.tick(FPS)`.
    

**Game Termination:**

* Exits PyGame and terminates the program when the main loop is exited.
    

This structure ensures continuous gameplay, handling user input, updating game state, and providing visual feedback to the player.

## Conclusion

In this tutorial, you've navigated through the intricacies of several key functions that form the backbone of your bouncing ball game.

Let's recap their roles:

The `start_screen()` function clears the screen with a black background, displays the game title and instructions, flips the display for visibility, and waits for a key press using `wait_for_key()`.

The `game_over_screen()` function clears the screen with a black background, displays the game over message, final score, and restart instructions, flips the display, and waits for a key press with `wait_for_key()`.

The `victory_screen()` function clears the screen with a black background, displays a congratulatory message, final score, and exit instructions, flips the display, and waits for a key press with `wait_for_key()`.

The `wait_for_key()` function waits for either a quit event (closing the game window) or a key press event. It exits the game if quitting, and breaks out of the waiting loop if a key is pressed.

The `show_text_on_screen(text, font_size, y_position)` function renders text on the screen with specified attributes, utilizes the `pygame.font.Font` class for creating a font object, and positions and draws the text in the center of the screen.

And the `change_platform_color()` function returns a random RGB color for changing the platform color.

Following these functions, you delved into the main game loop, the heart of our game. It orchestrates the game's mechanics, including event handling, platform and ball movement, collision detection, level progression, and game termination.

You witnessed how this loop ensures continuous gameplay, responsive user interactions, and dynamic visuals.

Now that you're equipped with the understanding of these functions and the main loop, you have the knowledge to experiment, tweak, and expand your game. Feel empowered to embark on your journey of game development, explore new features, and create unique gaming experiences. Happy coding!

If you want to download the code or play the game, you can find it here:

%[https://github.com/jpromanonet/bouncing_ball_game]
