---
title: Memory Game in Vanilla JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-28T14:31:49.000Z'
originalURL: https://freecodecamp.org/news/vanilla-javascript-tutorial-build-a-memory-game-in-30-minutes-e542c4447eae
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ikkvZ9ToN2kCtpUSP6702w.gif
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Marina Ferreira

  Learn JS, CSS and HTML by building a memory game in 30 minutes!

  This tutorial explains some basic HTML5, CSS3 and JavaScript concepts. We will discuss
  data attribute, positioning, perspective, transitions, flexbox, event handling,
  ...'
---

By Marina Ferreira

#### Learn JS, CSS and HTML by building a memory game in 30 minutes!

This tutorial explains some basic HTML5, CSS3 and JavaScript concepts. We will discuss data attribute, positioning, perspective, transitions, flexbox, event handling, timeouts and ternaries. You are not expected to have much prior knowledge in programming. If you know what HTML, CSS and JS are for, it’s more than enough!

* ?Demo: M[emory Game Project](https://marina-ferreira.github.io/memory-game/)

### File Structure

Let’s start creating the files in the terminal:

```
? mkdir memory-game ? cd memory-game ? touch index.html styles.css scripts.js ? mkdir img  
```

### `HTML`

`The initial template linking both `css` and `js` files.`

`The game has 12 cards. Each card consists of a container `div` named `.memory-card`, which holds two `img` elements. The first one represents the card `front-face` and the second its `back-face`.`

![Image](https://cdn-media-1.freecodecamp.org/images/0*LXwjdEFd1dhLuME-.jpg)

`You can download the assets for this project at: [Memory Game Repo](https://github.com/code-sketch/memory-game).`

`The set of cards will be wrapped in a `section` container element. The final result:`

### `CSS`

`We will use a simple but yet very useful reset, applied to all items:`

`The `box-sizing: border-box` property includes padding and border values into element’s total width and height, so we can skip the math.`

`By setting [display: flex](https://marina-ferreira.github.io/tutorials/css/flexbox/#introduction) to the `body` and `margin: auto` to the `.memory-game` container, it will be centered both vertically and horizontally.`

`.memory-game` will also be a `flex-container`. By default, the items are set to shrink in width to fit the container. By setting [flex-wrap](https://marina-ferreira.github.io/tutorials/css/flexbox/#flex-wrap) to `wrap`, `flex-items` wrap along multiple lines, accordingly to their size.

`Each card `width` and `height` is calculated with [calc()](https://developer.mozilla.org/en-US/docs/Web/CSS/calc) CSS function. Let’s make three rows, four card each by setting `width` to `25%` and `height` to `33.333%` minus `10px` from `margin`.`

`To position `.memory-card` children, let’s add `position: relative` so we can position the children absolutely, relative to it.`

`The property `position: absolute` set to both `front-face` and `back-face`, will remove the elements from the original position, and stack them on top of each other.`

`The template should be looking like this:`

![Image](https://cdn-media-1.freecodecamp.org/images/0*XCqaVtrSiWnr7Ucp.jpg)

`Let’s also add a click effect. The `:active` pseudo class will be triggered every time the element gets clicked. It will apply a .2s transition to its size:`

![Image](https://cdn-media-1.freecodecamp.org/images/0*NediqPWKuwU_g0i8.gif)

### `Flip Card`

`To flip the card when clicked, a class `flip` is added to the element. For that, let’s select all `memory-card` elements with `document.querySelectorAll`. Then loop through them with `forEach` and attach an event listener. Every time a card gets clicked `flipCard` function will be fired. The `this` variable represents the card that was clicked. The function accesses the element’s `classList` and toggles the `flip` class:`

`In the CSS the `flip` class rotates the card 180deg:`

`To produce the 3D flip effect, we will add the [perspective](https://developer.mozilla.org/en-US/docs/Web/CSS/perspective) property to `.memory-game`. That property sets how far in the `z` plane the object is from the user. The lower the value the bigger the perspective effect. For a subtle effect, let’s apply `1000px`:`

`To the `.memory-card` elements let’s add `transform-style: preserve-3d`, to position them in the 3D space created in the parent, instead of flattening it to the `z = 0` plane ([transform-style](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-style)).`

`Now, a transition has to be applied to the `transform` property to produce the movement effect:`

`So, we got the card to 3D flip, yay! But why isn’t the card face showing up? Right now, both `.front-face` and `.back-face` are stacked up onto each other, because they are absolutely positioned. Every element has a `back face`, which is a mirror image of its `front face`. The property [backface-visibility](https://developer.mozilla.org/en-US/docs/Web/CSS/backface-visibility) defaults to `visible`, so when we flip the card, what we get is the JS badge back face.`

![Image](https://cdn-media-1.freecodecamp.org/images/0*k2MPONGEHyHGYvyl.gif)

`To reveal the image underneath it, let’s apply `backface-visibility: hidden` to `.front-face` and `.back-face`.`

`If we refresh the page and flip a card, it’s gone!`

![Image](https://cdn-media-1.freecodecamp.org/images/0*YCMzdW-z0yruzOPf.gif)

`Since we’ve hidden both images back face, there is nothing in the other side. So now we have to turn the `.front-face` 180 degrees:`

`And now, there’s the desired flip effect!`

![Image](https://cdn-media-1.freecodecamp.org/images/0*QQAnvvQeYs7iFSAo.gif)

### `Match card`

`Now that we have flipping cards, let’s handle the matching logic.`

`When we click the first card, it needs to wait until another card is flipped. The variables `hasFlippedCard` and `flippedCard` will manage the flip state. In case there is no card flipped, `hasFlippedCard` is set to `true` and `flippedCard` is set to the clicked card. Let’s also switch the `toggle` method to `add`:`

`So now, when the user clicks the second card, we will fall into the else block in our condition. We will check to see if it’s a match. In order to do that, let’s identify each card.`

`Whenever we feel like adding extra information to HTML elements, we can make use of [data attributes](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes). By using the following syntax: `data-*`, where, `*` can be any word, that attribute will be inserted in the element’s dataset property. So, let’s add a `data-framework` to each card:`

`So now we can check for a match by accessing both cards dataset. Let’s extract the matching logic to its own method `checkForMatch()` and also set `hasFlippedCard` back to false. In case of a match, `disableCards()` is invoked and the event listeners on both cards are detached, to prevent further flipping. Otherwise, `unflipCards()` will turn both cards back by a 1500ms timeout that removes the `.flip` class:`

`Putting all together:`

`A more elegant way of writing the matching condition is to use a [ternary operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator). It’s composed by three blocks. The first block is the condition to be evaluated. The second block is executed if the condition returns true, otherwise the executed block is the third:`

### `Lock Board`

`So now that we have the matching logic covered, we need to lock the board. We lock the board to avoid two sets of cards being turned at the same time, otherwise the flipping will fail.`

![Image](https://cdn-media-1.freecodecamp.org/images/0*z1gY24eYgqu2cjvw.gif)

`Let’s declare a `lockBoard` variable. When the player clicks the second card, `lockBoard` will be set to `true` and the condition `if (lockBoard) return;` will prevent any card flipping before the cards are hidden or match:`

### `Same Card Click`

`The is still the case where the player can click twice on the same card. The matching condition would evaluate to true, removing the event listener from that card.`

![Image](https://cdn-media-1.freecodecamp.org/images/0*WuPO5Ra7nRNJkZIO.gif)

`To prevent that, let’s check if the current clicked card is equal to the `firstCard` and return if positive.`

`The `firstCard` and `secondCard` variables need to be reset after each round, so let’s extract that to a new method `resetBoard()`. Let’s place the `hasFlippedCard = false;` and `lockBoard = false` there too. The es6 [destructuring assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment) `[var1, var2] = ['value1', 'value2']`, allows us to keep the code super short:`

`The new method will be called both from `disableCards()` and `unflipCards()`:`

### `Shuffling`

`Our game looks pretty good, but there is no fun if the cards are not shuffled, so let’s take care of that now.`

`When `display: flex` is declared on the container, `flex-items` are arranged by the following hierarchy: _group_ and _source_ order. Each group is defined by the [order](https://marina-ferreira.github.io/tutorials/css/flexbox/#order) property, which holds a positive or negative integer. By default, each `flex-item` has its `order` property set to `0`, which means they all belong to the same group and will be laid out by source order. If there is more than one group, elements are firstly arranged by ascending group order.`

`There is 12 cards in the game, so we will iterate through them, generate a random number between 0 and 12 and assign it to the flex-item `order` property:`

`In order to invoke the `shuffle` function, let’s make it a [Immediately Invoked Function Expression (IIFE)](https://developer.mozilla.org/en-US/docs/Glossary/IIFE), which means it will execute itself right after its declaration. The scripts should look like this:`

`And that’s all folks!`

`You can also find a video explanation at ? C[ode Sketch Channel.](https://www.youtube.com/watch?v=eMhiMsEC9Uk&list=PLLX1I3KXZ-YH-woTgiCfONMya39-Ty8qw)`

### `References`

* `[Marina Ferreira — Flexbox Fundamentals](https://marina-ferreira.github.io/tutorials/css/flexbox/)`
* `[MDN Web Docs — Main Axis](https://developer.mozilla.org/en-US/docs/Glossary/Main_Axis)`
* `[MDN Web Docs — Cross Axis](https://developer.mozilla.org/en-US/docs/Glossary/Cross_Axis)`
* `[MDN Web Docs — calc](https://developer.mozilla.org/en-US/docs/Web/CSS/calc)`
* `[MDN Web Docs — perspective](https://developer.mozilla.org/en-US/docs/Web/CSS/perspective)`
* `[MDN Web Docs — transform-style](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-style)`
* `[MDN Web Docs — backface-visibility](https://developer.mozilla.org/en-US/docs/Web/CSS/backface-visibility)`
* `[MDN Web Docs — Using data attributes](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes)`
* `[MDN Web Docs — order](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Ordering_Flex_Items)`
* `[MDN Web Docs — IIFE](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)`
* `[MDN Web Docs — ternary operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator)`
* `[MDN Web Docs — destructuring assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)`

`_Originally published at [marina-ferreira.github.io](https://marina-ferreira.github.io/tutorials/js/memory-game/)._`

