---
title: 'Minimax Algorithm Guide: How to Create an Unbeatable AI'
subtitle: ''
author: Oluwatobi Sofela
co_authors: []
series: null
date: '2020-12-09T16:16:23.000Z'
originalURL: https://freecodecamp.org/news/minimax-algorithm-guide-how-to-create-an-unbeatable-ai
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fc9fb8be6787e0983939c87.jpg
tags:
- name: algorithms
  slug: algorithms
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Game Development
  slug: game-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
seo_title: null
seo_desc: "Recently I wondered – how can I program the computer to be unbeatable in\
  \ a tic-tac-toe game? \nWell, I thought I could easily get an answer to this question.\
  \ But as I went back and forth from articles to videos to a series of coding meditations,\
  \ I onl..."
---

Recently I wondered – how can I program the computer to be unbeatable in a tic-tac-toe game? 

Well, I thought I could easily get an answer to this question. But as I went back and forth from articles to videos to a series of coding meditations, I only succeeded in becoming more confused. 

However, my “Aha!” moment came when I took the time to understand how the **minimax algorithm** works.

If you are also on a similar path, let me take you through the steps to build an unbeatable AI (Artificial Intelligence).

## Step 1: Understand the basics of the minimax algorithm

A **minimax algorithm** is a [recursive](https://www.codesweetly.com/recursion/) program written to find the best gameplay that minimizes any tendency to lose a game while maximizing any opportunity to win the game.

Graphically, we can represent minimax as an exploration of a [game tree's](https://en.wikipedia.org/wiki/Game_tree) [nodes](https://en.wikipedia.org/wiki/Node_(computer_science)) to discover the best game move to make. In such a case, the tree's root is the game's current state — where the minimax algorithm got invoked.

![Tic-tac-toe game tree](https://www.freecodecamp.org/news/content/images/2020/12/game-tree-for-tic-tac-toe-minimax-codesweetly.png)
_Figure 1: The game tree of a concluding tic-tac-toe game_

Our focus in this guide is to use minimax to create an unbeatable AI for a tic-tac-toe game. However, [you can also use it for complex games](https://en.wikipedia.org/wiki/Minimax), like chess, and general decision-making to resolve any uncertainties.

In most cases, the player that initially invokes minimax is called the _maximizing player_. In other words, the original invocator of minimax is the player that wants to maximize any opportunity to win the game.

In contrast, the maximizing player’s opponent is called the _minimizing player_. As such, the minimizing player is the player whose chances of winning must be minimized.

In short, a minimax algorithm is a recursive function created to help a player (the maximizer) decide on the gameplay that _minimizes_ the _maximum_ possibility to lose a game.

## Step 2: Get familiar with this tutorial’s root node

To make this tutorial precise, the root node (the current state of the tic-tac-toe game) we will use will be a near-the-end state game board — as shown in figure 2 below. 

Also, the **X** mark will represent the AI’s mark, while the **O** mark will be the human player’s mark.

![The initial state of this tutorial's tic-tac-toe board](https://www.freecodecamp.org/news/content/images/2020/12/root-node-for-tic-tac-toe-minimax-tutorial-codesweetly.png)
_Figure 2: This tutorial’s root node_

In the current stage of the tic-tac-toe game (as shown in figure 2 above), it’s **X**’s turn to play (that is, the AI’s turn). And since there are three empty cells on the board, it implies that **X** has three possible play choices — top-middle, center, or bottom-right. 

But which is the best choice? Which move will best help **X** minimize the maximum possibility of losing the game?

![AI player's possible moves](https://www.freecodecamp.org/news/content/images/2020/12/ai-player-first-possible-moves-minimax-tic-tac-toe-codesweetly.png)
_Figure 3: AI player’s possible play choices_

To make the best decision, the AI needs to do the following:

1. Store the current state (values) of the tic-tac-toe board in an array. (For any empty cell, the cell’s index will get stored as its present content).
2. Get an array list of _only the empty cells’_ indexes.
3. Check and confirm if a specific player has won the game.
4. [Recursively](https://www.codesweetly.com/recursion/) invoke _minimax_ on each of the board’s empty cells.
5. Return a score for every possible move for both player **X** and player **O**.
6. Out of all the returned scores, choose the best one (the highest) that is guaranteed to minimize the human player’s possibilities of winning the game.

Therefore, in the following steps below, we will configure the AI to accomplish the list above. So, let’s get started by storing the board’s current state in an array.

## Step 3: Store the board’s current state in an array

Our next step is to store the current content of each of the board's cells in an array like so:

```js
const currentBoardState = ["X", 1, "O", "X", 4, "X", "O", "O", 8];
```

**Note:**

* The current state of our tic-tac-toe board is still as illustrated in figure 2.
* The values `1`, `4`, and `8` in the `currentBoardState` array are the board's empty cells' index numbers. In other words, instead of using empty strings, we chose to store the empty cells' current content as their respective indexes.

Importantly, before moving to the next step, let us explicitly define whose mark is `“X”` and who owns `“O”`.

```js
const aiMark = "X";
const humanMark = "O";
```

The two statements above denote that the AI’s mark is **X** while the human player’s mark is **O**.

## Step 4: Create a function to get the indexes of all the empty cells

The function below will filter the `currentBoardState` array — which will be passed-in as the function’s parameter’s argument. It will then return a new array containing all the `currentBoardState` array’s items that are neither `“X”` nor `“O”`.

```js
function getAllEmptyCellsIndexes(currBdSt) {
    return currBdSt.filter(i => i != "X" && i != "O");
}
```

**Note:** Remember that the `currentBoardState` array we created in step 3 contains only the values `“X”`, `“O”`, and _the board's empty cells' indexes_. Therefore, the `getAllEmptyCellsIndexes()` function above filters out any occurrence of an index in the `currentBoardState` array.

## Step 5: Create a winner determiner function

The primary purpose of the _winner determiner function_ below is to receive a `currentBoardState` array and a specific player’s mark (either mark `“X”` or `“O”`) as its parameters’ arguments. 

Then, it checks if the received mark forms a winning combination on the tic-tac-toe board. If so, the Boolean value `true` is returned — otherwise, `false` is returned.

```js
function checkIfWinnerFound(currBdSt, currMark) {
    if (
        (currBdSt[0] === currMark && currBdSt[1] === currMark && currBdSt[2] === currMark) ||
        (currBdSt[3] === currMark && currBdSt[4] === currMark && currBdSt[5] === currMark) ||
        (currBdSt[6] === currMark && currBdSt[7] === currMark && currBdSt[8] === currMark) ||
        (currBdSt[0] === currMark && currBdSt[3] === currMark && currBdSt[6] === currMark) ||
        (currBdSt[1] === currMark && currBdSt[4] === currMark && currBdSt[7] === currMark) ||
        (currBdSt[2] === currMark && currBdSt[5] === currMark && currBdSt[8] === currMark) ||
        (currBdSt[0] === currMark && currBdSt[4] === currMark && currBdSt[8] === currMark) ||
        (currBdSt[2] === currMark && currBdSt[4] === currMark && currBdSt[6] === currMark)
    ) {
        return true;
    } else {
        return false;
    }
}
```

## Step 6: Create the minimax algorithm

A **minimax algorithm** is just an ordinary function that contains statements to be executed once the function is invoked. Therefore, the process of creating the algorithm is the same as creating any other function. So, let’s create one now.

```js
function minimax(currBdSt, currMark) {
    
    // Space for the minimax’s statements 
    
}
```

That’s it! We’ve created a **minimax** function — albeit an empty one. Our next step is to fill up the function with statements that will be executed once the function is invoked — which we will do below.

**Note:** The minimax function created above is designed to accept _two arguments_.  
The first is _an array_ list of the current board’s content — that is, the present value of the `currentBoardState` array. While the second argument is _the mark_ of the player currently running the minimax algorithm — that is, mark `“X”` or mark `“O”`.

## Step 7: First minimax invocation

To avoid any confusion later in this tutorial, let’s invoke our minimax function for the first time — while passing-in the `currentBoardState` array and the `aiMark` as the function’s arguments.

```js
const bestPlayInfo = minimax(currentBoardState, aiMark);
```

## Step 8: Store the indexes of all empty cells

In this step, we will invoke the `getAllEmptyCellsIndexes` function that we created at step 4 — while passing-in the `currentBoardState` array as the function’s argument. 

Then, we will store the _returned_ array list of indexes inside a variable named `availCellsIndexes`.

```js
const availCellsIndexes = getAllEmptyCellsIndexes(currBdSt);
```

## Step 9: Check if there is a terminal state

At this stage, we need to verify if there is a terminal state (that is, a loss state, a win state, or a draw state) on the tic-tac-toe board. We will accomplish this verification by invoking the _winner determiner function_ (created in step 5) for each of the players.

If the function finds a win state for the human player (the minimizer), it will return `-1` (which signifies that the human player has won, and the AI has lost). But if it finds a win state for the AI player (the maximizer), it will return `+1` (which indicates that the AI has won, and the human player has lost).

However, suppose the winner determiner function cannot find any empty cell on the board or any win state for either player. In that case, it will return `0` (zero) — which signifies that the game has ended in a tie.

**Note:** The scores (`-1`, `+1`, and `0`) indicated above are [heuristic](https://www.vocabulary.com/dictionary/heuristic) values — which means that we will still get the same result if we prefer to use -25, +25, and 0.

Let’s now proceed to implement the terminal state verification by using an _if statement_ like so:

```js
if (checkIfWinnerFound(currBdSt, humanMark)) {
    return {score: -1};
} else if (checkIfWinnerFound(currBdSt, aiMark)) {
    return {score: 1};
} else if (availCellsIndexes.length === 0) {
    return {score: 0};
}
```

When there is a terminal state (lose, win, or draw), the active minimax function will return the appropriate terminal state score (`-1`, `+1`, or `0`) and end its invocation.

If the active minimax ends its invocation here, the algorithm will move on to step 12.

However, when there is _no_ terminal state, the active minimax function will execute the next statement (step 10, below).

## Step 10: Get ready to test the outcome of playing the current player’s mark on each empty cell

As step 9 found no terminal state, we have to devise a way to test what will happen if the current player (who is to make the next game move) plays on each empty cell.

In other words, if the current player plays on the first available cell, and the opponent plays on the second empty cell, will the current player win, lose, or draw the game? Or will there still be no terminal state found?

Alternatively, what will happen if the current player plays on the second available cell, and the opponent plays on the first empty cell?

Or perhaps, will the third available cell be the best spot for the current player to play?

This test drive is what we need to do now. But before we begin, we need a place to record each test's outcome — so let’s do that first by creating an array named `allTestPlayInfos`.

```js
const allTestPlayInfos = [];
```

So, now that we have secured a place to store each test drive’s result, let’s begin the trials by creating a _for-loop statement_ that will loop through each of the empty cells starting from the first one.

```js
for (let i = 0; i < availCellsIndexes.length; i++) {
    
    // Space for the for-loop’s codes
    
}
```

In the next two steps, we will fill up the for-loop with the code it should run for each empty cell.

## Step 11: Test-play the current player’s mark on the empty cell the for-loop is currently processing

Before doing anything in this step, let’s review the current state of our board.

![Current tic-tac-toe board](https://www.freecodecamp.org/news/content/images/2020/12/current-tic-tac-toe-minimax-board-codesweetly.png)
_Figure 4: The current state of the tic-tac-toe board_

Notice that the above board is still the same as that of figure 2, except that we’ve highlighted — in red — the cell the for-loop is currently processing.

Next, it will be helpful to have a place to store this test-play’s terminal score — so let’s create an object like so:

```js
const currentTestPlayInfo = {};
```

Also, before test-playing the current player’s mark on the red cell, let’s save the cell’s index number — so that it will be easy to reset the cell’s info after this test-play.

```js
currentTestPlayInfo.index = currBdSt[availCellsIndexes[i]];
```

Let’s now place the current player’s mark on the red cell (that is, the cell currently being processed by the for-loop).

```js
currBdSt[availCellsIndexes[i]] = currMark;
```

Based on the current player’s gameplay, the board’s state will change to reflect its latest move.

![New tic-tac-toe board](https://www.freecodecamp.org/news/content/images/2020/12/ai-latest-move-tic-tac-toe-minimax-board-codesweetly.png)
_Figure 5: The new board — which reflects the current player’s latest move_

Therefore, since the board’s state has changed, we need to recursively run minimax on the new board — while passing in the new board's state and the next player's mark.

```js
if (currMark === aiMark) {
    const result = minimax(currBdSt, humanMark);
    currentTestPlayInfo.score = result.score;
} else {
    const result = minimax(currBdSt, aiMark);
    currentTestPlayInfo.score = result.score;
}
```

**Note:**

* The recursive invocation of minimax at this very point will be the _____ time we are invoking the function. The first invocation happened in step 7.
* This recursive invocation will cause the reiteration of steps 8 to 11.
* Suppose there is a terminal state at step 9. In that case, the current minimax invocation will stop running — and store the returned terminal object (for example, `{score: 1}`) in the `result` variable.
* Once there is a terminal state, step 12 will be the next step.
* If there exists _no_ terminal state, a **second for-loop** will begin for the new board at step 10.
* If step 10 is repeated, please replace figure 4’s board with the new board in figure 5. However, the cell highlighted in red will now be the cell the for-loop is currently processing. So please, do reflect the changes accordingly.

## Step 12: Save the latest terminal score

After the just concluded minimax invocation has returned its terminal state's value, the active for-loop will save the `result` variable's score into the `currentTestPlayInfo` object like so:

```js
currentTestPlayInfo.score = result.score;
```

Then, since the returned score officially ends the current test-play, it is best to reset the current board back to the state before the current player made its move.

```js
currBdSt[availCellsIndexes[i]] = currentTestPlayInfo.index;
```

Also, we need to save the result of the current player’s test-play for future use. So, let’s do that by pushing the `currentTestPlayInfo` object to the `allTestPlayInfos` array like so:

```js
allTestPlayInfos.push(currentTestPlayInfo);
```

**Note:**

* If you got to this step from step 17, kindly continue this tutorial at _step 18_. Otherwise, consider the next point.
* If the active for-loop has finished looping through all the current board's empty cells, the loop will end at this point, and _step 14_ will be next. Otherwise, the loop will proceed to process the next available cell (step 13).

## Step 13: Run the active for-loop on the next empty cell

Remember that the currently active for-loop (that began at step 10) has only finished its work for the preceding empty cell(s). Therefore, the loop will proceed to test-play the current player’s mark on the next free cell. 

In other words, the currently running minimax function will repeat steps **11** and **12**. But, essentially, take note of the following:

* The red cell highlighted in figure 4 will change to the cell the for-loop is currently processing.
* Please, be mindful that figure 5 will also change. In other words, the current player’s move will now be on the cell the for-loop is currently processing.
* After the active for-loop has completed its work, the `allTestPlayInfos` array will contain specific objects for each empty cell the for-loop has processed.
* Each of the objects in the `allTestPlayInfos` array will contain an `index` property and a `score` property (take for example: `{index: 8, score: -1}`).
* If you got to this step from step 20, then, _on completing step 12_, kindly continue this tutorial at _step 18_.

## Step 14: Plan how to get the object with the best test-play score for the current player

Immediately after the for-loop has completed its work of looping through all the empty cells of the current board, minimax will:

1. **Create a space** to store the reference number that will later help to get the best test-play object.
2. **Get the reference number** to the current player’s best test-play.
3. **Use the acquired reference number** to get the object with the best test-play for the current player.

Without any further ado, let’s implement this plan in the next few steps.

## Step 15: Create a store for the best test-play’s reference

The variable below is the place we will later store the reference to the best test-play object. (Note that the value `null` indicates that we have deliberately left the variable empty).

```js
let bestTestPlay = null;
```

## Step 16: Get the reference to the current player’s best test-play

Now that there is a `bestTestPlay` store, the active minimax function can proceed to get the reference to the current player’s best test-play like so:

```js
if (currMark === aiMark) {
    let bestScore = -Infinity;
    for (let i = 0; i < allTestPlayInfos.length; i++) {
        if (allTestPlayInfos[i].score > bestScore) {
            bestScore = allTestPlayInfos[i].score;
            bestTestPlay = i;
        }
    }
} else {
    let bestScore = Infinity;
    for (let i = 0; i < allTestPlayInfos.length; i++) {
        if (allTestPlayInfos[i].score < bestScore) {
            bestScore = allTestPlayInfos[i].score;
            bestTestPlay = i;
        }
    }
}
```

The code above means if the current mark is equal to the AI player’s mark:

1. Create a `bestScore` variable with the value of `-Infinity`. (Note that this value is just a placeholder value that needs to be _less than_ all the scores in the `allTestPlayInfos` array. Therefore, using `-700` will do the same job).
2. Then, for every test-play object in the `allTestPlayInfos` array, check if the test-play the loop is currently processing has a _higher_ score than the current `bestScore`. If so, record that test-play’s details inside both the `bestScore` variable and the `bestTestPlay` variable.

Otherwise, if the current mark is the human player’s mark:

1. Create a `bestScore` variable with the value of `+Infinity`. (Again, note that we will get the same outcome if we had preferred to use `+300`. It is just a placeholder value that needs to be _greater than_ all the scores in the `allTestPlayInfos` array).
2. Then, for every test-play object in the `allTestPlayInfos` array, check if the test-play the loop is currently processing has a _lesser_ score than the current `bestScore`. If so, record that test-play’s details inside both the `bestScore` variable and the `bestTestPlay` variable.

## Step 17: Get the object with the best test-play score for the current player

Finally, the currently running minimax invocation can now finish its work by returning the object with the best test-play for the current player like so:

```js
return allTestPlayInfos[bestTestPlay];
```

Note that minimax will store the returned object inside the `result` variable of the first for-loop that began at step 11. It will then repeat step 12. Please revisit step 12 only. Then, continue this tutorial below.

## Step 18: Let’s do a review

This stage is an excellent time to review what we've done thus far pictorially.

**Note:**

* If this is your first time on this step, please use the diagram in _step 19_.
* Is this your second time on this step? If so, the diagram in _step 21_ is yours.
* Are you here for the third time? Well-done! Check out the diagram in _step 23_.

## Step 19: Tracing our steps with a diagram

The diagram below shows the AI and the human player's _first test-play_ for the first for-loop invocation initiated by the AI player.

![First tic-tac-toe test-play](https://www.freecodecamp.org/news/content/images/2020/12/tic-tac-toe-minimax-first-test-play-codesweetly-1.png)
_Figure 6: First test-play which predicts a loss state for the AI (maximizer)_

## Step 20: The first for-loop moves forward to process the next empty cell

On concluding that playing on the first empty cell will end in a loss state, the AI forges ahead to test the outcome of playing on the _second free cell_ by repeating step 13.

## Step 21: Tracing our steps with a diagram

The diagram below shows the AI and the human player's _second test-play_ for the first for-loop invocation initiated by the AI player.

![Second tic-tac-toe test-play](https://www.freecodecamp.org/news/content/images/2020/12/tic-tac-toe-minimax-second-test-play-codesweetly-1.png)
_Figure 7: Second test-play which predicts a win state for the AI (maximizer)_

## Step 22: The first for-loop moves forward to process the next empty cell

Now that the AI has confirmed that playing on the second empty cell will result in a win state, it further checks the outcome of playing on the _third free cell_ by repeating step 13.

## Step 23: Tracing our steps with a diagram

The diagram below shows the AI and the human player's _third test-play_ for the first for-loop invocation initiated by the AI player.

![Third tic-tac-toe test-play](https://www.freecodecamp.org/news/content/images/2020/12/tic-tac-toe-minimax-third-test-play-codesweetly-1.png)
_Figure 8: Third test-play which predicts a loss state for the AI (maximizer)_

## Step 24: Get the object with the best test-play score for the AI player

At this point (after the third test-play), the first for-loop would have processed all the three empty cells of the first board (passed-in to minimax at step 7). 

Therefore, minimax will forge ahead to get the object with the best test-play for the AI player — by repeating steps 15 to 17. However, _when at step 17_, kindly note the following:

* The returned object will now get stored in the `bestPlayInfo` variable that we created at step 7.
* Minimax will not repeat step 12 because the for-loop statement is no longer active.

![Overview of all tic-tac-toe test-plays and scores](https://www.freecodecamp.org/news/content/images/2020/12/tic-tac-toe-minimax-view-of-all-test-plays-codesweetly-1.png)
_Figure 9: Overview of all test-plays and scores_

## Step 25: Use the data inside bestPlayInfo

Considering this tutorial’s board (a near-the-end state game board — as shown in figure 2 of step 2), the object in the `bestPlayInfo` variable will be `{index: 4, score: 1}`. Therefore, the AI can now use its index value to choose the best cell to play on.

### Example

```js
// Get all the board’s cells:
const gameCells = document.querySelectorAll(".cell");

// Below is the variable we created at step 3:
const aiMark = "X";

// Here is the bestPlayInfo we created at step 7 to contain the best test-play object for the AI player:
const bestPlayInfo = minimax(currentBoardState, aiMark);

// Play the AI’s mark on the cell that is best for it:
gameCells[bestPlayInfo.index].innerText = aiMark;
```

Therefore, the AI player will win the game, and the new board will now look like so:

![AI's winning move](https://www.freecodecamp.org/news/content/images/2020/12/ai-winning-move-tic-tac-toe-minimax-board-codesweetly.png)
_Figure 10: Final gameboard showing that the AI (player X) has won the game_

## Step 26: A bird’s-eye view of this tutorial’s algorithm

Below is this tutorial’s minimax algorithm in one piece. Feel free to insert it into your editor. Play around with it for various game scenarios, and use the console to test, test, and test it again until you are comfortable building an unbeatable AI. 

And remember, programming is better only when you [code sweetly](https://www.codesweetly.com/) — so have lots of fun with it!

```js
// Step 3 - Store the board’s current state in an array and define each mark's owner:
const currentBoardState = ["X", 1, "O", "X", 4, "X", "O", "O", 8];
const aiMark = "X";
const humanMark = "O";

// Step 4 - Create a function to get the indexes of all the empty cells:
function getAllEmptyCellsIndexes(currBdSt) {
    return currBdSt.filter(i => i != "O" && i != "X");
}

// Step 5 - Create a winner determiner function:
function checkIfWinnerFound(currBdSt, currMark) {
    if (
        (currBdSt[0] === currMark && currBdSt[1] === currMark && currBdSt[2] === currMark) ||
        (currBdSt[3] === currMark && currBdSt[4] === currMark && currBdSt[5] === currMark) ||
        (currBdSt[6] === currMark && currBdSt[7] === currMark && currBdSt[8] === currMark) ||
        (currBdSt[0] === currMark && currBdSt[3] === currMark && currBdSt[6] === currMark) ||
        (currBdSt[1] === currMark && currBdSt[4] === currMark && currBdSt[7] === currMark) ||
        (currBdSt[2] === currMark && currBdSt[5] === currMark && currBdSt[8] === currMark) ||
        (currBdSt[0] === currMark && currBdSt[4] === currMark && currBdSt[8] === currMark) ||
        (currBdSt[2] === currMark && currBdSt[4] === currMark && currBdSt[6] === currMark)
) {
        return true;
    } else {
        return false;
    }
}

// Step 6 - Create the minimax algorithm:
function minimax(currBdSt, currMark) {
    // Step 8 - Store the indexes of all empty cells:
    const availCellsIndexes = getAllEmptyCellsIndexes(currBdSt);
    
    // Step 9 - Check if there is a terminal state:
    if (checkIfWinnerFound(currBdSt, humanMark)) {
        return {score: -1};
    } else if (checkIfWinnerFound(currBdSt, aiMark)) {
        return {score: 1};
    } else if (availCellsIndexes.length === 0) {
        return {score: 0};
    }
    
    // Step 10 - Create a place to record the outcome of each test drive:
    const allTestPlayInfos = [];
    
    // Step 10 - Create a for-loop statement that will loop through each of the empty cells:
    for (let i = 0; i < availCellsIndexes.length; i++) {
        // Step 11 - Create a place to store this test-play’s terminal score:
        const currentTestPlayInfo = {};
        
        // Step 11 - Save the index number of the cell this for-loop is currently processing:
        currentTestPlayInfo.index = currBdSt[availCellsIndexes[i]];
        
        // Step 11 - Place the current player’s mark on the cell for-loop is currently processing:
        currBdSt[availCellsIndexes[i]] = currMark;
        
        if (currMark === aiMark) {
            // Step 11 - Recursively run the minimax function for the new board:
            const result = minimax(currBdSt, humanMark);
            
            // Step 12 - Save the result variable’s score into the currentTestPlayInfo object:
            currentTestPlayInfo.score = result.score;
        } else {
            // Step 11 - Recursively run the minimax function for the new board:
            const result = minimax(currBdSt, aiMark);
            
            // Step 12 - Save the result variable’s score into the currentTestPlayInfo object:
            currentTestPlayInfo.score = result.score;
        }
        
        // Step 12 - Reset the current board back to the state it was before the current player made its move:
        currBdSt[availCellsIndexes[i]] = currentTestPlayInfo.index;
        
        // Step 12 - Save the result of the current player’s test-play for future use:
        allTestPlayInfos.push(currentTestPlayInfo);
    }
    
    // Step 15 - Create a store for the best test-play’s reference:
    let bestTestPlay = null;
    
    // Step 16 - Get the reference to the current player’s best test-play:
    if (currMark === aiMark) {
        let bestScore = -Infinity;
        for (let i = 0; i < allTestPlayInfos.length; i++) {
            if (allTestPlayInfos[i].score > bestScore) {
                bestScore = allTestPlayInfos[i].score;
                bestTestPlay = i;
            }
        }
    } else {
        let bestScore = Infinity;
        for (let i = 0; i < allTestPlayInfos.length; i++) {
            if (allTestPlayInfos[i].score < bestScore) {
                bestScore = allTestPlayInfos[i].score;
                bestTestPlay = i;
            }
        }
    }
    
    // Step 17 - Get the object with the best test-play score for the current player:
    return allTestPlayInfos[bestTestPlay];
} 

// Step 7 - First minimax invocation:
const bestPlayInfo = minimax(currentBoardState, aiMark);
```

## Useful resource

* [Recursion: What You Need to Know about Recursion](https://www.codesweetly.com/recursion/)

