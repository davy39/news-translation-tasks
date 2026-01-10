---
title: How to Learn JavaScript Promises and Async/Await in 20 Minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-01T01:38:27.000Z'
originalURL: https://freecodecamp.org/news/learn-promise-async-await-in-20-minutes
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/maxresdefault.jpg
tags:
- name: async/await
  slug: asyncawait
- name: JavaScript
  slug: javascript
- name: projects
  slug: projects
- name: promises
  slug: promises
seo_title: null
seo_desc: 'By Thu Nghiem

  On the web, many things tend to be time-consuming – if you query an API, it can
  take a while to receive a response. Therefore, asynchronous programming is an essential
  skill for developers.

  When working with asynchronous operations in J...'
---

By Thu Nghiem

On the web, many things tend to be time-consuming – if you query an API, it can take a while to receive a response. Therefore, asynchronous programming is an essential skill for developers.

When working with asynchronous operations in JavaScript, we often hear the term `Promise`. But it can be tricky to understand how they work and how to use them.

Unlike many traditional coding tutorials, in this tutorial we'll learn by doing. We'll complete four tasks by the end of the article:

* Task 1: Promise basics explained using my birthday
* Task 2: Build a guessing game
* Task 3: Fetch country info from an API
* Task 4: Fetch a country's neighboring countries

If you want to follow along, be sure to download the resources here: [https://bit.ly/3m4bjWI](https://bit.ly/3m4bjWI)

%[https://youtu.be/J29jeuyMJ38]

## Task 1: Promise basics explained using my birthday

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/z51d1v0jf07b43bfhfuu.gif)

My friend Kayo promises to make a cake for my birthday in two weeks.

If everything goes well and Kayo doesn't get sick, we'll have a certain number of cakes. (Cakes are a countable in this tutorial 😆). Otherwise, if Kayo gets sick, we'll have no cakes.

Either way, we're still going to have a party.

For this first task, we'll translate this story into code. First, let's create a function that returns a `Promise`:

```js
const onMyBirthday = (isKayoSick) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (!isKayoSick) {
        resolve(2);
      } else {
        reject(new Error("I am sad"));
      }
    }, 2000);
  });
};
```

In JavaScript, we can create a new `Promise` with `new Promise()`, which takes in a function as an argument: `(resolve, reject) => {}`. 

In this function, `resolve` and `reject` are callback functions that are provided by default in JavaScript.

Let's take a closer look at the code above.

When we run the `onMyBirthday` function, after `2000ms`:

* If Kayo is not sick, then we run `resolve` with `2` as the argument
* If Kayo is sick then we run `reject` with `new Error("I am sad")` as the argument. Even though you can pass anything to `reject` as an argument, it's recommended to pass it an `Error` object.

Now, because `onMyBirthday()` returns a `Promise`, we have access to the `then`, `catch`, and `finally` methods. 

And we also have access to the arguments that were passed into `resolve` and `reject` earlier within `then` and `catch`.

Let's take a closer look at the code.

If Kayo is not sick:

```js
onMyBirthday(false)
  .then((result) => {
    console.log(`I have ${result} cakes`); // In the console: I have 2 cakes  
  })
  .catch((error) => {
    console.log(error); // Does not run
  })
  .finally(() => {
    console.log("Party"); // Shows in the console no matter what: Party
  });

```

If Kayo is sick:

```js
onMyBirthday(true)
  .then((result) => {
    console.log(`I have ${result} cakes`); // does not run 
  })
  .catch((error) => {
    console.log(error); // in console: Error: I am sad
  })
  .finally(() => {
    console.log("Party"); // Shows in the console no matter what: Party
  });

```

Alright, so by now, I hope you get the basic idea of `Promise`. Let's move onto task 2.

## Task 2: Build a guessing game

The requirements:

* User story: A user can enter a number
* User story: The system picks a random number from 1 to 6
* User story: If the user's number is equal to a random number, give the user 2 points
* User story: If the user's number is different than the random number by 1,  
give the user 1 point. Otherwise, give the user 0 points
* User story: The user can play the game as long as they want to

For the first 4 user stories, let's create an `enterNumber` function and return a `Promise`:

```js
const enterNumber = () => {
  return new Promise((resolve, reject) => {
    // Let's start from here
  });
};
```

The first thing we need to do is to ask for a number from user and pick a random number between 1 and 6:

```js
const enterNumber = () => {
  return new Promise((resolve, reject) => {
    const userNumber = Number(window.prompt("Enter a number (1 - 6):")); // Ask the user to enter a number
    const randomNumber = Math.floor(Math.random() * 6 + 1); // Pick a random number between 1 and 6
  });
};

```

Now, `userNumber` can enter a value, that is not a number. If so, let's call the `reject` function with an error:

```js
const enterNumber = () => {
  return new Promise((resolve, reject) => {
    const userNumber = Number(window.prompt("Enter a number (1 - 6):")); // Ask user to enter a number
    const randomNumber = Math.floor(Math.random() * 6 + 1); // Pick a random number between 1 and 6

    if (isNaN(userNumber)) {
      reject(new Error("Wrong Input Type")); // If the user enters a value that is not a number, run reject with an error
    }
  });
};

```

The next thing we want to do is to check if the `userNumber` is equal to `randomNumber`, if so, we want give user 2 points and we can run the `resolve` function passing an object `{ points: 2, randomNumber }`. Notice here that we also want to know the `randomNumber` when the Promise is resolved

If the `userNumber` is different than `randomNumber` by one, then we give the user 1 point. Otherwise, we give the user 0 points:

```js
return new Promise((resolve, reject) => {
  const userNumber = Number(window.prompt("Enter a number (1 - 6):")); // Ask the user to enter a number
  const randomNumber = Math.floor(Math.random() * 6 + 1); // Pick a random number between 1 and 6

  if (isNaN(userNumber)) {
    reject(new Error("Wrong Input Type")); // If the user enters a value that is not a number, run reject with an error
  }

  if (userNumber === randomNumber) {
    // If the user's number matches the random number, return 2 points
    resolve({
      points: 2,
      randomNumber,
    });
  } else if (
    userNumber === randomNumber - 1 ||
    userNumber === randomNumber + 1
  ) {
    // If the user's number is different than the random number by 1, return 1 point
    resolve({
      points: 1,
      randomNumber,
    });
  } else {
    // Else return 0 points
    resolve({
      points: 0,
      randomNumber,
    });
  }
});
```

Alright, let's also create another function to ask if the user wants to continue the game:

```js
const continueGame = () => {
  return new Promise((resolve) => {
    if (window.confirm("Do you want to continue?")) { // Ask if the user want to continue the game with a confirm modal
      resolve(true);
    } else {
      resolve(false);
    }
  });
};

```

Notice here that we create a `Promise`, but it does not use the `reject` callback. This is totally fine.

Now let's create a function to handle the guess:

```js
const handleGuess = () => {
  enterNumber() // This returns a Promise
    .then((result) => {
      alert(`Dice: ${result.randomNumber}: you got ${result.points} points`); // When resolve is run, we get the points and the random number 
      
      // Let's ask the user if they want to continue the game
      continueGame().then((result) => {
        if (result) {
          handleGuess(); // If yes, we run handleGuess again
        } else {
          alert("Game ends"); // If no, we show an alert
        }
      });
    })
    .catch((error) => alert(error));
};

handleGuess(); // Run handleGuess function

```

Here when we call `handleGuess`, `enterNumber()` now returns a `Promise`:

* If the `Promise` is resolved, we call the `then` method and show an alert message. We also ask if the user wants to continue.
* If the `Promise` is rejected, we show an alert message with the error.

As you can see, the code is quite difficult to read.

Let's refactor the `handleGuess` function a bit using the `async/await` syntax:

```js
const handleGuess = async () => {
  try {
    const result = await enterNumber(); // Instead of the then method, we can get the result directly by just putting await before the promise

    alert(`Dice: ${result.randomNumber}: you got ${result.points} points`);

    const isContinuing = await continueGame();

    if (isContinuing) {
      handleGuess();
    } else {
      alert("Game ends");
    }
  } catch (error) { // Instead of catch method, we can use the try, catch syntax
    alert(error);
  }
};

```

You can see that we created an `async` function by putting `async` before the brackets. Then in the `async` function:

* Instead of the `then` method, we can get the results directly just by putting `await` before the promise
* Instead of the `catch` method, we can use the `try, catch` syntax

Here's all the code for this task again for your reference:

```js
const enterNumber = () => {
  return new Promise((resolve, reject) => {
    const userNumber = Number(window.prompt("Enter a number (1 - 6):")); // Ask the user to enter a number
    const randomNumber = Math.floor(Math.random() * 6 + 1); // Pick a random number between 1 and 6

    if (isNaN(userNumber)) {
      reject(new Error("Wrong Input Type")); // If the user enters a value that is not a number, run reject with an error
    }

    if (userNumber === randomNumber) { // If the user's number matches the random number, return 2 points
      resolve({
        points: 2,
        randomNumber,
      });
    } else if (
      userNumber === randomNumber - 1 ||
      userNumber === randomNumber + 1
    ) { // If the user's number is different than the random number by 1, return 1 point
      resolve({
        points: 1,
        randomNumber,
      });
    } else { // Else return 0 points
      resolve({
        points: 0,
        randomNumber,
      });
    }
  });
};

const continueGame = () => {
  return new Promise((resolve) => {
    if (window.confirm("Do you want to continue?")) { // Ask if the user want to continue the game with a confirm modal
      resolve(true);
    } else {
      resolve(false);
    }
  });
};

const handleGuess = async () => {
  try {
    const result = await enterNumber(); // Instead of the then method, we can get the result directly by just putting await before the promise

    alert(`Dice: ${result.randomNumber}: you got ${result.points} points`);

    const isContinuing = await continueGame();

    if (isContinuing) {
      handleGuess();
    } else {
      alert("Game ends");
    }
  } catch (error) { // Instead of catch method, we can use the try, catch syntax
    alert(error);
  }
};

handleGuess(); // Run handleGuess function

```

Alright, we are done with the second task. Let's move on to the third one.

## Task 3: Fetch country info from [an API](https://restcountries.eu/)

You'll see `Promises` used a lot when fetching data from an API.

If you open [https://restcountries.eu/rest/v2/alpha/col](https://restcountries.eu/rest/v2/alpha/col) in a new browser, you will see the country data in JSON format.  
  
By using the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch), we can fetch the data by:

```js
const fetchData = async () => {
  const res = await fetch("https://restcountries.eu/rest/v2/alpha/col"); // fetch() returns a promise, so we need to wait for it

  const country = await res.json(); // res is now only an HTTP response, so we need to call res.json()

  console.log(country); // Columbia's data will be logged to the dev console
};

fetchData();


```

Now that we have the country data we want, let's move onto the last task.

## Task 4: Fetch a country's neighboring countries

If you open task 4, you will see that we have a `fetchCountry` function, that fetches the data from the endpoint: `https://restcountries.eu/rest/v2/alpha/${alpha3Code}` where `alpha3code` is the code of the country.  
  
You also see that it will catch any `error` that might happen when getting the data.

```js
// Task 4: get the neigher countries of Columbia

const fetchCountry = async (alpha3Code) => {
  try {
    const res = await fetch(
      `https://restcountries.eu/rest/v2/alpha/${alpha3Code}`
    );

    const data = await res.json();

    return data;
  } catch (error) {
    console.log(error);
  }
};

```

Let's create a `fetchCountryAndNeighbors` function and fetch Columbia's information by passing `col` as the `alpha3code`.

```js
const fetchCountryAndNeighbors = async () => {
  const columbia = await fetchCountry("col");

  console.log(columbia);
};

fetchCountryAndNeighbors();

```

Now, if you look in your console, you can see an object look like this:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/35vkx7gewawg05wfcmni.png)

In the object, there is a `border` property which is a list of `alpha3codes` for Columbia's neighboring countries.

Now if we try to get the neighboring countries by:

```js
  const neighbors = 
    columbia.borders.map((border) => fetchCountry(border));

```

Then, `neighbors` will be an array of `Promise` objects.

When working with an array of promises, we need to use `Promise.all`:

```js
const fetchCountryAndNeigbors = async () => {
  const columbia = await fetchCountry("col");

  const neighbors = await Promise.all(
    columbia.borders.map((border) => fetchCountry(border))
  );

  console.log(neighbors);
};

fetchCountryAndNeigbors();

```

In the `console`, we should be able to see list of country objects.

Here's all the code for task 4 again for your reference:

```js
const fetchCountry = async (alpha3Code) => {
  try {
    const res = await fetch(
      `https://restcountries.eu/rest/v2/alpha/${alpha3Code}`
    );

    const data = await res.json();

    return data;
  } catch (error) {
    console.log(error);
  }
};

const fetchCountryAndNeigbors = async () => {
  const columbia = await fetchCountry("col");

  const neighbors = await Promise.all(
    columbia.borders.map((border) => fetchCountry(border))
  );

  console.log(neighbors);
};

fetchCountryAndNeigbors();

```

## Conclusion

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/34m9mus03v2zo9agn2bq.png)

After completing these 4 tasks, you can see that `Promise` is useful when it comes to asynchronous actions or things that are not happening at the same time.

You can see this in practice in one of my tutorials, where we build an application from scratch with React and Next.js:

%[https://youtu.be/v8o9iJU5hEA]

## __________ 🐣 About me __________

* I am the founder of [DevChallenges](https://devchallenges.io/)
* Subscribe to my [YouTube Channel](https://www.youtube.com/channel/UCmSmLukBF--YrKZ2g4akYAQ?sub_confirmation=1)
* Follow me on [Twitter](https://twitter.com/thunghiemdinh)
* Join [Discord](https://discord.com/invite/3R6vFeM)

