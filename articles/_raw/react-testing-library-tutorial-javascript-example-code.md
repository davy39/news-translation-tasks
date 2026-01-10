---
title: React Testing Library – Tutorial with JavaScript Code Examples
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2021-03-07T22:15:39.000Z'
originalURL: https://freecodecamp.org/news/react-testing-library-tutorial-javascript-example-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/react-testing-library-guide-1.png
tags: []
seo_title: null
seo_desc: 'This post will help you to learn what the React Testing Library is, and
  how you can use it to test your React application.

  This tutorial will assume you already know some basic JavaScript and understand
  the basics of how React works.

  React Testing Li...'
---

This post will help you to learn what the React Testing Library is, and how you can use it to test your React application.

This tutorial will assume you already know some basic JavaScript and understand the basics of how React works.

[React Testing Library](https://testing-library.com/docs/react-testing-library/intro) is a testing utility tool that's built to test the actual DOM tree rendered by React on the browser. The goal of the library is to help you write tests that resemble how a user would use your application. This can give you more confidence that your application works as intended when a real user does use it.

The library does this by providing utility methods that will query the DOM in the same way a user would. For example, a user would find a button to 'Save' their work by its text, so the library provides you with the `getByText()` method. You're going to learn more about the library's methods for testing later.

But first, let's see an example of React Testing Library in action.

## How to Use React Testing Library

A React application created with Create React App (or CRA) already includes both React Testing Library and Jest by default. So all you need to do is write your test code.

If you want to use React Testing Library outside of a CRA application, then you need to install both React Testing Library and Jest manually with NPM:

```shell
npm install --save-dev @testing-library/react jest
```

You need to install Jest because React Testing Library only provides methods to help you write the test scripts. So you still need a JavaScript test framework to run the test code. 

You can also use other test frameworks like Mocha or Jasmine, but I'm going to use Jest because it works well with both React and the Testing Library.

For this tutorial, I will create a new React application with CRA using the default template:

```shell
npx create-react-app react-test-example
```

Once the application is created, you should have an `App.test.js` file already generated inside the src/ folder. The content of the file would be as follows:

```javascript
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});

```

The test code above used React Testing Library's `render` method to virtually render the `App` component imported from `App.js` file and append it to the `document.body` node. You can access the rendered HTML through the `screen` object.

To see the result of the `render()` call, you can use the `screen.debug()` method:

```javascript
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  screen.debug();
});
```

Then open your terminal and run `npm run test` command. You'll see the whole `document.body` tree rendered into your console:

```html
<body>
  <div>
    <div class="App">
      <header class="App-header">
        <img alt="logo" class="App-logo" src="logo.svg" />
        <p>
          Edit<code> src/App.js </code>and save to reload.
        </p>
        <a
          class="App-link"
          href="https://reactjs.org"
          rel="noopener noreferrer"
          target="_blank"
        >
          Learn React
        </a>
      </header>
    </div>
  </div>
</body>
```

The `screen` object also has the DOM testing methods already bound into it. That's why the test code above could use `screen.getByText()` to query the anchor `<a>` element by its **textContent** value.

Finally, the test code will assert whether the link element is available in the `document` object or not with the `expect` method from Jest:

```javascript
expect(linkElement).toBeInTheDocument();
```

When the link element is not found, Jest will mark the test as **failed**.

## React Testing Library Methods for Finding Elements

Most of your React test cases should use methods for finding elements. React Testing Library provides you with several methods to find an element by specific attributes in addition to the `getByText()` method above:

* `getByText()`: find the element by its textContent value
* `getByRole()`: by its `role` attribute value
* `getByLabelText()`: by its `label` attribute value
* `getByPlaceholderText()`: by its `placeholder` attribute value
* `getByAltText()`: by its `alt` attribute value
* `getByDisplayValue()`: by its `value` attribute, usually for `<input>` elements
* `getByTitle()`: by its `title` attribute value

And when these methods are not enough, you can use the `getByTestId()` method, which allows you to find an element by its `data-testid` attribute:

```javascript
import { render, screen } from '@testing-library/react';

render(<div data-testid="custom-element" />);
const element = screen.getByTestId('custom-element');
```

But since selecting elements using `data-testid` attributes doesn't resemble how a real user would use your application, the documentation recommends you use it only as the last resort when all other methods fail to find your element. Generally, finding by Text, Role, or Label should cover most cases.

## How to Testing User Generated Events with React Testing Library

Aside from finding whether elements are present in your document body, React Testing Library also helps you test user generated events, like clicking on a button and typing values into a textbox.

The `user-event` library is companion library for simulating user-browser interaction. Suppose you have a button component to toggle between Light and Dark theme as follows:

```javascript
import React, { useState } from "react";

function App() {
  const [theme, setTheme] = useState("light");

  const toggleTheme = () => {
    const nextTheme = theme === "light" ? "dark" : "light";
    setTheme(nextTheme);
  };

  return <button onClick={toggleTheme}>
      Current theme: {theme}
    </button>;
}

export default App;

```

Next, you create a test that finds the button and simulates a click event by using the `userEvent.click()` method. Once the button is clicked, you can assert the test is a success by inspecting whether the button element text contains "dark" or not:

```javascript
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import App from "./App";

test("Test theme button toggle", () => {
  render(<App />);
  const buttonEl = screen.getByText(/Current theme/i);
    
  userEvent.click(buttonEl);
  expect(buttonEl).toHaveTextContent(/dark/i);
});
```

And that's how you can simulate user events with React Testing Library. The `user-event` library also has several other methods like `dblClick` for double clicking an element and `type` for typing into a textbox. You can checkout the [documentation for `user-event` library](https://testing-library.com/docs/ecosystem-user-event) for more info.

## Conclusion

> The more your tests resemble the way your software is used, the more confidence they can give you.   
> (Source: [Kent C.Dodds](https://twitter.com/kentcdodds/status/977018512689455106), React Testing Library Author)

A real user won't see the implementation details like what state or props are currently in your React components. They only see the rendered HTML elements on the browser. React Testing Library encourages you to test the behavior of your application instead of implementation details.

By testing your application the way a user would use it, you can be confident that your application will behave as expected when all test cases have passed. For more information, you can visit the [documentation for React Testing Library](https://testing-library.com/docs/react-testing-library/example-intro).

If you enjoyed this article and want to take your JavaScript skills to the next level, I recommend you check out my new book _Beginning Modern JavaScript_ [here](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

The book is designed to be easy to understand and accessible to anyone looking to learn JavaScript. It provides a step-by-step gentle guide that will help you understand how to use JavaScript to create a dynamic application.

Here's my promise: _You will actually feel like you understand what you're doing with JavaScript._

Until next time!




