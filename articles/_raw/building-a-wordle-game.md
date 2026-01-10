---
title: How to Build a Wordle Clone with Python
subtitle: ''
author: Tantoluwa Heritage Alabi NB
co_authors: []
series: null
date: '2022-05-12T21:24:00.000Z'
originalURL: https://freecodecamp.org/news/building-a-wordle-game
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/pexels-suzy-hazelwood-1822568.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'Solving puzzles is a way to relax and pass the time after a long day. It
  is also beneficial to the mind.

  And even better – there are correlations between puzzle-solving and increased problem-solving
  skills.

  Wordle is a new word puzzle game that chall...'
---

Solving puzzles is a way to relax and pass the time after a long day. It is also beneficial to the mind.

And even better – there are correlations between puzzle-solving and increased problem-solving skills.

[Wordle](https://wordlegame.org/) is a new word puzzle game that challenges its players to guess a five-letter word in six tries.

In this tutorial, you will build a Wordle-like guessing game with the same rules as the original game. We'll build the game in Python. Working through this challenge will improve your knowledge of functions and while loops, and it will help you become more familiar with the zip method.

## Prerequisites

* Basic knowledge of Python
    

## What We'll Cover:

* How the game works
    
* How to write the game logic
    
* Results of the game
    

## How the Game Works

The game will consist of:

* a variable that stores a five-letter word called "hidden\_word".
    
* input from a user.
    
* a variable that stores the number of times (up to 6 tries) the user tries to guess the word.
    
* a condition to check if a letter is guessed correctly and in the right position, indicated by "✔"
    
* another condition to check if a letter is guessed correctly but in the wrong position, indicated by "➕"
    
* the final condition to check if a letter is guessed but not in the hidden word, indicated by "❌"
    

## How to Write the Game Logic

### First Function Block

First, we need to inform players about the rules. This is necessary so people know how to play properly.

Start off by creating a function with the name "game\_instruction".

```python
def game_instruction():
```

Then, pass in the instructions as a string to the "print" function to show the result. Wrap the strings in docstrings (""" """) because the symbols ("✔❌❌✔➕") will be wrapped in double quotations (" ") . Also each instruction will appear on a new line without using the ("\\n") [tag](https://replit.com/@HeritageAlabi/triplequote#main.py).

```python
print("""Wordle is a single player game
A player has to guess a five letter hidden word
You have six attempts
Your Progress Guide "✔❌❌✔➕"
"✔" Indicates that the letter at that position was guessed correctly
"➕" indicates that the letter at that position is in the hidden word, but in a different position
"❌" indicates that the letter at that position is wrong, and isn't in the hidden word   """)
```

Each sentence is started on a new line, and it will appear that way on the console. We wrap up by calling our function so the instructions will be printed on the screen.

```python
game_instruction()
```

If you get an error, it could either be that you forget to put the colon (:) at the end of the function definition `def game_instruction()` or your code isn't formatted properly. Pay attention to the console error logged, as it will guide you.

### Bringing it together

```python
 def game_instruction():
     print("""Wordle is a single player game
A player has to guess a five letter hidden word
You have six attempts
Your Progress Guide "✔❌❌✔➕"
"✔" Indicates that the letter at that position was guessed correctly
"➕" indicates that the letter at that position is in the hidden word, but in a different position
"❌" indicates that the letter at that position is wrong, and isn't in the hidden word   """)
game_instruction()
```

And finally, if you run your code and there is no result on your console, it means that you probably forgot to call the function.

### Output

![Image](https://www.freecodecamp.org/news/content/images/2022/04/game_instruction.jpg align="left")

*Game instructions for players*

### Second Function Block

The next step is working with the user's entry and comparing it with the hidden word. The ability to do that is essential to the game.

Create a function called "check\_word". In the code block, create a variable named "hidden word" and assign it to any five letter word of your choice. This hidden word is what the user will try to guess correctly.

```python
def check_word():
  hidden_word = "snail"
```

Since the player has 6 tries, assign a new variable called "attempt" to the value of "6" and create a while statement.

It's best to use a while loop here because the process runs until the user guesses the right word or exhausts their tries. The condition for the while statement to run is if the number of attempts is greater than "0".

```python
def check_word():
  hidden_word = "snail"
  attempt = 6
  while attempt > 0:
```

The user's input is then created inside the while loop, and conditions are checked against the hidden word. If the user's entry is the same as the hidden word, the loop ends and the game is over.

```python
def check_word():
  hidden_word = "snail"
  attempt = 6
  while attempt > 0:
    guess = str(input("Guess the word: "))
    if guess == hidden_word:
      print("You guessed the words correctly! WIN 🕺🕺🕺 ")
      break
```

Format strings ( f" ") are another method of joining variables and strings together without using the "+" sign.

Here's an example:

```python
# Instead of,
print("you have" + attempt + " attempt(s) ,, \n") # '\n' is used for new line

# use this,
print(f"you have {attempt} attempt(s) ,, \n") # the variable to be printed is wrapped in curly braces
```

If the user's entry is not equal to the hidden word, introduce an else statement and all conditions will be checked in the "else" block. The attempt decreases by 1 and the attempts left are printed on the console as the user plays the game.

```python

def check_word():
  hidden_word = "snail"
  attempt = 6
  while attempt > 0:
    guess = str(input("Guess the word: "))
    if guess == hidden_word:
      print("You guessed the words correctly! WIN 🕺🕺🕺 ")
      break
    else:
      attempt = attempt - 1
      print(f"you have {attempt} attempt(s) ,, \n ")
```

If the user's input does not match the hidden word, there are three conditions to be checked:

* First, if the letter is in the wrong position but in the hidden word, print a "➕" beside the letter.
    
* Second, if the letter is in the right position and in the hidden word, print a "✔" beside the letter.
    
* Third, if the letter is not in the hidden word at all, print an "❌" beside the letter.
    

To compare the letters both in the user's input and the hidden word, include a for loop alongside a zip() function as a statement.

`for i, j in zip(food, drink):`

A zip() function is a built in function that loops through items like lists and tuples. It can extract values from multiple variables of the same size.

For strings, you can't directly use the zip() function alone. The "for" loop is included to get the letters from the variables that store the strings.

Here's an example:

A user enters a five letter word and a variable with a five letter word is created. Looping through the two variables at the same time with zip(), all the elements will be printed and separated by a hyphen.

Code block

```python
user_entry = input("spell 5 letter word: ")
default_value = "shell"
for i, j in zip(user_entry, default_value):
  print(i + " - " +  j)
```

Output

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-82.png align="left")

Back to our code:

```python
def check_word():
  hidden_word = "snail"
  attempt = 6
  while attempt > 0:
    guess = str(input("Guess the word: "))
    if guess == hidden_word:
      print("You guessed the words correctly! WIN 🕺🕺🕺 ")
      break
    else:
      attempt = attempt - 1
      print(f"you have {attempt} attempt(s) ,, \n ")
      for char, word in zip(hidden_word, guess):
            if word in hidden_word and word in char:
                print(word + " ✔ ")

            elif word in hidden_word:
                print(word + " ➕ ")
            else:
                print(" ❌ ")
```

Let's go through what's happening here:

`for char, word in zip(hidden_word, guess)` - this statement means looping through `hidden_word` with variable name `char` and looping through `guess` with variable name `word`. All the letters in the hidden word are accessed by `char` and all the letters in guess are accessed by `word`.

Then the three conditions mentioned earlier will be checked comparing both letters in `word` (the user's input) and `char` in (hidden word):

```python
def check_word():
  hidden_word = "snail"
  attempt = 6
  while attempt > 0:
    guess = str(input("Guess the word: "))
    if guess == hidden_word:
      print("You guessed the words correctly! WIN 🕺🕺🕺 ")
      break
    else:
      attempt = attempt - 1
      print(f"you have {attempt} attempt(s) ,, \n ")
      for char, word in zip(hidden_word, guess):
            if word in hidden_word and word in char:
                print(word + " ✔ ")

            elif word in hidden_word:
                print(word + " ➕ ")
            else:
                print(" ❌ ")
      if attempt == 0:
        print(" Game over !!!! ")
```

The final step is to call the function:

```python
def check_word():
  hidden_word = "snail"
  attempt = 6
  while attempt > 0:
    guess = str(input("Guess the word: "))
    if guess == hidden_word:
      print("You guessed the words correctly! WIN 🕺🕺🕺 ")
      break
    else:
      attempt = attempt - 1
      print(f"you have {attempt} attempt(s) ,, \n ")
      for char, word in zip(hidden_word, guess):
            if word in hidden_word and word in char:
                print(word + " ✔ ")

            elif word in hidden_word:
                print(word + " ➕ ")
            else:
                print(" ❌ ")
      if attempt == 0:
        print(" Game over !!!! ")

check_word()
```

Bringing all the code blocks together, it should look like this:

```python
def game_instruction():
    print("""Wordle is a single player game 
A player has to guess a five letter hidden word 
You have six attempts 
Your Progress Guide "✔❌❌✔➕"  
"✔" Indicates that the letter at that position was guessed correctly 
"➕" indicates that the letter at that position is in the hidden word, but in a different position 
"❌" indicates that the letter at that position is wrong, and isn't in the hidden word   """)


game_instruction()

def check_word():
  hidden_word = "snail"
  attempt = 6
  while attempt > 0:
    guess = str(input("Guess the word: "))
    if guess == hidden_word:
      print("You guessed the words correctly! WIN 🕺🕺🕺 ")
      break
    else:
      attempt = attempt - 1
      print(f"you have {attempt} attempt(s) ,, \n ")
      for char, word in zip(hidden_word, guess):
            if word in hidden_word and word in char:
                print(word + " ✔ ")

            elif word in hidden_word:
                print(word + " ➕ ")
            else:
                print(" ❌ ")
      if attempt == 0:
        print(" Game over !!!! ")

check_word()
```

**Output:**

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-42.png align="left")

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-44.png align="left")

## Conclusion

Great job! You are done creating a word puzzle game with Python. The code sample is found [here](https://replit.com/@HeritageAlabi/woordle-game#main.py), and you can reach out to me on [Twitter](https://twitter.com/HeritageAlabi1) if you have any questions. 💙
