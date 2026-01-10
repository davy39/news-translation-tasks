---
title: More project ideas to improve your coding skills
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-18T18:42:43.000Z'
originalURL: https://freecodecamp.org/news/more-project-ideas-to-improve-your-coding-skills-99f48d09bb4b
coverImage: https://cdn-media-1.freecodecamp.org/images/0*hL2XRi5uD_N7Pr8T.png
tags:
- name: application
  slug: application
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Florin Pop

  https://www.youtube.com/watch?v=TNzCfgwIDCY

  Two weeks ago I published an article containing 15 project ideas that you can build
  to level up your coding skills, and people were very excited about that resource.

  Also, the app-ideas reposi...'
---

By Florin Pop

%[https://www.youtube.com/watch?v=TNzCfgwIDCY]

Two weeks ago I published an article containing [15 project ideas](https://medium.freecodecamp.org/here-are-some-app-ideas-you-can-build-to-level-up-your-coding-skills-39618291f672) that you can build to level up your coding skills, and people were very excited about that resource.

Also, the [app-ideas](https://github.com/florinpop17/app-ideas) repository has gotten almost 3000 stars since I published that article. That’s insane! ?

Thank you all for that! ?

In this post we’ll go over some **new** projects that were added to the repository since then.

As a quick reminder, all of the projects are divided into three _tiers_ based on the knowledge and experience required to complete them. Check out the _tiers_ description in the repository.

Below you’ll find 2 **Beginner**, 4 **Intermediate** and 3 **Advanced** project ideas.

### 1. CALCULATOR

**Tier:** 1 — Beginner

Calculators are not only one of the most useful tools available, but they are also a great way to understand UI and event processing in an application. In this problem you will create a calculator that supports basic arithmetic calculations on integers.

The styling is up to you so use your imagination and get creative! You might also find it worth your time to experiment with the calculator app on your mobile device to better understand basic functionality and edge cases.

#### Constraints

* You may not use the `eval()` function to execute calculations

#### User Stories

* User can see a display showing the current number entered or the result of the last operation.
* User can see an entry pad containing buttons for the digits 0–9, operations — ‘+’, ‘-’, ‘/’, and ‘=’, a ‘C’ button (for clear), and an ‘AC’ button (for clear all).
* User can enter numbers as sequences up to 8 digits long by clicking on digits in the entry pad. Entry of any digits more than 8 will be ignored.
* User can click on an operation button to display the result of that operation on: _ the result of the preceeding operation and the last number entered OR _ the last two numbers entered OR * the last number entered
* User can click the ‘C’ button to clear the last number or the last operation. If the users last entry was an operation the display will be updated to the value that preceded it.
* User can click the ‘AC’ button to clear all internal work areas and to set the display to 0.
* User can see ‘ERR’ displayed if any operation would exceed the 8 digit maximum.

#### Bonus features

* User can click a ‘+/-’ button to change the sign of the number that is currently displayed.
* User can see a decimal point (.) button on the entry pad that allows floating point numbers up to 3 places to be entered and operations to be carried out to the maximum number of decimal places entered for any one number.

#### Useful links and resources

* [Calculator (Wikipedia)](https://en.wikipedia.org/wiki/Calculator)
* [MDN](https://developer.mozilla.org/en-US/)

#### Example projects

%[https://codepen.io/giana/pen/GJMBEv]

%[https://codepen.io/mjijackson/pen/xOzyGX]

### 2. RECIPE APP

**Tier:** 1 — Beginner

You might not have realized this, but recipes are nothing more than culinary algorithms. Like programs, recipes are a series of imperative steps which, if followed correctly, result in a tasty dish.

The objective of the Recipe app is to help the user manage recipes in a way that will make them easy to follow.

#### Constraints

* For the initial version of this app, the recipe data may be encoded as a JSON file. After implementing the initial version of this app you may expand on this to maintain recipes in a file or database.

#### User Stories

* User can see a list of recipe titles
* User can click a recipe title to display a recipe card containing the recipe title, meal type (breakfast, lunch, supper, or snack), number of people it serves, its difficulty level (beginner, intermediate, advanced), the list of ingredients (including their amounts), and the preparation steps.
* User click a new recipe title to replace the current card with a new recipe.

#### Bonus features

* User can see a photo showing what the item looks like after it has been prepared.
* User can search for a recipe not in the list of recipe titles by entering the meal name into a search box and clicking a ‘Search’ button. Any open source recipe API may be used as the source for recipes (see The MealDB below).
* User can see a list of recipes matching the search terms
* User can click the name of the recipe to display its recipe card.
* User can see a warning message if no matching recipe was found.
* User can click a ‘Save’ button on the cards for recipes located through the API to save a copy to this apps recipe file or database.

#### Useful links and resources

* [Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
* [Axios](https://www.npmjs.com/package/axios)
* [The MealDB API](https://www.themealdb.com/api.php)

#### Example projects

%[https://codepen.io/eddyerburgh/pen/xVeJvB]

%[https://codepen.io/inkblotty/pen/oxWRme]

### 3. DRAWING APP

**Tier:** 2 — Intermediate

Create digital artwork on a canvas on the web to share online and also export as images.

#### User Stories

* User can draw in a `canvas` using the mouse
* User can change the color
* User can change the size of the tool
* User can press a button to clear the `canvas`

#### Bonus features

* User can save the artwork as an image (`.png`, `.jpg`, etc format)
* User can draw different shapes (`rectangle`, `circle`, `star`, etc)
* User can share the artwork on social media

#### Useful links and resources

* [Learn how to create a Drawing Application using p5js](https://www.florin-pop.com/blog/2019/04/drawing-app-built-with-p5js/)

#### Example projects

%[https://codepen.io/FlorinPop17/pen/VNYyZQ]

%[https://codepen.io/t0mm4rx/pen/dLowvZ]

### 4. EMOJI TRANSLATOR

**Tier:** 2 — Intermediate

Emojis have become the _lingua franca_ of modern society. They are a fun and fast way to communicate, but an also extremely expressive mechanism for communicating emotions and reactions.

The objective of the Emoji Translator app is to translate text entered by the user into an equivalent string of emojis, translated from one or more words in the original text, and words for which there is no corresponding emoji.

#### User Stories

* User can enter a string of words, numbers, and punctuation into a text box
* User can click a ‘Translate’ button to translate words in the entered text into their corresponding emojis.
* User can see a warning message if ‘Translate’ was clicked, but the input text box was empty or unchanged from the last translation.
* User can see text elements in the entered text translated to their equivalent emojis in an output text box. Text elements for which there is no emoji will be left unchanged.
* User can click a ‘Clear’ button to clear the input and output text boxes.

#### Bonus features

* Developer will implement an emoji synonym feature to allow the app to translate a wider variety of words to emoji.
* User can select the language the input text is entered from a dropdown list of languages.

#### Useful links and resources

[Full Emoji List v12.0](https://unicode.org/emoji/charts/full-emoji-list.html)

#### Example projects

[Emoji Translate](https://emojitranslate.com/)

### 5. MEME GENERATOR APP

**Tier:** 2 — Intermediate

Allow users to generate custom memes by adding text over an image.

#### User Stories

* User can upload an image that will appear in a canvas
* User can add text in the top part of the image
* User can add text in the bottom part of the image
* User can select the color of the text
* User can select the size of the text
* User can save the resulting meme

#### Bonus features

* User can select the font-family for the text
* User can share the meme on social media (twitter, reddit, facebook, etc)
* User can drag the text around and place it wherever he wants on top of the image
* User can draw shapes on top of the image (circles, rectangles, or free drawing with the mouse)

#### Useful links and resources

Working with canvas is made very easy by the [p5js](http://p5js.org/) library.

#### Example projects

[Meme Generator by imgflip](https://imgflip.com/memegenerator)

%[https://codepen.io/ninivert/pen/BpLKRx]

### 6. TYPING PRACTICE

**Tier:** 2 — Intermediate

Some things are so obvious they can be easily overlooked. As a developer your ability to type quickly and accurately is one factor that influences your development productivity. The objective of the Typing Practice app is to provide you with typing practice along with metrics to allow you to measure your progress.

Typing practice displays a word which you must then type within a specific interval of time. If the word is incorrectly typed it stays on screen and the time interval remains the same. But when the word is correctly typed a new word is displayed and the time interval is slightly reduced.

Hopefully, this repetitive practice will help you improve both your typing speed and accuracy.

#### User Stories

* User can see the time interval words must be typed in displayed in the app window.
* User can see the number of successful attempts and the number of total attempts in a score box.
* User can click a ‘Start Practice’ button to start the practice session.
* User can see the prompt word displayed in a text box.
* User can begin typing the word in a text input box.
* User can see the letters that have been typed flash if an incorrect letter is entered and the text input box will be cleared.
* User can see the a message adjacent to the text input box indicating the user should try again if an incorrect letter is entered.
* User can see the number of total attempts incremented in the score box.
* User can see a congratulations message if the word is correctly typed.
* User can see the time interval words must be typed decremented by a small amount if the word is correctly typed.
* User can see the number of successful attempts incremented in the score box if the word was correctly typed.
* User can click a ‘Stop Practice’ button to stop the practice session.

#### Bonus features

* User can hear a unique audible tone signaling when a new word is displayed, a word is correctly entered, or an incorrect letter is typed in the word.
* User can login to the app
* User can see cumulative performance statistics across all of his/her practice sessions.

#### Useful links and resources

* [keydown](https://developer.mozilla.org/en-US/docs/Web/Events/keydown)
* [setInterval](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)

#### Example projects

[Twiddler Typing Tutor](http://twiddler.tekgear.com/tutor/twiddler.html)

### 7. ELEVATOR

**Tier:** 3 — Advanced

It’s tough to think of a world without elevators. Especially if you have to walk up and down 20 flights of stairs each day. But, if you think about it elevators were one of the original implementations of events and event handlers long before web applications came on the scene.

The objective of the Elevator app is to simulate the operation of an elevator and more importantly, how to handle the events generated when the buildings occupants use it. This app simulates occupants calling for an elevator from any floor and pressing the buttons inside the elevator to indicate the floor they wish to visit.

#### Constraints

* You must implement a single event handler for the up and down buttons on each floor. For example, if there are 4 floors a single event handler should be implemented rather than 8 (two buttons per floor).
* Similarly, a single event handler should be implemented for all buttons on the control panel in the elevator rather than a unique event handler for each button.

#### User Stories

* User can see a cross section diagram of a building with four floors, an elevator shaft, the elevator, and an up button on the first floor, up and down buttons on the second and third floors, and a down button on the fourth floor.
* User can see the elevator control panel with a button for each of the floors to the side of the diagram.
* User can click the up and down button on any floor to call the elevator.
* User can expect that clicking the up and down buttons on any floor to request the elevator will be queued and serviced in the sequence they were clicked.
* User can see the elevator move up and down the shaft to the floor it was called to.
* User can click the elevator control panel to select the floor it should travel to.
* User can expect the elevator to pause for 5 seconds waiting for a floor button on the control panel to be clicked. If a floor button isn’t clicked within that time the elevator will process the next call request.
* User can expect the elevator to return to the first floor when there are no requests to process.

#### Bonus features

* User can see a warning notification if the number of elevator requests exceeds the maximum number allowed. This limit is left to the developer.
* User can hear a sound when the elevator arrives at a floor.
* User can see an occupant randomly arrive at a floor to indicate when the user should click the up or down elevator call button on that floor.
* User can specify the time interval between new occupants arriving to call an elevator.

#### Useful links and resources

[First-in, first out queue (Wikipedia)](https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics))

#### Example projects

%[https://codepen.io/nibalAn/pen/prWdjq]

### 8. FAST FOOD SIMULATOR APP

**Tier:** 3 — Advanced

Fast Food app simulates the operation of a simple take-away restaurant and is designed to help the developer put their knowledge of Promises and SOLID design principles to work.

This app simulates customers of a take-away restaurant placing orders and and waiting for them to be prepared and delivered to a pickup counter. After placing the order the customer waits on the order to be announced before picking it up and proceeding to the dining area.

The user stories that make up this app center around four distinct roles:

* User — the end user using the application
* Customer — the simulated Customer
* Order Taker — the simulated Order Taker
* Cook — the simulated Cook
* Server — the simulated Server

This app has quite a few User Stories. Don’t be overwhelmed though. Take the time to sketch out not just the UI, but how the different actors (roles) interact and incrementally build the app following Agile principles.

#### Constraints

* Order tickets can be represented as two different types of Promises — one the Server waits on while the Cook prepares the order and another the Customer waits on while in the serving line.
* Use the native equivalent of JS Promises in whichever language you choose to develop in. JS developers should use native Promises and not `async/await`.
* Create this app using native language features. You may NOT use a simulation package or library.
* New customers arrive in the order line at a fixed interval of time. In other words, new customers arrive at a constant rate.
* Order tickets are fulfilled at a fixed interval of time as well. They are completed at a constant rate.

#### User Stories

**Application Operation**

* User can see an input area that allows the entry of the time interval for customer arrival and a time interval for the fulfillment of an _order ticket_ by the cook.
* User can see a customized warning message if the customer arrival interval or the order fulfillment interval is incorrectly entered.
* User can start the simulation by clicking on a Start button.
* User can see an order line area containing a text box showing the number of customers waiting to place orders.
* User can see an order area containing text boxes showing the _order number_ currently being taken.
* User can see a kitchen area containing a text box showing the _order number_ that’s being prepared and a text box listing the waiting orders in sequence, along with a count of the number of waiting orders.
* User can see a Pickup area containing a text box showing the _order number_ that’s currently available for pickup by the Customer and a text box showing the number of Customers waiting in the serving line.
* User can stop the simulation at any time by clicking a Stop button.

#### Bonus features

* User can specify how long it takes for an Order Taker to create an _order ticket_.
* User can specify how long it takes for the Server to deliver an order to the customer.
* User can specify the total amount of time the simulation is to run once the Start button has been clicked.
* User can see an animated view of Customers and orders as they move through the workflow.

#### Useful links and resources

* [Fast Food Simulator — Logical Workflow](https://drive.google.com/file/d/1Thfm5cFDm1OjTg_0LsIt2j1uPL5fv-Dh/view?usp=sharing)
* [Agile Manifesto & 12 Principles of Agile Software](http://agilemanifesto.org/)
* [SOLID Principles Every Developer Should Know](https://blog.bitsrc.io/solid-principles-every-developer-should-know-b3bfa96bb688)
* [Using Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)
* [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)

### 9. SHELL GAME

**Tier:** 3 — Advanced

A Shell game is a classic gambling game that dates back to ancient Greece. Playing it requires three shells, a pea, hand dexterity by the operator, and keen observation skills on the part of the player. It’s also a classic con game since it’s easy for the operator to swindle the player. Thank goodness the latter isn’t our intent with this app.

This Shell game is intended to provide a graphical interface to the classical shell game and to provide the player with an honest game to play. Our game draws three shells on the canvas along with the pea, moves the pea under one, of the shells, and shuffles the shells for a specific interval of time. The user must then click on the shell they think the pea is hidden under. The user is allowed to continue guessing until the pea is located.

#### User Stories

* User can see the canvas with three shells and the pea.
* User can click the shell the pea is to be hidden under.
* User can see the pea move under the shell thats been clicked.
* User can click on a ‘Shuffle’ button to start an animated shuffling of the shells for 5 seconds.
* User can click on the shell she believes the pea is hidden under when the animation stops.
* User can see the shell that has been clicked rise to reveal if the pea is hidden under it.
* User can continue clicking shells until the pea is found.
* User can see a congratulations message when the pea is located
* User can start a new game by clicking a shell the pea is to be hidden under (step #2 above). The steps above are then repeated.

#### Bonus features

* User can see a score panel containing the number of wins and the number of games played.
* User can see the number of games played increase when the pea is hidden under a shell
* User can see the number of wins incremented when the pea is found on the first guess.
* User can see the shell hiding the pea to animate (color, size, or some other effect) when it is clicked (a correct guess).

#### Useful links and resources

* [Shell Game (Wikipedia)](https://en.wikipedia.org/wiki/Shell_game)
* [Javascript HTML DOM Animation](https://www.w3schools.com/js/js_htmldom_animate.asp)
* [p5js Animation Library](https://p5js.org/)

#### Example projects

%[https://codepen.io/RedCactus/pen/dwEjXy]

### Conclusion

Don’t forget to check out the [previous article](https://www.freecodecamp.org/news/here-are-some-app-ideas-you-can-build-to-level-up-your-coding-skills-39618291f672/) and the [repository](https://github.com/florinpop17/app-ideas) if you want to find more application/project ideas.

Also, if the information from this article and from the repo was useful to you in any way, make sure you give it a star ?; this way others can find it and benefit too! Thank you!

Do you have any suggestions on how we could improve this project overall? Let us know! We’d love to hear your feedback!

You are welcomed to contribute with your own ideas! We can make this repository the go-to resource when it comes to app ideas.

_Originally published at [www.florin-pop.com](https://www.florin-pop.com/blog/2019/04/more-project-ideas-to-improve-your-coding-skills/)._

