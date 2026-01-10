---
title: React Conditional Rendering –  Explained with Examples From BBC Sports
subtitle: ''
author: Rufai Mustapha
co_authors: []
series: null
date: '2023-04-04T00:23:29.000Z'
originalURL: https://freecodecamp.org/news/react-conditional-rendering
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/poster--1-.jpg
tags:
- name: React
  slug: react
seo_title: null
seo_desc: "Conditional rendering is a powerful tool for creating dynamic and engaging\
  \ user interfaces in React applications. \nYou can use it to control what content\
  \ is rendered and when, and it improves user experience, simplifies your code, and\
  \ helps you creat..."
---

Conditional rendering is a powerful tool for creating dynamic and engaging user interfaces in React applications. 

You can use it to control what content is rendered and when, and it improves user experience, simplifies your code, and helps you create more flexible and adaptable components.

### Code Sample

* The code in this article can be found [here](https://github.com/rufai/bbcquiz/tree/master/src).
* The examples used in this article are inspired by [The 100 Premier League Goals Quiz](https://bbc.com/sport/football/61202500) on the BBC. 

### Prerequisites

Before learning about React component rendering, it is important to have a basic understanding of HTML, CSS, and JavaScript.

* You should also have a basic understanding of React itself, including its fundamental concepts such as state, props, and lifecycle methods.
* Additionally, it is important to understand the concept of virtual DOM and how it works in React, as it is closely related to component rendering.

### What You Will Learn In This Article

* How to return different JSX depending on a condition.
* How to conditionally include or exclude a piece of JSX.
* Common conditional syntax shortcuts you’ll encounter in React codebase.

### About The Demos

In each demo that you'll see below:

* I show the demo video of what I'll show you how to create,
* then I show the code that achieves what is in the video,
* and finally, I explain the code.

## Table of Contents

1. [What is React conditional rendering](#heading-what-is-react-conditional-rendering)?

* Define React conditional rendering and how it works
* Why conditional rendering is necessary in React applications

2.  [How to implement React conditional rendering](#heading-how-to-implement-react-conditional-rendering)

*  The ternary operator and the `&&` operator
* Code examples for each method

3.  [How to manage application state for conditional rendering](#heading-how-to-manage-application-state-for-conditional-rendering)

* How application state can be used to control when content is rendered.
* How to use the `useState` hook to manage state for conditional rendering.
* Demo 1 - Login Logout
* Demo 2 - How To Play Button

4.  [Advanced: How to Use Props to Cause React Conditional Rendering](#heading-advanced-how-to-use-props-to-cause-react-conditional-rendering)

* Rendering components based on props
* Demo 3 - Component ABC
* Demo 4 - Start Quiz

5.  [Further Reading](#heading-further-reading)

## What Is React Conditional Rendering?

In React, conditional rendering is the process of displaying different content based on certain conditions or states. It allows you to create dynamic user interfaces that can adapt to changes in data and user interactions. 

In this process, you can use conditional statements to decide what content should be rendered.

### Why Conditional Rendering is Necessary in React Applications

There are several reasons why you might want to use conditional rendering in your React applications:

1. Improved User Experience: Conditional rendering allows you to create dynamic user interfaces that adapt to changes in data and user interactions. By showing and hiding content based on the user's actions or the application state, you can create a more intuitive and engaging user experience.
2. Improved Performance: By conditionally rendering content, you can avoid rendering unnecessary components and improve the performance of your application. This is particularly important in larger applications where unnecessary rendering can lead to performance issues.
3. Simplified Code: Conditional rendering can help you simplify your code and make it more readable. By using conditional statements to decide what content should be rendered, you can avoid duplicating code and create more modular components.
4. Flexibility: Conditional rendering allows you to create more flexible and customizable components. By rendering different content based on the application state, you can create components that can be used in different contexts and adapt to different user interactions.

## How to Implement React Conditional Rendering

In React, there are different ways to conditionally render content based on the state of a component or other conditions. Two common ways are using the ternary operator and the `&&` operator.

```js
function Greeting(props) {
  const isLoggedIn = props.isLoggedIn;
  return (
    <div>
      {isLoggedIn ? (
        <h1>Welcome back!</h1>
      ) : (
        <h1>Please sign up.</h1>
      )}
    </div>
  );
}
```

In the above code, we used the ternary operator `isLoggedIn ? ... : ...` to conditionally render the message depending on whether the user is logged in or not.	

```js
function Greeting(props) {
  const isLoggedIn = props.isLoggedIn;
  return (
    <div>
      {isLoggedIn && <h1>Welcome back!</h1>}
    </div>
  );
}

```

In the above code, we used the `&&` operator to conditionally render the message if `isLoggedIn` is `true`.

Both of these methods are effective for conditionally rendering content in React. Which one to use often comes down to personal preference or the specific use case.

The ternary operator may be more useful when there are multiple conditions to check, while the `&&` operator can be simpler and more concise when there is only one condition.

## How to Manage Application State For Conditional Rendering

In React, the application state can be used to control when and how content is rendered. The application state is a central repository of data that is used by the application to render the user interface. When the application state changes, React re-renders the components that depend on that state.

One way to use the application state to control rendering is to conditionally render components based on the state. For example, if you have a component that should only be displayed when a certain condition is met, you can use the application state to control when the component is rendered.

Another way to use the application state to control rendering is to pass state variables down to child components as props. This allows child components to render content based on the state of the parent component.

Here is an example of how you can use the application state to control rendering in React:

### Demo 1 - Login Logout

%[https://youtu.be/y0Dpte_sDKU]

```js
import React, { useState } from "react";

const App = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleLogin = () => {
    setIsLoggedIn(true);
  };

  const handleLogout = () => {
    setIsLoggedIn(false);
  };

  return (
    <div>
      {isLoggedIn ? (
        <div>
          <h1>Welcome Back!</h1>
          <button onClick={handleLogout}>Logout</button>
        </div>
      ) : (
        <div>
          <h1>Please Login</h1>
          <button onClick={handleLogin}>Login</button>
        </div>
      )}
    </div>
  );
};

export default App;

```

In this example, we have a component `App` that renders different content based on the isLoggedIn state. Initially, `isLoggedIn` is set to false using the useState hook.

When the user clicks on the "Login" button, the `handleLogin` function is called, which sets the `isLoggedIn` state to `true`. Similarly, when the user clicks on the "Logout" button, the `handleLogout` function is called, which sets the `isLoggedIn` state to `false`.

The `return` statement of the `App` component uses a ternary operator to render different content based on the value of `isLoggedIn`. If `isLoggedIn` is `true`, it renders a welcome message and a "Logout" button. If `isLoggedIn` is `false`, it renders a message asking the user to login along with a "Login" button.

This example demonstrates how you can use conditional rendering to create dynamic user interfaces that can adapt to changes in the application state. 

By using the `useState` hook to manage the `isLoggedIn` state and conditional statements to decide what content should be rendered, we can create a simple login/logout system that changes the content of the page based on the user's authentication status.

### Demo 2 - Build a How to Play Button

%[https://youtu.be/0dGhpmNAb8A]



![Image](https://www.freecodecamp.org/news/content/images/2023/04/toplay.JPG)
_Folder Structure for How To Play Component_

```js
import React, { useState } from "react";

import "./style.css";

const HowToPlay = () => {
  const [showRules, setShowRules] = useState(false);

  const toggleRules = () => {
    setShowRules(!showRules);
  };

  return (
    <div>
      <button className="flat-black-button" onClick={toggleRules}>
        How to Play
      </button>
      {showRules ? (
        <div>
          <p className="flat-black-button-content">
            To get under way, click 'Start'. Once you have started the quiz,
            type an answer into the box and either hit enter or click the submit
            button. If you are right, it will fill in the correct slot in the
            table. Keep entering more answers until you've successfully
            completed the quiz - or the timer runs out. If you do not want to
            play any more, just hit the 'Give up!' button. You can then reveal
            the answers you missed - or have another go.
          </p>
        </div>
      ) : null}
    </div>
  );
};

export default HowToPlay;

```

This component displays a "How to Play" button and shows the game instructions when the button is clicked.   
  
Let's break down the code:

* We use the `useState` hook to create a state variable `showRules` and its setter function `setShowRules`, initialized to `false`. This state toggles the display of the game instructions when the button is clicked.
* The `toggleRules` function is called when the "How to Play" button is clicked, which toggles the `showRules` state using `setShowRules`.
* The `return` statement displays the "How to Play" button using a button element, which has a class name of "flat-black-button". It also conditionally displays the game instructions if `showRules` is `true`.
* We display the game instructions using a paragraph element, which has a class name of "flat-black-button-content".
* Finally, we export the `HowToPlay` component as the default export of the module.

You can use this component in other parts of the application where the "How to Play" button is needed. When the button is clicked, the game instructions will be displayed or hidden based on the current state of `showRules`.

## Advanced: How to Use Props to Cause React Conditional Rendering  


![Image](https://www.freecodecamp.org/news/content/images/2023/04/Group-8.jpg)
_Component A,B, and C are children of App_

The above diagram shows how a parent component named "App" communicates, indicated with a black line, with its child components, A, B, and C. 

Component A needs to talk to components B and C, so it sends a message, indicated by the red line, to App using "props". App then passes that message down to B and C using their own "props".

### Demo 3 - Component ABC

%[https://youtu.be/nAv0ksWYfls]

```js
import "./App.css";

import React, { useState } from "react";

function App() {
  return (
    <div>
      <A />
    </div>
  );
}

function A() {
  const [showB, setShowB] = useState(false);
  const [showC, setShowC] = useState(false);
  const [text, setText] = useState("");

  const handleInputChange = (event) => {
    setText(event.target.value);
    setShowB(true);
    setShowC(true);
  };

  return (
    <div className="App">
      <input type="text" onChange={handleInputChange} />
      {showB && <B text={text} />}
      {showC && <C text={text} />}
    </div>
  );
}

function B(props) {
  const { text } = props;
  return <h1>Component B - {text.toUpperCase()}</h1>;
}

function C(props) {
  const { text } = props;
  return <h1>Component C - {text.toLowerCase()}</h1>;
}

export default App;

```

In this example, the `A` component has three state variables: `showB`, `showC`, and `text`. When the input field value changes, the `handleInputChange` function is called and based on the input field value, the `text` state variable is updated and `showB` and `showC` state variables are set to `true`.

The `B` and `C` components are functional components that receive the `text` prop as input and render the text in different ways – `B` component renders the text in uppercase, while `C` component renders the text in lowercase.

The `&&` operator is used to conditionally render the components based on their respective state variables.  
  
Let see how this concepts is used in a product app.

### Demo 4 - Start Quiz

 Demo 4 is another version of the last example.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Group-9.jpg)
_Clicking the StartQuiz's button will trigger the Timer and populate the PlayerNameTable_

When the user clicks the "StartQuiz" button, a Timer begins counting down, and a signal is sent to populate the PlayerNameTable.

%[https://youtu.be/QM9b69PfVjE]

### Timer Component

```js
import React, { useEffect } from "react";
import { useTimer } from "react-timer-hook";

const Timer = ({ expiryTimestamp, shouldTimerStart }) => {
  const { seconds, minutes, start, reset } = useTimer({
    expiryTimestamp,
    autoStart: false,
  });
  useEffect(() => {
    if (shouldTimerStart) {
      start();
    }
  }, [shouldTimerStart]);

  return (
    <div>
      {minutes}:{seconds < 10 ? `0${seconds}` : seconds}
    </div>
  );
};

export default Timer;

```

This is a React component that uses the `useTimer` hook from the `react-timer-hook` library to create a countdown timer. Let's break it down:

1. Import the necessary dependencies: `React` and `useTimer` from the `react-timer-hook` library.
2. Define the `Timer` component, which takes two props: `expiryTimestamp` and `shouldTimerStart`.
3. Destructure the `seconds`, `minutes`, `start`, and `reset` properties from the `useTimer` hook. The `useTimer` hook takes an options object with an `expiryTimestamp` property that specifies the time at which the timer should expire, and an `autoStart` property that specifies whether the timer should start automatically when the component mounts.
4. Use the `useEffect` hook to start the timer when `shouldTimerStart` changes. The `useEffect` hook takes a callback function that runs after every render, and an array of dependencies that determines when the callback should run. In this case, the callback runs whenever `shouldTimerStart` changes.
5. Render the timer using the `minutes` and `seconds` properties, with a conditional statement that adds a leading zero to the seconds when they are less than 1o.
6. Export the Timer component as the default export of the module.

### PlayerNameTable

```js
import React, { useState, useEffect } from "react";

import "./style.css";

const PlayerNameTable = ({ trigger }) => {
  const data = require("../data/League100.json");
  console.log(data);

  const [shouldShowData, updateShouldShowData] = useState(false);

  useEffect(() => {
    if (trigger) {
      updateShouldShowData(trigger);
    }
  }, [trigger]);

  return (
    <table>
      <thead>
        <tr>
          <th>Rank</th>
          <th>Goals</th>
          <th>Clubs</th>
          <th>Player</th>
        </tr>
      </thead>
      <tbody>
        {shouldShowData ? (
          data.sort().map((player, index) => (
            <tr key={index}>
              <td>{index + 1}</td>
              <td>{player.goals}</td>
              <td>{player.clubs}</td>
              {/* <td>{player.name || player.player}</td> */}
            </tr>
          ))
        ) : (
          <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
          </tr>
        )}
      </tbody>
    </table>
  );
};

export default PlayerNameTable;

```

This is a React component that renders a Premier League table. Let's break it down:

1. Import the necessary dependencies: `React`, `useState`, and `useEffect`.
2. Import the `style.css` file, which presumably contains CSS styles for the table.
3. Define the `PlayerNameTable` component, which takes one prop: `trigger`.
4. Load the data for the Premier League table from a JSON file using `require`. The JSON data contains information about players, including their rank, number of goals, club, and name.
5. Use the `useState` hook to define a state variable `shouldShowData`, which determines whether the data should be shown in the table or not. By default, it is set to `false`.
6. Use the `useEffect` hook to update the `shouldShowData` state variable whenever the `trigger` prop changes. This allows the parent component to control when the data is shown in the table.
7. Render the table using the `table`, `thead`, `tbody`, and `tr` HTML elements, along with the `th` and `td` elements for the table headers and data cells.
8. Use a conditional statement to determine whether to show the data or an empty table. If `shouldShowData` is `true`, sort the `data` array by rank and map over it to render each player's data as a table row. If `shouldShowData` is `false`, render an empty table row.
9. Export the `PlayerNameTable` component as the default export of the module.

### StartQuiz

```js
import React, { useState } from "react";
import "./style.css";

function Quiz({ trigger }) {
  const [isStarted, setIsStarted] = useState(false);
  const [answer, setAnswer] = useState("");

  const handleStartClick = () => {
    setIsStarted(true);
    trigger(true);
  };

  const handleResetClick = () => {
    setIsStarted(false);
    trigger(false);
  };

  const handleSubmitClick = () => {
    // Do something with the answer, e.g. validate it
  };

  return (
    <div>
      {isStarted ? (
        <div>
          <input
            type="text"
            value={answer}
            onChange={(e) => setAnswer(e.target.value)}
          />
          <button className="submit-button" onClick={handleSubmitClick}>
            Submit
          </button>
          <button className="reset-button" onClick={handleResetClick}>
            Reset
          </button>
        </div>
      ) : (
        <button className="start-button" onClick={handleStartClick}>
          Start Quiz
        </button>
      )}
    </div>
  );
}

export default Quiz;

```

This is a React component that represents a simple quiz. Here's what it does:

1. Import the necessary dependencies: `React` and `useState`.
2. Import the `style.css` file, which presumably contains CSS styles for the quiz.
3. Define the `Quiz` component, which takes one prop: `trigger`.
4. Use the `useState` hook to define two state variables: `isStarted`, which determines whether the quiz has been started or not, and `answer`, which stores the user's answer to the quiz question.
5. Define three functions to handle user events: `handleStartClick`, `handleResetClick`, and `handleSubmitClick`.
6. In the `handleStartClick` function, set the `isStarted` state variable to `true` and trigger the `trigger` prop to inform the parent component that the quiz has started.
7. In the `handleResetClick` function, set the `isStarted` state variable to `false` and trigger the `trigger` prop to inform the parent component that the quiz has been reset.
8. In the `handleSubmitClick` function, do something with the user's answer, such as validating it against the correct answer.
9. In the `return` statement, render the quiz based on whether it has been started or not. If `isStarted` is `true`, render an input field for the user's answer, along with a "Submit" button and a "Reset" button. If `isStarted` is `false`, render a "Start Quiz" button.
10. Export the `Quiz` component as the default export of the module.

### Parent App Component

```js
import "./App.css";

import HowToPlay from "./HowToPlay";
import ScoreCounter from "./ScoreCounter";
import Timer from "./Timer";
import Table from "./Rank";
import PremierLeagueTable from "./Rank/index2";
import Quiz from "./Quiz";

import { useState, useEffect } from "react";

function App() {
  const [hasQuizStarted, updateHasQuizStarted] = useState(null);

  function startTimer(status) {
    updateHasQuizStarted(status);
  }

  const time = new Date();
  time.setSeconds(time.getSeconds() + 300);
  return (
    <div className="App">
      <h1>Can you name the players with 100 Premier League goals?</h1>
      <HowToPlay></HowToPlay>
      <div className="place_edges">
        <ScoreCounter></ScoreCounter>
        <Timer expiryTimestamp={time} shouldTimerStart={hasQuizStarted}></Timer>
      </div>
      <Quiz trigger={startTimer}></Quiz>
      <PremierLeagueTable trigger={hasQuizStarted}></PremierLeagueTable>
    </div>
  );
}

export default App;

```

React application that renders a quiz for Premier League players with 100 goals. The application includes components for displaying instructions, keeping track of the score and time, and rendering the quiz and the Premier League player table.

The startTimer function is passed as a prop to the Quiz component, which is called when the user starts the quiz. This updates the state of the hasQuizStarted variable, which is then passed to the Timer and PremierLeagueTable components to start the timer and render the player table.

## Further Reading

Conditional rendering is an important concept in React that allows you to render different content based on a certain condition. Here are some resources that can help you further understand conditional rendering in React:

1. Official React documentation on conditional rendering: [https://react.dev/learn/conditional-rendering](https://react.dev/learn/conditional-rendering)
2. "Conditional Rendering in React" by Robin Wieruch: [https://www.robinwieruch.de/conditional-rendering-react](https://www.robinwieruch.de/conditional-rendering-react)

