---
title: How I came back to an old problem and finally wrote a Sudoku-solving algorithm
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-27T13:45:12.000Z'
originalURL: https://freecodecamp.org/news/coming-back-to-old-problems-how-i-finally-wrote-a-sudoku-solving-algorithm-3b371e6c63bd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ERYVo0W3nlPCEQGOHul6Rw.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: sudoku
  slug: sudoku
seo_title: null
seo_desc: 'By Ali Spittel

  This article will be part technical, part personal story, and part cultural critique.
  If you are just here for the code and explanation, jump to the The Initial Approach
  header!

  This story starts a few years ago in a college computer s...'
---

By Ali Spittel

This article will be part technical, part personal story, and part cultural critique. If you are just here for the code and explanation, jump to the **The Initial Approach** header!

This story starts a few years ago in a college computer science classroom. I had an untraditional path to writing code — I randomly enrolled in a computer science class during my sophomore year of college, because I had an extra credit hour and I was curious what it was about. I thought we would learn how to use Microsoft Word and Excel — I genuinely had no idea what code was.

My high school definitely did not have any coding classes, they barely had functioning computers! I didn’t play video games or engage in activities that traditionally lead to kids learning how to code, either. So coding was brand new to me when I took that Python class in college.

As soon as I walked into the classroom, they had us type Python code into Idle, a text editor that comes with the Python language. They had printed the code and just had us type it in and run it — I was immediately hooked. Over the course of that class, I built a Tic Tac Toe script with a GUI to input pieces and a Flappy Bird clone. It honestly came pretty easily to me, and I had a ton of fun. I quickly decided to minor in computer science, and I just wanted to write more code.

The next semester, I enrolled in a Data Structures and Algorithms course which was next in the computer science sequence. The class was taught in C++, which, unbeknownst to me, was supposed to be learned over the summer before the class. It quickly became obvious that the professors were trying to use the class to filter out students — around 50% of the enrollees on day one made it through the semester. We even changed classrooms from a lecture hall to a break out room. My pride was the only thing keeping me in the class. I felt completely lost in pretty much every lesson. I spent many all-nighters working on projects and studying for the exams.

One problem in particular really got me — we were supposed to build a program in C++ that would solve any Sudoku problem. Again, I spent countless hours on the assignment trying to get the code working. By the time the project was due, my solution worked for some of the test cases but not all of them. I ended up getting a C+ on my assignment — one of my worst grades in all of college.

After that semester, I abandoned my idea of minoring in computer science, completely quit coding, and stuck to what I thought I was good at — writing and politics.

Of course, funny things happen in life and I obviously started coding again, but it took me a long time to feel like I was a competent programmer.

All that being said, a few years later into my programming journey, I decided to retry implementing the Sudoku solving algorithm to prove to myself that I could implement it now. The code isn’t perfect, but it will solve pretty much any Sudoku puzzle. Let’s walk through the algorithm and then the implementation.

### Sudoku Puzzles

![Image](https://cdn-media-1.freecodecamp.org/images/NGyo6kOiNfPdOzeV5RfN8K4SUw0Jxw0LOraz)

In case you haven’t played Sudoku puzzles before, they are number puzzles in which each row, column, and 3x3 square in the puzzle must have the numbers 1–9 represented exactly once. There are lots of approaches to solving these puzzles, many of which can be replicated by a computer instead of a person. Usually, when we solve them using a computer, we will use nested arrays to represent the Sudoku board like so:

```
puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],          [6, 0, 0, 1, 9, 5, 0, 0, 0],          [0, 9, 8, 0, 0, 0, 0, 6, 0],          [8, 0, 0, 0, 6, 0, 0, 0, 3],          [4, 0, 0, 8, 0, 3, 0, 0, 1],          [7, 0, 0, 0, 2, 0, 0, 0, 6],          [0, 6, 0, 0, 0, 0, 2, 8, 0],          [0, 0, 0, 4, 1, 9, 0, 0, 5],          [0, 0, 0, 0, 8, 0, 0, 7, 9]]
```

When solved, the zeros will be filled in with actual numbers:

```
solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],            [6, 7, 2, 1, 9, 5, 3, 4, 8],            [1, 9, 8, 3, 4, 2, 5, 6, 7],            [8, 5, 9, 7, 6, 1, 4, 2, 3],            [4, 2, 6, 8, 5, 3, 7, 9, 1],            [7, 1, 3, 9, 2, 4, 8, 5, 6],            [9, 6, 1, 5, 3, 7, 2, 8, 4],            [2, 8, 7, 4, 1, 9, 6, 3, 5],            [3, 4, 5, 2, 8, 6, 1, 7, 9]]
```

### The Initial Approach

Because I didn’t feel like writing a full test suite with different puzzles, I used the challenges on [CodeWars](https://www.codewars.com/) to test myself. The first problem I tried was [this](https://www.codewars.com/kata/sudoku-solver) — where all of the puzzles were “easy” Sudokus that could be solved without a more complex algorithm.

I decided to try and solve the Sudokus in the way I personally do — where I would find the possible numbers for a space, keep track of them, and if there is only one possible number, plug it into that spot. Since these were easier Sudokus, this approach worked fine for this Kata, and I passed.

Here’s my (uncleaned) code!

```
class SudokuSolver:    def __init__(self, puzzle):        self.puzzle = puzzle        self.box_size = 3
```

```
    def find_possibilities(self, row_number, column_number):        possibilities = set(range(1, 10))        row = self.get_row(row_number)        column = self.get_column(column_number)        box = self.get_box(row_number, column_number)        for item in row + column + box:            if not isinstance(item, list)and item in possibilities:                possibilities.remove(item)        return possibilities
```

```
    def get_row(self, row_number):        return self.puzzle[row_number]
```

```
    def get_column(self, column_number):        return [row[column_number] for row in self.puzzle]
```

```
    def get_box(self, row_number, column_number):        start_y = column_number // 3 * 3        start_x = row_number // 3 * 3        if start_x < 0:            start_x = 0        if start_y < 0:            start_y = 0        box = []        for i in range(start_x, self.box_size + start_x):            box.extend(self.puzzle[i][start_y:start_y+self.box_size])        return box
```

```
    def find_spot(self):        unsolved = True        while unsolved:            unsolved = False            for row_number, row in enumerate(self.puzzle):                for column_number, item in enumerate(row):                    if item == 0:                        unsolved = True                        possibilities = self.find_possibilities(                            row_number, column_number)                        if len(possibilities) == 1:                            self.puzzle[row_number][column_number] = list(possibilities)[                                0]        return self.puzzle
```

```
def sudoku(puzzle):    sudoku = SudokuSolver(puzzle)    return sudoku.find_spot()
```

Of course, I also wanted to solve more difficult Sudoku puzzles, so I decided to implement a more complex algorithm in order to solve those puzzles.

### The Algorithm

One algorithm to solve Sudoku puzzles is the backtracking algorithm. Essentially, you keep trying numbers in empty spots until there aren’t any that are possible, then you backtrack and try different numbers in the previous slots.

![Image](https://cdn-media-1.freecodecamp.org/images/XHVFcJhCX-mRMxvSBvuWMQuEw1eipOCxKWBS)
_Shoutout to Wikipedia for the awesome visualization!_

The first thing that I did was continue my “easy” Sudoku solver’s approach of finding the possible values for each square based on which values were already in that square’s row, column, and box. I stored all of these values in a list so that I could quickly refer to them while backtracking or finding which value to use in that square.

Next, I needed to implement the forward moving and backtracking of putting items in each space. I put markers on each non-given space (so the ones that were zeros when the game started) so that those spaces would be included in the backtracking and given spots wouldn’t be. I then iterated through those un-solved spots. I would put the first item of the possible value list in that spot and then move to the next unsolved spot. I would then put the first possible value of that spot in its place. If it conflicted with the value of the previous slot, I would then move to the second item in the list of possible values and then move to the next slot.

That process would continue until there was no possible move for a given spot — that is, the end of the possible value list was reached and none of the values worked in that row, column, or box. Then, the backtracking algorithm kicked in.

Within the backtracking implementation, the code would move back to the last spot that was filled in and move to the next possible value and then start moving forward again. If the last of the possible values was reached at that spot as well, the backtracking algorithm would keep moving backwards until there was a spot that could be incremented.

Once the end of the puzzle was reached with correct values in each square, the puzzle was solved!

### My Approach

I like object oriented approaches, so I have two different classes in my solution: one for the cell and one for the Sudoku board. My very imperfect code looks like this:

```
class Cell:    """One individual cell on the Sudoku board"""
```

```
    def __init__(self, column_number, row_number, number, game):        # Whether or not to include the cell in the backtracking        self.solved = True if number > 0 else False        self.number = number  # the current value of the cell        # Which numbers the cell could potentially be        self.possibilities = set(range(1, 10)) if not self.solved else []        self.row = row_number  # the index of the row the cell is in        self.column = column_number  # the index of the column the cell is in        self.current_index = 0  # the index of the current possibility        self.game = game  # the sudoku game the cell belongs to        if not self.solved:  # runs the possibility checker            self.find_possibilities()
```

```
    def check_area(self, area):        """Checks to see if the cell's current value is a valid sudoku move"""        values = [item for item in area if item != 0]        return len(values) == len(set(values))
```

```
    def set_number(self):        """changes the number attribute and also changes the cell's value in the larger puzzle"""        if not self.solved:            self.number = self.possibilities[self.current_index]            self.game.puzzle[self.row][self.column] = self.possibilities[self.current_index]
```

```
    def handle_one_possibility(self):        """If the cell only has one possibility, set the cell to that value and mark it as solved"""        if len(self.possibilities) == 1:            self.solved = True            self.set_number()
```

```
    def find_possibilities(self):        """filter the possible values for the cell"""        for item in self.game.get_row(self.row) + self.game.get_column(self.column) + self.game.get_box(self.row, self.column):            if not isinstance(item, list) and item in self.possibilities:                self.possibilities.remove(item)        self.possibilities = list(self.possibilities)        self.handle_one_possibility()
```

```
    def is_valid(self):        """checks to see if the current number is valid in its row, column, and box"""        for unit in [self.game.get_row(self.row), self.game.get_column(self.column), self.game.get_box(self.row, self.column)]:            if not self.check_area(unit):                return False        return True
```

```
    def increment_value(self):        """move number to the next possibility while the current number is invalid and there are possibilities left"""        while not self.is_valid() and self.current_index < len(self.possibilities) - 1:            self.current_index += 1            self.set_number()
```

```
class SudokuSolver:    """contains logic for solving a sudoku puzzle -- even very difficult ones using a backtracking algorithm"""
```

```
    def __init__(self, puzzle):        self.puzzle = puzzle  # the 2d list of spots on the board        self.solve_puzzle = []  # 1d list of the Cell objects        # the size of the boxes within the puzzle -- 3 for a typical puzzle        self.box_size = int(len(self.puzzle) ** .5)        self.backtrack_coord = 0  # what index the backtracking is currently at
```

```
    def get_row(self, row_number):        """Get the full row from the puzzle based on the row index"""        return self.puzzle[row_number]
```

```
    def get_column(self, column_number):        """Get the full column"""        return [row[column_number] for row in self.puzzle]
```

```
    def find_box_start(self, coordinate):        """Get the start coordinate for the small sudoku box"""        return coordinate // self.box_size * self.box_size
```

```
    def get_box_coordinates(self, row_number, column_number):        """Get the numbers of the small sudoku box"""        return self.find_box_start(column_number), self.find_box_start(row_number)
```

```
    def get_box(self, row_number, column_number):        """Get the small sudoku box for an x and y coordinate"""        start_y, start_x = self.get_box_coordinates(row_number, column_number)        box = []        for i in range(start_x, self.box_size + start_x):            box.extend(self.puzzle[i][start_y:start_y+self.box_size])        return box
```

```
    def initialize_board(self):        """create the Cells for each item in the puzzle and get its possibilities"""        for row_number, row in enumerate(self.puzzle):            for column_number, item in enumerate(row):                self.solve_puzzle.append(                    Cell(column_number, row_number, item, self))
```

```
    def move_forward(self):        """Move forwards to the next cell"""        while self.backtrack_coord < len(self.solve_puzzle) - 1 and self.solve_puzzle[self.backtrack_coord].solved:            self.backtrack_coord += 1
```

```
    def backtrack(self):        """Move forwards to the next cell"""        self.backtrack_coord -= 1        while self.solve_puzzle[self.backtrack_coord].solved:            self.backtrack_coord -= 1
```

```
    def set_cell(self):        """Set the current cell to work on"""        cell = self.solve_puzzle[self.backtrack_coord]        cell.set_number()        return cell
```

```
    def reset_cell(self, cell):        """set a cell back to zero"""        cell.current_index = 0        cell.number = 0        self.puzzle[cell.row][cell.column] = 0
```

```
    def decrement_cell(self, cell):        """runs the backtracking algorithm"""        while cell.current_index == len(cell.possibilities) - 1:            self.reset_cell(cell)            self.backtrack()            cell = self.solve_puzzle[self.backtrack_coord]        cell.current_index += 1
```

```
    def change_cells(self, cell):        """move forwards or backwards based on the validity of a cell"""        if cell.is_valid():            self.backtrack_coord += 1        else:            self.decrement_cell(cell)
```

```
    def solve(self):        """run the other functions necessary for solving the sudoku puzzle"""        self.move_forward()        cell = self.set_cell()        cell.increment_value()        self.change_cells(cell)
```

```
    def run_solve(self):        """runs the solver until we are at the end of the puzzle"""        while self.backtrack_coord <= len(self.solve_puzzle) - 1:            self.solve()
```

```
def solve(puzzle):    solver = SudokuSolver(puzzle)    solver.initialize_board()    solver.run_solve()    return solver.puzzle
```

[Hard Sudoku Solver](https://www.codewars.com/kata/hard-sudoku-solver)

### My Takeaways

Sometimes it just takes time and practice. The Sudoku solver I spent countless college hours on took me less than an hour a few years later.

I will say that computer science programs don’t tend to start in a way that allows people who didn’t write code earlier in life to participate. In a few years, computer science education policies may change. But for now, this eliminates people who grew up in small towns, who weren’t interested in coding growing up, or who went to weaker high schools.

In part, this definitely contributes to the success of coding bootcamps which start with the fundamentals and teach the less conceptual web development skills rather than heavy algorithms.

I can now write the Sudoku solving algorithm, but I don’t think it’s a necessary skill for developers to have — I still became a successful software engineer shortly after that time when I couldn’t implement the Sudoku solver.

I do think that some computer science fundamentals can be very helpful, even for new developers. For example, the concepts behind Big-O notation can be really helpful for deciding between approaches. That being said, most data structures and algorithms aren’t used on a day to day basis, so why are they the basis for interviews and computer science classes instead of the more important things used every day?

I’m happy to see my own personal growth in coding; however, I can’t wait for a day when developers aren’t jumping through imaginary hoops to prove themselves, and when learning environments are much more constructive.

_If you liked this article, please [subscribe](https://tinyletter.com/ali_writes_code) to my weekly newsletter where you’ll receive my favorite links from the week and my latest articles._

