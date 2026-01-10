---
title: How I built a React game with react-dnd and react-flip-move
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-14T00:41:38.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-a-react-game-with-react-dnd-and-react-flip-move-26300156a825
coverImage: https://cdn-media-1.freecodecamp.org/images/1*d4ldJrlOxFf2SABu9HNteg.png
tags:
- name: Games
  slug: games
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Nicholas Vincent-Hill

  This is a high level overview of my implementation of a puzzle/word game built entirely
  in React. It’s not the prettiest code ever written, but I’m happy with my first
  browser-based game.

  Here’s what I built:

  Scrabblr — Impro...'
---

By Nicholas Vincent-Hill

This is a high level overview of my implementation of a puzzle/word game built entirely in React. It’s not the prettiest code ever written, but I’m happy with my first browser-based game.

Here’s what I built:

#### [Scrabblr](https://scrabblr.herokuapp.com/) — Improve your Scrabble skills while having tons of fun

![Image](https://cdn-media-1.freecodecamp.org/images/Yuy7Y3NjzTb45SAG5BmbqDhXrd9qzHj-vEw6)
_Click me to play Scrabblr!_

### **Background**

I was looking at animation solutions in React.js and stumbled upon Joshua Comeau’s [react-flip-move](https://github.com/joshwcomeau/react-flip-move) [demo](http://joshwcomeau.github.io/react-flip-move/examples/#/scrabble?_k=8l9xbo). I saw the potential to build all sorts of scrabble-like games with his cool drag-and-drop and animated motion interface.

### Technical challenges

#### Decorators with Babel

Joshua Comeau’s [react-flip-move](https://github.com/joshwcomeau/react-flip-move) requires function decorators, a language feature not supported by create-react-app’s compiler Babel.

![Image](https://cdn-media-1.freecodecamp.org/images/N1ViOUNEKcBwyVbNoGTuIgc0bQsaV3WREoVh)

The package [react-app-rewired](https://github.com/timarney/react-app-rewired) solves this problem by overriding create-react-app Webpack configs without ejecting (something that’s super scary for a noob like me who didn’t want to deal with Webpack’s complexity under the hood).

![Image](https://cdn-media-1.freecodecamp.org/images/DaNp9bCEpfrPwRdXOfuAz7utnMOXa4P9avjo)
_config-overrides.js_

The above code allowed me to inject the [transform-decorators-legacy](https://github.com/loganfsmyth/babel-plugin-transform-decorators-legacy) plugin (without ejecting) to handle decorators. One problem solved with many more to go.

#### Creating a game loop

To me, what separates a cool thing and a “game” is the concept of a [game loop](https://gamedevelopment.tutsplus.com/articles/gamedev-glossary-what-is-the-game-loop--gamedev-2469).

The main game loop begins with user input (a button clicked to start a new game). The user shuffles tiles and finds words.

Every time the user changes the location of a tile, the game checks for any valid words. If the word is valid, it scores that word and increments the total score by the word’s score. It also adds that word to a “Found Words” array so it doesn’t double count if it’s found again in the future.

When the user finds all possible words (see below for the implementation of the all possible matches problem) or gives up (clicks the surrender button) the game loop ends and a results modal appears.

The data or source of truth is all contained in `state` and passed to my components with the new React.context API (to avoid [prop-drilling](https://itnext.io/compound-components-with-react-v16-3-6679c752bd56)). When a new game loop starts, these values are all reset in `state`.

![Image](https://cdn-media-1.freecodecamp.org/images/OMK5X0IhgiEZaZeOjdAYU6ew5pQJLVO6-sGi)
_Method to initializes game loop inside the App component_

#### Accessing tile location to find characters

This problem took me an embarrassingly long time to solve. The tile’s (x, y) position in the grid matrix is contained in `state.tiles`.

![Image](https://cdn-media-1.freecodecamp.org/images/YESlxksNLL-Mu4pMWirwiv92D4qa-rixtxtM)
_Tiles are created with default properties and held in state_

I needed to be able to scrape letters from tiles by their position and assemble a string to validate. My solution is a complete hack job and I won’t show it here — it’s the `checkForWords()` method in App.js on [my Github](https://github.com/nvincenthill/scrabblr), which is in desperate need of refactoring.

#### Validating words

I also needed a quick way to check if a string of characters was a valid English word. The [free dictionary API’s](https://www.wordsapi.com/) I considered had prohibitively low requests allowed per day and high latency. I needed a solution that allowed me to check an exhaustive local list quickly. The `Object.hasOwnProperty()` method invoked on a dictionary of 270,000+ key-value pairs works nicely and quickly.

![Image](https://cdn-media-1.freecodecamp.org/images/JYbcOMZuVG3ZalGkakc-mETO8t0p8KNJin6K)
_Check a single word against the Scrabble dictionary_

The code below is my solution to find all possible valid words given an array of letters. This is how I calculate the number of words remaining to display to the user and know when to end the game loop.

My original attempt, without utilizing the `Object.hasOwnProperty()` method and speed optimizations took nearly ten seconds to calculate all possible valid words. This implementation appears nearly instantaneous to the user and is called at the start of a new game loop.

![Image](https://cdn-media-1.freecodecamp.org/images/aDj0Di2Pw1a2mswM7RLXRuo67nIJ22fb4-tE)
_Find all possible valid English words given an array of letters_

### **Conclusion**

I learned a lot building this project and I’m proud of the result: my game runs fast and looks good. Eventually I’d like to add OAuth and data permanence, high score record keeping, and user-designed levels.

I’m still new to programming and web design — I’d love to hear your comments/suggestions/critiques in the comments.

Play [Scrabblr here!](https://scrabblr.herokuapp.com/)

![Image](https://cdn-media-1.freecodecamp.org/images/YzhGBRF2K-Z9c8yUrtELsNILPMJlIa1NAu43)

![Image](https://cdn-media-1.freecodecamp.org/images/lesSwgRiwHVV0Y4WKx0M0hr6G84pnN9djrHU)
_Thanks for reading!_

> _Read Next:_

> [Introduction and a little about accessing IEX’s API with JavaScript](https://medium.com/coding-overload/introduction-and-a-little-about-accessing-iexs-api-with-javascript-7ae4e8af79d6)

