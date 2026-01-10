---
title: A quick guide to test-driven development in React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-07T19:42:31.000Z'
originalURL: https://freecodecamp.org/news/quick-guide-to-tdd-in-react-81888be67c64
coverImage: https://cdn-media-1.freecodecamp.org/images/0*be_rcBa_vhJE6cVD.
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: null
seo_desc: 'By Michał Baranowski

  Following the principles of Test-Driven Development (TDD) when writing a front-end
  React app might seem more difficult than doing the same on the back-end.

  First, we need to somehow render our component. Then we need to simulate ...'
---

By Michał Baranowski

Following the principles of **Test-Driven Development** (TDD) when writing a front-end React app might seem more difficult than doing the same on the back-end.

First, we need to somehow **render** our component. Then we need to **simulate** user interaction with a browser. Next we respond to changes in **props** and **state,** and finally come up with a way to test **asynchronous** methods triggered by the click of a button.

Trying to cover all these cases in our tests often results in tests that are difficult to read. They also often depend on one another. We mock a lot, and in return we have tests full of anti-patterns.

### Don’t waste your time

From what I’ve seen, many programmers create working React components first.Then they try to cover them with tests, just to realize that the components cannot be tested in their current implementation. Then they need to refactor. Because of that they lose patience, time, and their employer’s money.

### Available solutions

Fortunately for us, there are many testing libraries that can help us address these problems. We can try rendering React components with [**Enzyme**](https://github.com/airbnb/enzyme) and mock API responses using [**MockAxios**](https://github.com/ctimmerm/axios-mock-adapter). However, these libraries usually have so many methods and options that it might get confusing, especially for people who have just started writing tests.

Let’s take **Enzyme** for example — what’s the difference between the **Shallow**, **Mount** and **Render** methods? And which should you use? This is not what you should be worried about when you write your tests, in my opinion. It should be as straight forward as possible.

### Our project

For our Quick Guide purposes, we’re going to create a small React app. After clicking on a button, a random joke about [Chuck Norris](https://pl.wikipedia.org/wiki/Chuck_Norris) will be fetched and displayed.

> No one has ever pair-programmed with Chuck Norris and lived to tell about it.

So let’s begin.

Kick-off by creating a React project in [**CodeSandbox**](https://codesandbox.io/s/new)**,** and then install the following dependencies (J**est** is already pre-installed if you started from the link above):

* [**axios**](https://github.com/axios/axios) — used for fetching data from the external API
* [**axios-mock-adapter**](https://github.com/ctimmerm/axios-mock-adapter) — used for mocking server responses
* [**react-testing-library**](https://github.com/kentcdodds/react-testing-library) — light, easy to use testing library for rendering, simulating actions, and handling async methods — created by [Kent C. Dodds](https://www.freecodecamp.org/news/quick-guide-to-tdd-in-react-81888be67c64/undefined)
* [**jest**](https://facebook.github.io/jest/) — for running the tests and creating assertions

#### Folder/files structure

* **src/index.js** — entry point for our React app
* **src/jokeGenerator.js** — our [container](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0) component which fetches, controls, and provides data
* **src/joke.js** — simple presentation component
* **src/__tests__/jokeGenerator.test.js** — contains our tests

#### Your first test

Each time before we create a component **we will write a failing test first and then try to make it pass**. Let’s start by writing a test for our dummy component **<Joke** /> which will render a text from props.

![Image](https://cdn-media-1.freecodecamp.org/images/Hex65Vqu6mUtqCS1F1-5mJDDes-ua5BSTSNK)
_jokeGenerator.test.js_

Reading from the top: we use a [render](https://github.com/kentcdodds/react-testing-library#render) method from the **react-testing-library** and pass the &**lt;Jok**e/> component (which does not exist at this point) into it. It returns an object containing a few very useful methods (find the full list of available me[thod](https://github.com/kentcdodds/react-testing-library#render)s here) — for ex**ample getBy**TestId. It then returns an HTML element bas**ed on data-t**estid as an argument.

Next, we write an **expect** using above method and **data-testid,** and check if the element contains the text from props. After running the tests, we get:

> Joke is not defined

Yep, we want it to fail! **<Joke** /> does not exist yet, remember? We have only created an _empty jo_ke.j_s_ file so far. We wrote a test in which we can clearly see what we expect the component to do. Now our job is to make the **test pass without modifying the tes**t code. Let’s do that then:

![Image](https://cdn-media-1.freecodecamp.org/images/lCi4BrSPyRaCkptSkuZQO3d7UaBoJ7CZa9ue)
_joke.js_

Now, if you did everything just like I did, the test should pass :)

#### Second component

Our second component will be responsible for fetching a random joke after a user clicks a button. We’ll save it in the component’s state and pass it down to our **<Joke** /> component. We would also like to display a default message when no joke has been loaded yet.

Of course, we start with test first. It is a bigger component, so we’ll be writing the test step-by-step. We’ll also make sure it is passing as often as possible.

![Image](https://cdn-media-1.freecodecamp.org/images/wZoc7qf8aDj-omViRiELm9UNsZ89RgibccoP)
_jokeGenerator.test.js_

We are already familiar with the **render** method, but this time we are taking **getByText** from the return object. As you might have guessed, the method returns an HTML Element if one exists in the DOM.

Run the tests and….

> JokeGenerator is not defined

You know what to do with it:

![Image](https://cdn-media-1.freecodecamp.org/images/Q5hr0EZ7poKO-fuA2kfkuSAo-nBiWpLSZPx5)
_jokeGenerator.js_

The test is still failing, but this time it outputs a different error:

> Unable to find an element with the text.

**You haven’t loaded any jokes yet**. This could be because the text is broken up by multiple elements. In this case, you can provide a function for your text matcher to make your matcher more flexible.

Let’s quickly fix that by introducing a **state** to our component and displaying a default message when there is no **joke** in the **state**.

![Image](https://cdn-media-1.freecodecamp.org/images/5RfACQ6NeneEtE4Fz9XHpysVjaBO4zO7a1A8)
_jokeGenerator.js_

Tests are passing now, so we can move on to add new functionality. Imagine that when we click on a button, the default text in the component disappears to make room for a “_Loading…_” message. Sounds pretty straightforward, right? We can test this scenario with only **three** lines of code!

Let’s import the **Simulate** method first, as we’re going to need that:

> import { render, Simulate } from “react-testing-library”

![Image](https://cdn-media-1.freecodecamp.org/images/gGK6Sfw3gmdLpdjyQqgZFRWYJe5kYXU88HlD)
_Append it to our second test — jokeGenerator.test.js_

The difference between **queryByText** and **getByText** is in what each one returns when the element is not found. The first one returns **null** and the second one throws an **error message**. Re-running the tests:

> Unable to find an element with the text: **Load a random joke**…

We need to create a button and set the **onClick** method which will set the **loading** state to **true**.

![Image](https://cdn-media-1.freecodecamp.org/images/uoGJiY5bC4-yyK5HpLuREFgnlSdavInme7rV)
_jokeGenerator.js_

Just like that the test is passing again. Now it’s time to fetch our random joke! Well… it won’t be random in our tests. We’ll mock it using **MockAxios**.

> import * as axios from "axios"  
> import MockAxios from “axios-mock-adapter”

Above our tests in **jokeGenerator.test.js,** insert these two lines of code:

![Image](https://cdn-media-1.freecodecamp.org/images/VA9ve3xfI5JUv-vznDWIHRIs7QEkl3ooEcJC)
_Insert above all tests — jokeGenerator.test.js_

The first line creates a new instance of **MockAxios** with a random delay. The second line takes and executes a callback function after running all the tests in this file, and removes the mocked state from **axios**.

At the top of our second test where we test the **<JokeGenerator** /> component, add:

![Image](https://cdn-media-1.freecodecamp.org/images/nSEIfJmjCd5aaTwFb0mEK9SrNp6zRwXvuzXV)
_Top of the second test — jokeGenerator.test.js_

It mocks the response of any **GET** call done via **axios**. At the end of the same test:

![Image](https://cdn-media-1.freecodecamp.org/images/Ssf6gSyjvVaJ4G1MtujRqjSq7whZIksqXnG3)
_jokeGenerator.test.js_

Don’t forget to import **wait**:

> import { render, Simulate, wait } from “react-testing-library”

The **wait** method waits (4500ms by default) until a callback function stops throwing an error. It is checked at 50ms intervals. Basically we’re just waiting until the loading message disappears from the DOM.

[**wait**](https://github.com/TheBrainFamily/wait-for-expect) is also available as a separate [npm package](https://github.com/TheBrainFamily/wait-for-expect) (**react-testing-library** uses it as a dependency). It was created by [Łukasz Gozda Gandecki](https://www.freecodecamp.org/news/quick-guide-to-tdd-in-react-81888be67c64/undefined).

After making all of the code modifications and running the tests, we should get the following fail message:

> Expected the element **not** to be present  
> Received : <div>Loading…</div>

What do you think it might be? According to our test, we expect the loading message to be gone. Additionally, we want to fetch our joke from the API and save it to the **state** so that next **expect** passes.

![Image](https://cdn-media-1.freecodecamp.org/images/RiBFROcMESY6up039OAXvaOtUb3vsReZWCM8)
_jokeGenerator.js_

![Image](https://cdn-media-1.freecodecamp.org/images/ZEaKt3f6itVBQb5lzlg2Vq0G2nMZd-48mLGv)
_Insert into render() method — jokeGenerator.js_

Tests should pass again now. We are sure that everything works as expected…aren’t we? Notice that we have **never opened our browser and verified manually if our app even works**…However, thanks to how we were writing our tests ([so that our tests resemble the way the user would use the application](https://twitter.com/kentcdodds/status/977018512689455106)), we can be almost 100% sure that our small app is simply working.

As the last piece of code, let’s add this to the index.js and open the browser :)

![Image](https://cdn-media-1.freecodecamp.org/images/PzjDJRbEJAjgV6qTqIzxIC8FRfXptZI2HnWO)
_index.js_

### Bonus

Because of the way we wrote our tests, we can utilize them as **e2e** tests **without adding a single line of code!** All we need to do is to remove all the lines related to **MockAxios** and run the tests again! They will now use a real external API. Cool, isn’t it? :)

### Summary

All the code is available on the project’s [**CodeSandbox**](https://codesandbox.io/s/6yq6v1xk3)**.** I really encourage you to get familiar with a full [**react-testing-library**](https://github.com/kentcdodds/react-testing-library) documentation. You’ll find there many more examples and use cases.

I hope you enjoyed my **Quick Guide to TDD in React,** and that you’ve learned something new today.

