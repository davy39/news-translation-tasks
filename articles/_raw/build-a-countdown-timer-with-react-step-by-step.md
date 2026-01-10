---
title: How to Build a Countdown Timer with React – A Step-by-Step Guide
subtitle: ''
author: Franklin Ohaegbulam
co_authors: []
series: null
date: '2024-10-14T13:38:55.761Z'
originalURL: https://freecodecamp.org/news/build-a-countdown-timer-with-react-step-by-step
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1724788718279/35a8ba3c-db35-49b6-ae41-14bcda547795.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: reactjs
- name: Web Development
  slug: web-development
- name: Tutorial
  slug: tutorial
- name: ReactHooks
  slug: reacthooks
seo_title: null
seo_desc: 'In this tutorial, you will learn how to build a custom countdown timer
  to track events using React.js.

  A countdown timer is a simple way to measure the time until an event happens. It
  counts down that time in reverse – like 5, 4, 3, 2, 1. It helps yo...'
---

In this tutorial, you will learn how to build a custom countdown timer to track events using React.js.

A countdown timer is a simple way to measure the time until an event happens. It counts down that time in reverse – like 5, 4, 3, 2, 1. It helps you manage the time leading up to upcoming events, product launches, or offers, and allows you to inform users about that timeline.

### Table of Contents

* [1\. Set Up Your React App](#heading-1-set-up-your-react-app)
    
* [2\. Create the Count Down Component](#heading-2-create-the-count-down-component)
    
* [3\. Implement Time State Management and Functionality](#heading-3-implement-time-state-management-and-functionality)
    
* [4\. Create a Countdown Form](#heading-4-create-a-countdown-form)
    
* [5\. Handle the Countdown Start, Stop, and Reset Functionality](#heading-5-handle-the-countdown-start-stop-and-reset-functionality)
    
* [6\. Format the Event Date and Time](#heading-6-format-the-event-date-and-time)
    
* [7\. Display the CountDown Timer](#heading-7-display-the-countdown-timer)
    
* [8\. Styling the Countdown Timer Component](#heading-8-styling-the-countdown-timer-component)
    
* [Conclusion](#heading-conclusion)
    

### Prerequisites

You should have decent knowledge of HTML, CSS, and JavaScript to get the most out of this article.

Let's get started.

## 1\. Set Up Your React App

First, you’ll need to [create a React application](https://www.freecodecamp.org/news/how-to-build-a-react-app-different-ways/#heading-what-is-vite) if you don’t already have one ready to use. In this tutorial, I’m using Vite. Then change into the new project directory by running the following commands in your code editor:

```bash
npm create vite countdown-timer

cd countdown-timer
```

Run this command to start the app on the local server:

```bash
npm run dev
```

Now, you should see the project in your browser on `https://localhost/3000`.

## 2\. Create the Count Down Component

In the `src` folder of your React app, create a `components` directory, and inside it, create a `CountDown.jsx` file.

```javascript
/* components/CountDown.jsx */

import React from "react";

const CountdownTImer = () => {

  return (
    <div className="countdown-timer-container">
    </div>
  );
};

export default CountdownTimer;
```

## 3\. Implement Time State Management and Functionality

Define the state variables using the useState hook. Update the `CountDown.jsx` file with the following code:

```javascript
/* components/CountDown.jsx */

import React, { useState, useEffect } from "react";

const CountdownTimer = () => {
  const [eventName, setEventName] = useState("");
  const [eventDate, setEventDate] = useState("");
  const [countdownStarted, setCountdownStarted] = useState(false);
  const [timeRemaining, setTimeRemaining] = useState(0);

 return (
    <div className="countdown-timer-container">
    </div>
  );
};

export default CountdownTimer;
```

Here's a brief breakdown of the `useState`:

* `eventName`: stores the name of the event for the countdown timer.
    
* `eventDate`: stores the date of the event for the countdown timer.
    
* `countdownStarted`: tracks whether the countdown timer has started.
    
* `timeRemaining`: stores the remaining time in milliseconds for the countdown.
    

Now, we’ll implement the functionality of the countdown timer using the useEffect hook:

```javascript
/* components/CountDown.jsx */

import React, { useState, useEffect } from "react";

const CountdownTimer = () => {
  
    // ...

  useEffect(() => {
    if (countdownStarted && eventDate) {
      const countdownInterval = setInterval(() => {
        const currentTime = new Date().getTime();
        const eventTime = new Date(eventDate).getTime();
        let remainingTime = eventTime - currentTime;

        if (remainingTime <= 0) {
          remainingTime = 0;
          clearInterval(countdownInterval);
          alert("Countdown complete!");
        }

        setTimeRemaining(remainingTime);
      }, 1000);

      return () => clearInterval(countdownInterval);
    }
  }, [countdownStarted, eventDate, timeRemaining]);

 return (
    <div className="countdown-timer-container">
    </div>
  );
};

export default CountdownTimer;
```

The `useEffect` hook runs whenever `countdownStarted` or `eventDate` changes. It sets up an interval that updates `timeRemaining` every second based on the current time and event time. If the remaining time becomes less than or equal to 0, it stops the interval and triggers the notification "Countdown complete!"

```javascript
/* components/CountDown.jsx */

import React, { useState, useEffect } from "react";

const CountdownTimer = () => {
 
  // ...
  
  useEffect(() => {
    if (countdownStarted) {
      document.title = eventName;
    }
  }, [countdownStarted, eventName]);

 return (
    <div className="countdown-timer-container">
    </div>
  );
};

export default CountdownTimer;
```

Here, the `useEffect` hook runs whenever `countdownStarted` or `eventName` changes. It updates the countdown timer title to display the `eventName` when the countdown timer is started.

## 4\. Create a Countdown Form

To have control over the countdown timer, you’ll need to create a form with two inputs for the name and date of the event. Then, add the following code:

```javascript
/* components/CountDown.jsx */

import React from "react";

 // ...
 
   const handleSetCountdown = () => {
    setCountdownStarted(true);
  };

 return (
 <div className="countdown-timer-container">
      <h2 className="countdown-name">
        {countdownStarted ? eventName : "Countdown Timer"}
      </h2>

      {!countdownStarted ? (
        <form className="countdown-form">
          <label htmlFor="title">Event Name</label>
          <input
            name="title"
            type="text"
            placeholder="Enter event name"
            value={eventName}
            onChange={(e) => setEventName(e.target.value)}
          />

          <label htmlFor="date-picker">Event Date</label>
          <input
            name="date-picker"
            type="date"
            value={eventDate}
            onChange={(e) => setEventDate(e.target.value)}
            onClick={(e) => (e.target.type = "date")}
          />
          <button onClick={handleSetCountdown}>Start Countdown</button>
        </form>
      }
    </div>
  );
};

export default CountdownTimer;
```

Here's a brief breakdown of the `useState`:

* `eventName`: stores the name of the event for the countdown timer.
    
* `countdown-name`: displays the "Countdown Timer" by default or updates to the  `eventName` entered once the countdown has started.
    

The form includes:

* The input field with the name `title` and label `Event Name` update the `eventName` state value.
    
* The input field with the name `date-picker` allow users to select a date and control the  `eventDate` state value.
    
* The button `Start Countdown` triggers the `handleSetCountdown` function when clicked to initiate the countdown.
    

## 5\. Handle the Countdown Start, Stop, and Reset Functionality

Next, update the `handleSetCountdown` function to store the event name and date in the local storage using `localStorage.setItem`. localStorage is a web API that enables users to store data as key-value pairs persistently, even when the browser is closed or refreshed.

The code is as follows:

```javascript
/* components/CountDown.jsx */

import React from "react";

 // ...
 
    const handleSetCountdown = () => {
    setCountdownStarted(true);
    localStorage.setItem("eventDate", eventDate);
    localStorage.setItem("eventName", eventName);
  };

 return (
 <div className="countdown-timer-container">
       // ...
 </div>
  );
};

export default CountdownTimer;
```

Now, create the `handleStopCountdown` and `handleResetCountdown` functions to stop the countdown timer by updating the `countdownStarted` state to `false`.

```javascript
/* components/CountDown.jsx */

import React from "react";

 // ...

  const handleStopCountdown = () => {
    setCountdownStarted(false);
    setTimeRemaining(0);
  };

  const handleResetCountdown = () => {
    setCountdownStarted(false);
    setEventDate("");
    setEventName("");
    setTimeRemaining(0);
    localStorage.removeItem("eventDate");
    localStorage.removeItem("eventName");
  };

 return (
 <div className="countdown-timer-container">
       // ...
       <div className="control-buttons">
            <button onClick={handleStopCountdown}>Stop</button>
            <button onClick={handleResetCountdown}>Reset</button>
        </div>
 </div>
  );
};

export default CountdownTimer;
```

Here:

* `handleStopCountdown`: resets the `timeRemaining` state to zero.
    
* `handleResetCountdown`: resets the countdown timer to its initial state. It clears the remaining time states and removes the event date and event name from local storage using `localStorage.removeItem()`.
    

## 6\. Format the Event Date and Time

Let's convert date and time data into a readable format.

```javascript
/* components/CountDown.jsx */

import React from "react";

 // ...
 
  const formatDate = (date) => {
    const options = { month: "long", day: "numeric", year: "numeric" };
    return new Date(date).toLocaleDateString("en-US", options);
  };

  const formatTime = (time) => {
    const seconds = Math.floor((time / 1000) % 60);
    const minutes = Math.floor((time / (1000 * 60)) % 60);
    const hours = Math.floor((time / (1000 * 60 * 60)) % 24);
    const days = Math.floor(time / (1000 * 60 * 60 * 24));

    return (
      <div className="countdown-display">
        <div className="countdown-value">
          {days.toString().padStart(2, "0")} <span>days</span>
        </div>
        <div className="countdown-value">
          {hours.toString().padStart(2, "0")} <span> hours</span>
        </div>
        <div className="countdown-value">
          {minutes.toString().padStart(2, "0")} <span>minutes</span>
        </div>
        <div className="countdown-value">
          {seconds.toString().padStart(2, "0")} <span>seconds</span>
        </div>
      </div>
    );
  };

 return (
 <div className="countdown-timer-container">
       // ...
 </div>
  );
};

export default CountdownTimer;
```

Here's a brief breakdown of the functions:

* `formatDate`: formats the date input into a human-readable date string.
    
* `formatTime`: takes a time in milliseconds as input and calculates the days, hours, minutes, and seconds of the timer. The `.toString().padStart(2, "0")` returns the formatted time as two characters by appending 0 at the beginning of the time only if the length of the number is less than 2.
    

Here are the complete contents of the `CountDown.jsx` file:

```javascript
 /* components/CountDown.jsx */

import React, { useState, useEffect } from "react";

const CountdownTimer = () => {
  const [eventName, setEventName] = useState("");
  const [eventDate, setEventDate] = useState("");
  const [countdownStarted, setCountdownStarted] = useState(false);
  const [timeRemaining, setTimeRemaining] = useState(0);

  useEffect(() => {
    if (countdownStarted && eventDate) {
      const countdownInterval = setInterval(() => {
        const currentTime = new Date().getTime();
        const eventTime = new Date(eventDate).getTime();
        let remainingTime = eventTime - currentTime;

        if (remainingTime <= 0) {
          remainingTime = 0;
          clearInterval(countdownInterval);
          alert("Countdown complete!");
        }

        setTimeRemaining(remainingTime);
      }, 1000);

      return () => clearInterval(countdownInterval);
    }
  }, [countdownStarted, eventDate, timeRemaining]);

  useEffect(() => {
    if (countdownStarted) {
      document.title = eventName;
    }
  }, [countdownStarted, eventName]);

  const handleSetCountdown = () => {
    setCountdownStarted(true);
    localStorage.setItem("eventDate", eventDate);
    localStorage.setItem("eventName", eventName);
  };

  const handleStopCountdown = () => {
    setCountdownStarted(false);
    setTimeRemaining(0);
  };

  const handleResetCountdown = () => {
    setCountdownStarted(false);
    setEventDate("");
    setEventName("");
    setTimeRemaining(0);
    localStorage.removeItem("eventDate");
    localStorage.removeItem("eventName");
  };

  const formatDate = (date) => {
    const options = { month: "long", day: "numeric", year: "numeric" };
    return new Date(date).toLocaleDateString("en-US", options);
  };

  const formatTime = (time) => {
    const seconds = Math.floor((time / 1000) % 60);
    const minutes = Math.floor((time / (1000 * 60)) % 60);
    const hours = Math.floor((time / (1000 * 60 * 60)) % 24);
    const days = Math.floor(time / (1000 * 60 * 60 * 24));

    return (
      <div className="countdown-display">
        <div className="countdown-value">
          {days.toString().padStart(2, "0")} <span>days</span>
        </div>
        <div className="countdown-value">
          {hours.toString().padStart(2, "0")} <span> hours</span>
        </div>
        <div className="countdown-value">
          {minutes.toString().padStart(2, "0")} <span>minutes</span>
        </div>
        <div className="countdown-value">
          {seconds.toString().padStart(2, "0")} <span>seconds</span>
        </div>
      </div>
    );
  };

  return (
    <div className="countdown-timer-container">
      <h2 className="countdown-name">
        {countdownStarted ? eventName : "Countdown Timer"}
      </h2>
      <p className="countdown-date">
        {countdownStarted && formatDate(eventDate)}
      </p>

      {!countdownStarted ? (
        <form className="countdown-form">
          <label htmlFor="title">Event Name</label>
          <input
            name="title"
            type="text"
            placeholder="Enter event name"
            value={eventName}
            onChange={(e) => setEventName(e.target.value)}
          />

          <label htmlFor="date-picker">Event Date</label>
          <input
            name="date-picker"
            type="date"
            value={eventDate}
            onChange={(e) => setEventDate(e.target.value)}
            onClick={(e) => (e.target.type = "date")}
          />
          <button onClick={handleSetCountdown}>Start Countdown</button>
        </form>
      ) : (
        <>
          {formatTime(timeRemaining)}
          <div className="control-buttons">
            <button onClick={handleStopCountdown}>Stop</button>
            <button onClick={handleResetCountdown}>Reset</button>
          </div>
        </>
      )}
    </div>
  );
};

export default CountdownTimer;
```

## 7\. Display the CountDown Timer

Import `CountDownTimer` in the `App.jsx`, replacing the default code with this:

```javascript
 /* App.jsx */

import React from "react";
import CountdownTimer from "./components/CountDown";

function App() {
  return (
    <div className="App">
      <CountdownTimer />
    </div>
  );
}

export default App;
```

And that's it! Your countdown timer app should be rendered on  `localhost:3000` in the browser.

## 8\. Styling the Countdown Timer Component

Lastly, update the `index.css` file in the same directory of your project by adding the following styles:

```css
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Open+Sans:wght@400;500;700&display=swap");

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  background: url("./img/bg-img.jpg") top center;
  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: fixed;
  font-family: "Inter", sans-serif;
  font-size: 1rem;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  padding: 1rem;
}

.countdown-form {
  background-color: #f6f6f6;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 1.5rem;
  width: 100%;
  max-width: 400px;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

label {
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #333;
}

input {
  background-color: #d1f1ee;
  border: 1px solid #dfdfdf;
  border-radius: 6px;
  outline: none;
  margin-bottom: 1rem;
  padding: 0.75rem;
  width: 100%;
  font-size: 1rem;
  transition: border-color 0.2s ease;
}

input:focus {
  border-color: #038a7f;
}

button {
  background-color: #038a7f;
  border: none;
  border-radius: 6px;
  color: #fff;
  cursor: pointer;
  outline: none;
  margin-top: 1rem;
  text-transform: uppercase;
  width: 100%;
  height: 2.75rem;
  font-weight: 600;
  letter-spacing: 0.5px;
  transition: background-color 0.2s ease;
}

button:hover {
  background-color: #005a53;
}

.countdown-message {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: clamp(1.25rem, 4vw, 1.5rem);
  margin: 1rem 0;
}

.countdown-name {
  color: #fff;
  font-size: clamp(1.5rem, 5vw, 2rem);
  margin-bottom: 1rem;
  text-align: center;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

.countdown-date {
  color: #eafbfa;
  margin: 0 0 1.5rem;
  text-align: center;
  font-size: clamp(1rem, 3vw, 1.25rem);
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

.countdown-display {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(80px, 1fr));
  gap: 1rem;
  justify-content: center;
  padding: 0.5rem;
  max-width: 600px;
  margin: 0 auto;
}

.countdown-value {
  background-color: #2f5d6f;
  border-radius: 50%;
  color: #03d5c0;
  aspect-ratio: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 1rem;
  font-size: clamp(1.5rem, 5vw, 2.5rem);
  font-weight: 700;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
  transition: transform 0.2s ease;
}

.countdown-value:hover {
  transform: scale(1.05);
}

.countdown-value > span {
  color: #fff;
  font-size: clamp(0.75rem, 2vw, 0.875rem);
  letter-spacing: 1px;
  text-transform: uppercase;
  margin-top: 0.2rem;
  font-weight: 500;
}

.control-buttons {
  margin-top: 2rem;
  display: flex;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.control-buttons > button {
  background-color: #03b4a2;
  border-radius: 50%;
  width: clamp(45px, 8vw, 50px);
  height: clamp(45px, 8vw, 50px);
  margin: 0;
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: clamp(0.65rem, 2vw, 0.775rem);
}

.control-buttons button:hover {
  background-color: #0b7c71;
  transform: scale(1.1);
}

@media (max-width: 480px) {
  .countdown-display {
    grid-template-columns: repeat(2, 1fr);
    gap: 0.75rem;
  }

  .countdown-value {
    font-size: clamp(1.25rem, 4vw, 1.75rem);
  }

  .countdown-value > span {
    font-size: 0.75rem;
  }

  .control-buttons {
    margin-top: 1.5rem;
  }
}

@media (max-width: 360px) {
  body {
    padding: 0.75rem;
  }

  .countdown-form {
    padding: 1rem;
  }

  .countdown-name {
    font-size: 1.25rem;
  }

  .countdown-date {
    font-size: 1rem;
  }

  .control-buttons > button {
    width: 40px;
    height: 40px;
  }
}
```

Congratulations, you’ve finished building your Countdown timer app!

## Conclusion

In this article, you've learned how to build a basic React countdown timer app and how to work with the browser's local storage.

The code implemented in this article is accessible in this [GitHub repository](https://github.com/frankiefab100/countdown-timer). To learn more about web development and technology, check out my [blog](https://frankiefab.hashnode.dev/) or connect with me on [X(Twitter)](https://twitter.com/frankiefab100) and [LinkedIn](https://linkedin.com/in/frankiefab100/).

Thank you for reading.
