---
title: Learn How to Build Tic-Tac-Toe with React Hooks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-29T13:49:57.000Z'
originalURL: https://freecodecamp.org/news/learn-how-to-build-tic-tac-toe-with-react-hooks
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-26-at-21.27.58.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: React
  slug: reactjs
- name: Scrimba
  slug: scrimba
seo_title: null
seo_desc: 'By Per Harald Borgen

  If you have a good understanding of HTML, CSS, JavaScript, and React you might be
  wondering where to go next on your learning journey. So why not check out Scrimba''s
  brand new, free tutorial on how to build the classic tic-tac-to...'
---

By Per Harald Borgen

If you have a good understanding of HTML, CSS, JavaScript, and React you might be wondering where to go next on your learning journey. So why not check out [Scrimba's brand new, free tutorial](https://scrimba.com/course/greactgame?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article) on how to build the classic tic-tac-toe game in React?

[![Fully working game](https://dev-to-uploads.s3.amazonaws.com/i/xtcbjygjr8s9in2u3nnv.png)](https://scrimba.com/course/greactgame?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article)
_Click above to go to the tutorial._

The example game is pulled from React's official tutorials but is brought up to date using React hooks - the latest hot topic in the React world. 

This article gives you an overview of the tutorial and lets you click through to the screencasts and play with the code at any time.

If your HTML, CSS, JavaScript or React skills feel shaky, never fear - Scrimba offers a huge range of tutorials to bring you up to speed. We recommend the following courses to get you ready for the tic-tac-toe tutorial:

- [HTML & CSS Crash Course](https://scrimba.com/course/ghtmlcss?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article) with Kevin Powell
- [Introduction to Javascript](https://scrimba.com/course/gintrotojavascript?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article) with Dylan C. Israel
- [Learn React for Free](https://scrimba.com/course/glearnreact?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article) with Bob Ziroll

In true Scrimba style, the Build Tic-Tac-Toe with React Hooks tutorial contains loads of interactive challenges along the way, so you'll embed your learning and feel like a hooks wizard by the end of it.

The course is led by Thomas Weibenfalk, a passionate developer, designer, and coding instructor from Sweden. Thomas loves teaching people about front-end development, especially React, making him the ideal teacher to take you through this learning experience.

Assuming you're ready to go with tic-tac-toe, let's get started!

## Introduction

[![Tic-tac-toe with React hooks slide](https://dev-to-uploads.s3.amazonaws.com/i/e9mee46gi4pz43um8h1t.png)](https://scrimba.com/p/pgGEGtW/cPkGD8Sm?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article)

In [the first scrim](https://scrimba.com/p/pgGEGtW/cPkGD8Sm?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article), Thomas tells us about his plans for the tutorial and shares the [Official React Documentation](https://reactjs.org/tutorial/tutorial.html), which we can refer to for a more detailed explanation of the features used to build the game.

As well as talking us through the file structure he has implemented for the app, Thomas also gives us our first glimpse of the finished product. Click the image above to visit the cast.

## Scaffolding Components

[Next up](https://scrimba.com/p/pgGEGtW/cV8eB8fp?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article), Thomas talks us through setting up the Board.js, Game.js and Square.js files needed to create the game. We also see how to import Game.js into the App.js file.

```js
import React from "react";
import Game from "./components/Game";

const App = () => <Game />;

export default App;
```

## Square Component and Destructuring Props

In [the next scrim](https://scrimba.com/p/pgGEGtW/cKp4eRfq?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article), we create our square component using JSX to add a button:

```js
const Square = (props) => (
	<button onClick={props.onClick}>{props.value}</button>
);
```

For our first challenge, Thomas encourages us to destructure out the props in our component. [Click through](https://scrimba.com/p/pgGEGtW/cKp4eRfq?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article) to the cast to give the challenge a try.

## Board Component and Scaffolding Functions

Now it's time to create [the board component](https://scrimba.com/p/pgGEGtW/cypaG6CZ?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article) by importing the square component and adding nine instances of it to the board (note that we will refactor this with a loop to improve the code later):

```js
<div>
	<Square value="1" onClick={() => onClick("dummy value")} />
	<Square value="2" onClick={() => onClick("dummy value")} />
	<Square value="3" onClick={() => onClick("dummy value")} />
	<Square value="4" onClick={() => onClick("dummy value")} />
	<Square value="5" onClick={() => onClick("dummy value")} />
	<Square value="6" onClick={() => onClick("dummy value")} />
	<Square value="7" onClick={() => onClick("dummy value")} />
	<Square value="8" onClick={() => onClick("dummy value")} />
	<Square value="9" onClick={() => onClick("dummy value")} />
</div>
```

Thomas also scaffolds out the functions we need in Game.js, which we'll complete later.

## Square Styling

[![app with styled squares](https://dev-to-uploads.s3.amazonaws.com/i/2zhixfxneekxecwxi2vn.png)](https://scrimba.com/p/pgGEGtW/ceMPzwhB?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article)
_Click the image to access the cast._

[Next up](https://scrimba.com/p/pgGEGtW/ceMPzwhB?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article), we style our squares using the `style` default prop:

```js
const style = {
	background: "lightblue",
	border: "2px solid darkblue",
	fontSize: "30px",
	fontWeight: "800",
	cursor: "pointer",
	outline: "none",
};

const Square = ({ value, onClick }) => (
	<button style={style} onClick={onClick}>
		{value}
	</button>
);
```

## Board Styling

[![app with styled board](https://dev-to-uploads.s3.amazonaws.com/i/ynvasbhvjvj5kr9g5fe4.png)](https://scrimba.com/p/pgGEGtW/c8rJyKcD?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article)
_Click the image to access the scrim._

Now that our squares are ready, it's time to the [style the board](https://scrimba.com/p/pgGEGtW/c8rJyKcD?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article). Thomas kicks us off by once again creating a style object, this time with CSS grid:

```js
const style = {
	border: "4px solid darkblue",
	borderRadius: "10px",
	width: "250px",
	height: "250px",
	margin: "0 auto",
	display: "grid",
	gridTemplate: "repeat(3, 1fr) / repeat(3, 1fr)",
};
```

Our challenge now is to apply the style object to the board. Head over [to the scrim](https://scrimba.com/p/pgGEGtW/c8rJyKcD?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article) to give it a try.

Don't forget, while Thomas has provided some great styling options, Scrimba is fully interactive, so you are free to customize your game however you prefer - let your imagination run wild!

## The calculateWinner Function Explained

```js
export function calculateWinner(squares) {
	const lines = [
		[0, 1, 2],
		[3, 4, 5],
		[6, 7, 8],
		[0, 3, 6],
		[1, 4, 7],
		[2, 5, 8],
		[0, 4, 8],
		[2, 4, 6],
	];
	for (let i = 0; i < lines.length; i++) {
		const [a, b, c] = lines[i];
		if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
			return squares[a];
		}
	}
	return null;
}
```

[Next up](https://scrimba.com/p/pgGEGtW/cBLrMvS2?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article), Thomas explains the all-important `calculateWinner()` function, which is taken from the original tutorial from [reactjs.org](https://reactjs.org/tutorial/tutorial.html). Head over [to the cast](https://scrimba.com/p/pgGEGtW/cBLrMvS2?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article) to explore the function and hear how it works.

## Create States and Fill with Initial Data

In the next [scrim](https://scrimba.com/p/pgGEGtW/c4Pw97tV?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article), we start creating the logic for the game.

We begin by adding a hook called `usedState` in Game.js and creating states to set an empty board and specify the next player. Lastly, we add `const winner`, which tells us whether the latest move was a winning one:

```js
const [board, setBoard] = useState(Array(9).fill(null));
const [xIsNext, setXisNext] = useState(true);
const winner = calculateWinner(board);
```

Over in Board.js, we delete our manually-rendered squares and replace them with mapped squares as promised earlier. [Click through](https://scrimba.com/p/pgGEGtW/c4Pw97tV?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article) to see this in detail:

```js
const Board = ({ squares, onClick }) => (
	<div style={style}>
		{squares.map((square, i) => (
			<Square key={i} value={square} onClick={() => onClick(i)} />
		))}
	</div>
);
```

## Create the handleClick Function

[Next](https://scrimba.com/p/pgGEGtW/c67knwTy?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article), we create the `handleClick()` function, which carries out the calculations when we make a move:

```js
const handleClick = (i) => {
	const boardCopy = [...board];
	// If user click an occupied square or if game is won, return
	if (winner || boardCopy[i]) return;
	// Put an X or an O in the clicked square
	boardCopy[i] = xIsNext ? "X" : "O";
	setBoard(boardCopy);
	setXisNext(!xIsNext);
};
```

## renderMoves Function and the Last JSX

[![Fully working game](https://dev-to-uploads.s3.amazonaws.com/i/xtcbjygjr8s9in2u3nnv.png)](https://scrimba.com/p/pgGEGtW/cNq2EQAL?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article)
_Click above to go to the tutorial._

[In this scrim](https://scrimba.com/p/pgGEGtW/cNq2EQAL?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article), we create the JSX which makes the game playable.

```js
<>
  <Board squares={board} onClick={handleClick} />
  <div style={styles}>
    <p>
      {winner ? "Winner: " + winner : "Next Player: " + (xIsNext ? "X" : "O")}
    </p>
  </div>
</>
```

We now have the all knowledge needed to create a fully working tic-tac-toe game with React hooks!

## BONUS: Implement Time Travel

[![Time travel feature in action](https://dev-to-uploads.s3.amazonaws.com/i/myoj1edcpkv3gx0ry7xj.png)](https://scrimba.com/p/pgGEGtW/cBLr6Df6?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article)
_Click the image to go to the bonus tutorial._

[In the bonus scrim](https://scrimba.com/p/pgGEGtW/cBLr6Df6?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article), we take our game to the next level by implementing time travel to review the moves made throughout the game. Click through to get the goodies in this bonus tutorial.

So there we have it - a fully working tic-tac-toe game using React hooks! I hope you found this tutorial helpful. Don't forget, you can refer back to it at any time to refresh your memory of the topics covered or play around with the code in the interactive screencasts.

Next up, why not check out some of many other tutorials available on [Scrimba?](https://scrimba.com/?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article) With a huge range of topics, there is something for everyone.

Happy learning :)

%[https://www.youtube.com/watch?v=Z5RbPrK4VqM]

