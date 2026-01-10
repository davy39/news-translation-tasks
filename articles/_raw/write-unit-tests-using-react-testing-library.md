---
title: React Testing Library Tutorial – How to Write Unit Tests for React Apps
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2022-11-30T16:53:39.000Z'
originalURL: https://freecodecamp.org/news/write-unit-tests-using-react-testing-library
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/cover_testing.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: unit testing
  slug: unit-testing
seo_title: null
seo_desc: 'In this tutorial, you will learn how to confidently write unit tests using
  the Testing Library. It is a very popular React testing library for writing unit
  tests.

  So let''s get started.

  What We''ll Cover:


  Why Do You Need to Write Unit Tests?

  What is t...'
---

In this tutorial, you will learn how to confidently write unit tests using the [Testing Library](https://testing-library.com/). It is a very popular React testing library for writing unit tests.

So let's get started.

## What We'll Cover:

1. [Why Do You Need to Write Unit Tests?](#heading-why-do-you-need-to-write-unit-tests)
2. [What is the React Testing Library?](#heading-what-is-the-react-testing-library)
3. [What Not to Test with the Testing Library](#heading-what-not-to-test-with-the-testing-library)
4. [How to Setup a React Project with Vite](#heading-how-to-setup-a-react-project-with-vite)
5. [How to Set Up the Testing Library and Jest in a React Project](#heading-how-to-set-up-the-testing-library-and-jest-in-a-react-project)
6. [How to Create the UI for Testing](#heading-how-to-create-the-ui-for-testing)
7. [How to Write Unit Test Cases](#heading-how-to-write-unit-test-cases)
8. [Let's Write Some More Tests](#heading-lets-write-some-more-tests)
9. [Conclusion](#heading-conclusion)

If you want to learn the React Testing Library in depth from scratch, you can check out my [MERN stack course](https://online-elearning-platform.netlify.app/). 

## Why Do You Need to Write Unit Tests?

You might think that you don't need to write so many unit test cases and that it's a waste of time. Perhaps you can manually test the application instead.

Well, you're right – you can certainly do that. But as the application grows, it might be difficult to test all the scenarios in the application and you might miss something. Even a small change might break the application if all the major functionality is not tested properly.

That's why I recommend writing unit test cases covering all those scenarios which you're manually going through as a user.

So by executing just a single command you will be able to know if something is broken in your application or if some test is failing.

## What is the React Testing Library?

The React [Testing Library](https://testing-library.com/) has a set of packages that help you test UI components in a user-centric way. This means it tests based on how the user interacts with the various elements displayed on the page.

So what happens is when the user clicks any button or types in any of the input textboxes, that interaction is tested using this testing library.

So instead of the user doing this testing manually (which takes a lot of time, and the user might miss testing certain scenarios when the application grows), the testing is done by writing unit test cases and executing them by just a single command.

## What Not to Test with the Testing Library

Testing Library encourages you to avoid testing implementation details like the internals of a component you're testing.

The guiding principles of this library emphasize a focus on tests that closely resemble how users interact with your web pages.

You may want to avoid testing the following implementation details:

* Internal state of a component
* Internal methods of a component
* Lifecycle methods of a component
* Child components

So if you have experience with [enzyme testing](https://enzymejs.github.io/enzyme/), you might be checking the value of state once you click any button or you might be checking the prop value If something changes.

But these types of checks are not necessary for testing with the React testing library. Instead, in the React testing library, you check the behavior of the DOM when the user clicks on a button or submits a form and so on.

## How to Setup a React Project with Vite

To set up our app that we'll test, we'll be using [Vite](https://vitejs.dev/). It's a popular and faster alternative to [create-react-app](https://reactjs.org/docs/create-a-new-react-app.html).

We'll use Vite because `create-react-app` becomes slow when the application grows and takes a lot of time to refresh the page when we make any changes in the application code. Also, by default, it also adds a lot of extra packages which we rarely need.

Vite just rebuilds the things we changed, instead of rebuilding the entire application which saves a lot of time during development.

Keep in mind that Vite requires Node.js version 14.18+, so make sure to install a Node version greater than or equal to 14.18.

The easiest and simplest way to install and switch Node.js versions is to use [nvm](https://github.com/nvm-sh/nvm#installing-and-updating).

Even if you're using `create-react-app`, all the tests you will learn in this tutorial should run exactly the same without any errors.

To create a new Vite project with React, execute the `npm init vite` command from the terminal.

It will ask you the `project name`, `framework`, and `variant`.

* For `project name`, you can enter `testing-library-demo` or any name of your choice.
* For `framework`, select `React` from the list of options
* For `variant`, select `JavaScript` from the list of options

![Image](https://www.freecodecamp.org/news/content/images/2022/11/1_setup.gif)
_Create a new React project using Vite_

Once the project is created, you can open that project in your favorite IDE.

The project folder structure will look like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/2_folder_structure.png)
_Folder structure of React Vite project_

Now, execute the `yarn` or `npm install` command to install all the packages from the `package.json` file.

Once all the packages are installed, you can execute the `yarn run dev` or `npm run dev` command to start the created React application.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/3_app_started.png)
_Running a React app_

Now, if you access the displayed URL `http://127.0.0.1:5173/` you will be able to see the default React application created using Vite.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/4_app_loaded.png)
_Default React page rendered using Vite_

So let's see how we can set up the [Testing Library](https://testing-library.com/docs/) in our Vite project.

## How to Set Up the Testing Library and Jest in a React Project

You can't just use the testing library alone – you also need to install [Jest](https://jestjs.io/). It exposes an extensively used global expect function and other things which help you make assertions in your test cases.

To set up [Testing library](https://testing-library.com/) and [Jest](https://jestjs.io/), you need to install the Jest and Testing Library packages as dev dependencies.

So execute the following command from the `testing-library-demo` folder:

```js
yarn add @testing-library/jest-dom@5.16.5 @testing-library/react@13.4.0 @testing-library/user-event@14.4.3 jest@29.3.1 jest-environment-jsdom@29.3.1 vitest@0.25.3 --dev

```

or with npm:

```js
npm install @testing-library/jest-dom@5.16.5 @testing-library/react@13.4.0 @testing-library/user-event@14.4.3 jest@29.3.1 jest-environment-jsdom@29.3.1 vitest@0.25.3 --save-dev

```

I'm mentioning versions here for each package which are the latest versions at the time of writing this tutorial. So even if there is a newer breaking version release that happens for any of the packages in the future, your code will not break.

Here, we're installing the `jest-environment-jsdom` library because we will be running tests in the node environment. But we're testing browser interactions through the DOM – so to inform Jest about that, we need to add this library.

The `@testing-library/jest-dom` library is required because it contains assertions like `toBeInTheDocument`, `toHaveBeenCalled`, and others which make it easy to test for DOM elements, which you will see later in this tutorial.

We have also added the `vitest` package which is only required when you're using Vite for the application.

You don't need it if you're using `create-react-app` or your own webpack configuration.

Now that we have installed the required packages, let's add a script in the `package.json` file to run the tests.

Open the `package.json` file and add the `test` script inside it like this:

```js
"test": "vitest"

```

Your `package.json` file will look like this now:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/5_package_json.png)
_Package.json file preview_

If you're not using `vite` for creating the React app, then you will be using the following test script:

```js
"test": "jest --watch"

```

Now, create a new file in the root of your project (`testing-library-demo`) with the name `setupTests.js` and add the following code inside it:

```js
import "@testing-library/jest-dom";

```

Now, open the `vite.config.js` file and add a new `test` object as shown in the below screenshot:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/9_vite_config.png)
_vite.config.js file configuration_

## How to Create the UI for Testing

Before writing tests, we need to have some components to test.

So let's create a simple registration page with some checkboxes, input fields, select dropdown, and buttons so we can write test cases for it.

We will use [react-bootstrap](https://react-bootstrap.github.io/) to create the UI elements so we don't have to write all the CSS from scratch.

Install `bootstrap` and `react-bootstrap` by executing the following command from the terminal:

```js
yarn add bootstrap@5.2.3 react-bootstrap@2.6.0 react-select@5.6.1

```

or with npm:

```js
npm install bootstrap@5.2.3 react-bootstrap@2.6.0 react-select@5.6.1

```

Bootstrap provides a base CSS which we need for the UI to look nice, so we're also installing Bootstrap along with react-bootstrap.

Once installed, open `src/main.jsx` and add an import for the Bootstrap CSS file before any of your other CSS files as shown below:

```js
import "bootstrap/dist/css/bootstrap.min.css";

```

Your `src/main.jsx` file will look like this now:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/6_bootstrap_css.png)
_bootstrap css imported_

We don't need the `index.css` and `App.css` files so you can delete them.

Now, create a `components` folder inside the `src` folder and create a `register` folder inside the `components` folder. Inside the `register` folder, create `Register.jsx` and `register.css` files.

So your `Register.js` file path will be `src/components/register/Register.js`.

Add the content from [this repo](https://github.com/myogeshchavan97/testing-library-demo/blob/master/src/components/register/Register.jsx) in the `Register.jsx` file and inside `register.css` file add contents from [this repo](https://github.com/myogeshchavan97/testing-library-demo/blob/master/src/components/register/register.css).

Now, open the `App.jsx` file and add the following contents inside it:

```js
import Register from "./components/Register";

function App() {
  return <Register />;
}

export default App;

```

Now, if you run the application by executing the `yarn run dev` or `npm run dev` command, you will see the following screen:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/7_register_page.png)
_Registration page_

This tutorial is focused on the testing library, so I'm not going to explain the code from the `Register.js` file as it's basic React code. But If you're not familiar with React hooks, you can check out [this article](https://levelup.gitconnected.com/an-introduction-to-react-hooks-50281fd961fe?sk=89baff89ec8bc637e7c13b7554904e54) to understand it better.

Also, instead of managing the state and onChange handler yourself, you can use the very popular [react-hook-form](https://react-hook-form.com/) library.

It also allows you to add validations to your code without writing much code. Check out [this article](https://www.freecodecamp.org/news/how-to-create-forms-in-react-using-react-hook-form/) if you want to learn about it in detail.

Now, we're all set to write unit test cases, so let's get started.

## How to Write Unit Test Cases

Before writing test cases, you should be aware of the different queries which you can make to access elements on the page.

The Testing Library provides a set of queries which you can see in the below screenshot:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/8_queries.png)
_Screenshot showing getBy, queryBy, findBy, getAllBy, queryAllBy, and findAllBy queries. ([Source](https://testing-library.com/docs/queries/about))_

To summarise:

* To select a single DOM element, you can use the `getBy`, `findBy`, or `queryBy` query
* To select multiple DOM elements, you can use the `getAllBy`, `findAllBy` or `queryAllBy` query
* `getBy` and `findBy` return an error if there is no match or more than one match
* `queryBy` returns null if there is no match and returns an error if there is more than one match
* `findBy` works well with asynchronous code but not with `getBy` and `queryBy`
* `getAllBy` returns an error if there is no match and returns an array of matches for one or more than one match
* `findAllBy` returns an error if there is no match and returns an array of matches for one or more than one match
* `queryAllBy` returns an empty array for no match and returns an array of matches for one or more than one match

So if you don't want your test to fail if the element is not displayed on the UI, then always use `queryBy` or `queryAllBy`.

In other words, only use the `queryBy` or `queryAllBy` queries for asserting that an element cannot be found or is hidden.

Now that you're familiar with query methods, let's start writing test cases for the `Register` component.

Create a new `register.test.jsx` file in the `src/components/register` folder with the following content inside it:

```js
import { render, screen } from "@testing-library/react";
import Register from "./Register";

describe("Register component", () => {
  it("should render Register component correctly", () => {
    render(<Register />);
    const element = screen.getByRole("heading");
    expect(element).toBeInTheDocument();
  });
});

```

Note that we're using Vite so the filename has to end with the `.jsx` extension even for test files. If you're not using vite then you can end the filename with the `.js` extension.

Now, if you execute the `npm run test` or `yarn run test` command you will see that the test passes.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/1_test_result.png)
_one test passed_

In the above code, we're first rendering the `Register` component using the `render` method provided by the testing library.

As we have an h1 element with `Register` text in the `Register` component, we're using the `screen.getByRole` method to get the DOM element of the role `heading`.

If you don't know what role to use in the `getByRole` method, then you can use some random name and the testing library will show you all the available roles for each DOM element for that component as shown below:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/10_role.gif)
_Seeing the DOM structure of UI elements_

Once we get that element using the `getByRole` method, then we're making an assertion to check if that element exists in the DOM using:

```js
expect(element).toBeInTheDocument();

```

You can see a list of all available `getBy`,`findBy` or `queryBy` methods by adding a dot after `screen` like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/11_query_methods.gif)
_Methods provided by screen object_

Now, we have added one test to check if the `Register` component is getting rendered correctly or not.

Let's write some more tests.

If you run the application by running the `yarn dev` command, you will see that, once you click on the `Register` button without filling out all the details, you get an error message as shown below.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/12_error_message.gif)
_Error message display on submitting form without entering data_

So now, we need to test the same by writing a test case.

For that, we can use `userEvent` from the `@testing-library/user-event` package which we've already installed.

Now, add a new test in your `register.test.jsx` file as shown below:

```js
it("should show error message when all the fields are not entered", () => {
    render(<Register />);
    const buttonElement = screen.getByRole("button");
    userEvent.click(buttonElement);
});

```

Your `register.test.jsx` file will look like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/13_new_test.png)
_New test added for testing error message display_

So we're triggering the click event for the `Register` button in the above code.

Now, we need to find the element with the error message so we can add assertions for it in the test.

The error message is actually an `Alert` component from `react-bootstrap` which is not visible initially. It's only displayed when we submit the form without filling in all the data.

In such a case, we can call the `screen.debug` method to see the structure of the DOM at that moment when we trigger the click event.

So change the test case as shown below:

```js
it("should show error message when all the fields are not entered", async () => {
    render(<Register />);
    const buttonElement = screen.getByRole("button");
    userEvent.click(buttonElement);
    screen.debug();
});

```

Note that we have added `screen.debug` at the end of the test.

Now, if you run the `yarn run test` or `npm run test`, you will see the following DOM structure:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/14_debug_output.png)
_DOM structure when after submitting the Form_

As you can see from the screenshot, you directly see the name input label inside the form tag after the `Register` heading.

So we're not able to see the error message even if we have triggered the click event for the button.

This is because it takes some time to execute the validation code from the `handleFormSubmit` method. Before that we're only using the `screen.debug` method so we don't see the error message.

So to fix this, we can wait using async/await.

So declare the test function as `async` and before the `userEvent.click(buttonElement)` add an `await` keyword like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/15_await_event.png)
_Added async/await_

Now, if you check the console, you will be able to see the text `All the fields are required.` inside a div with the role `alert`.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/error_message_dom.png)
_Error message getting displayed in DOM structure_

So we can use it in our assertion like this:

```js
const alertElement = screen.getByRole("alert");
expect(alertElement).toBeInTheDocument();

```

And now, you can see that the second test is also successful.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/16_success_test.png)
_test passed_

Some points to note:

* Always remember to remove the `screen.debug` statement once you're done with your assertions, and never keep it in your code.
* Always add an `await` keyword before triggering any event using `userEvent` as you may not know when the action will be completed.

## Let's Write Some More Tests

Now that we're done with adding these two tests, we can add one more test to check if there is no error when the page is loaded like this:

```js
it("should not show any error message when the component is loaded", () => {
    render(<Register />);
    const alertElement = screen.getByRole("alert");
    expect(alertElement).not.toBeInTheDocument();
});

```

Here, instead of using this:

```js
expect(alertElement).toBeInTheDocument();

```

we're using this:

```js
expect(alertElement).not.toBeInTheDocument();

```

Because we want the alert element to be **not** present on the component load.

But if you check the console, you will see that the test is failing.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/17_failed_test.png)
_Failed test when using getByRole_

So, the test is not failing because of our assertion. Rather, it's failing because it can't find an element with role `alert` on page load which is expected, as there will not be any error on page load.

But how we can make the test pass?

If you remember from the list of queries in the screenshot shown before:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/8_queries-1.png)
_Screenshot showing getBy, queryBy, findBy, getAllBy, queryAllBy, and findAllBy queries._

The `getBy` method throws an error if it does not find the matching element. So instead of using `getBy` we need to use `queryBy`. It does the same thing but it does not throw an error when there is no matching element.

So let's modify our test case to the below code:

```js
it("should not show any error message when the component is loaded", async () => {
    render(<Register />);
    const alertElement = screen.queryByRole("alert");
    expect(alertElement).not.toBeInTheDocument();
});

```

Now, if you check the console, you will see that the test passes successfully.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/18_test_passed_query.png)
_Passed test when using queryByRole_

Now, let's write a test for successful registration when we fill out all the required fields.

```js
it("should show success message when the registration is successful.", async () => {
    render(<Register />);
    const buttonElement = screen.getByRole("button");
    await userEvent.click(buttonElement);
    const alertElement = screen.getByRole("alert");
    expect(alertElement).toBeInTheDocument();
});

```

Now if you see the console, you will see that the test passes successfully.

Let's add a subheading to the registration page and see what happens when we run the tests again.

Add the following heading inside the `Form` tag in the `Register.jsx` file:

```js
<h6 className="subtitle">
   Please enter your details below to register yourself.
</h6>

```

So your code will now look like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/20_subtitle.png)
_Added new subheading_

Now, if you run the tests again, you will see that one test fails:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/21_failed_multiple.png)
_Failed test due to multiple headings on the page_

The test failed because in the first test we're finding the `Register` heading text as shown below:

```js
screen.getByRole("heading")

```

And as you know, `getBy` returns an error when you have more than one match. 

Here, we have two headings on the `Register` component so the test failed.

So how can we fix it?

To fix it we need to identify how to accurately select elements while writing tests.

I have seen many developers changing the HTML structure by adding some `testid` so they can get the test passed like this:

```js
it("should render Register component correctly", () => {
    render(<Register />);
    const element = screen.getByTestId("title");
    expect(element).toBeInTheDocument();
});

```

Assuming you added an extra `data-testid` attribute to your JSX like this:

```js
<h2 className="title" data-testid="title">
     Register
</h2>

```

This will work and make your all tests pass. But this is not the correct way.

Just to make your test pass, **you should not change your JSX by adding some extra `testid` or `class`.**

Instead, you should **always try to use methods provided by `screen`** to make an accurate selection of DOM elements.

So now the question is how to make an accurate selection.

The `getByRole` method accepts optional options which you can use like this:

```js
const element = screen.getByRole("heading", { level: 2 });

```

As our main `Register` heading is a `h2` heading, we specifically said to select `level 2` heading.

Now, if you update the first test case, you will see that all the tests are passing.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/22_fixed_failing_test.png)
_Test passed by adding more specific query for heading_

Now, let's add another test for testing the subheading.

As the subheading is of level 6, you can query it like this:

```js
const element = screen.getByRole("heading", { level: 6 });

```

This will work, but there is another way we can target that element.

For that, you can install the [testing playground](https://chrome.google.com/webstore/detail/testing-playground/hejbmebodbijjdhflfknehhcgaklhano?hl=en) Chrome browser extension.

Once it's installed, follow the below steps:

* open your Chrome dev tools using Ctrl + Alt + I or Cmd + Option + I (Mac)
* select the `Testing Playground` tab
* Click the cursor pointer and select the subheading of the `Register` component as shown below:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/23_accurate_subheading.gif)
_Testing Playground extension demo_

As you can see, you will get the accurate DOM element query which you can use in your test like this:

```js
screen.getByRole('heading', {
  name: /please enter your details below to register yourself\./i
})

```

So you can write your test like this:

```js
 it("should test for presence of subheading in the component", () => {
    render(<Register />);
    const element = screen.getByRole("heading", {
      name: /please enter your details below to register yourself\./i
    });
    expect(element).toBeInTheDocument();
 });

```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/24_all_passed.png)
_Test result_

Writing a test case for subheading is not necessary, because it does not affect the component behavior even if you don't test that. But just to show you how your tests will break for multiple elements, I have added that element on the UI along with its test case.

The `Testing Playground` Chrome extension is really useful to find out the exact matching query for any of the UI elements.

So instead of using the `screen.debug` method to see the DOM structure, you can use this Chrome extension to find out the role and other information for all the displayed elements as can be seen below:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/25_extension_demo.gif)
_Finding out specific query using testing playground_

As you can see, you can get any element by role, by placeholder text, or by label text with the methods provided by `screen`.

Now that you're aware of the more specific query selectors, let's update other test cases to use the specific selectors.

Wherever we're using just `screen.getByRole("button")`, replace it with the following:

```js
screen.getByRole("button", {
  name: /register/i
})

```

So now, if later someone adds another button in the same component, your test will not fail.

Your final `register.test.jsx` file will look like this:

```js
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import Register from "./Register";

describe("Register component", () => {
  it("should render Register component correctly", () => {
    render(<Register />);
    const element = screen.getByRole("heading", {
      level: 2
    });
    expect(element).toBeInTheDocument();
  });

  it("should test for presence of subheading in the component", () => {
    render(<Register />);
    const element = screen.getByRole("heading", {
      name: /please enter your details below to register yourself\./i
    });
    expect(element).toBeInTheDocument();
  });

  it("should show error message when all the fields are not entered", async () => {
    render(<Register />);
    const buttonElement = screen.getByRole("button", {
      name: /register/i
    });
    await userEvent.click(buttonElement);
    const alertElement = screen.getByRole("alert");
    expect(alertElement).toBeInTheDocument();
  });

  it("should not show any error message when the component is loaded", () => {
    render(<Register />);
    const alertElement = screen.queryByRole("alert");
    expect(alertElement).not.toBeInTheDocument();
  });

  it("should show success message when the registration is successful.", async () => {
    render(<Register />);
    const buttonElement = screen.getByRole("button", {
      name: /register/i
    });
    await userEvent.click(buttonElement);
    const alertElement = screen.getByRole("alert");
    expect(alertElement).toBeInTheDocument();
  });
});

```

## Conclusion

React Testing library is amazing and has become a very popular tool with which to test React applications.

Just remember that unlike [enzyme testing library](https://enzymejs.github.io/enzyme/), you should not test for state changes when using React Testing Library.

So we have not written test cases to check if the state correctly changes after the user types some text in the `name`, `email`, or `password` fields.

In React Testing Library you check the behavior of DOM when the user clicks on a button or submits a form and so on instead of testing the internal state of the component.

### Thanks for Reading!

You can find the complete source code for this tutorial in [this repository](https://github.com/myogeshchavan97/testing-library-demo).

If you want to become the best MERN stack developer (full stack developer), then do check out [my course](https://online-elearning-platform.netlify.app/).

* This is a pre-recorded video course that will be constantly updated for any future changes.
* In this course, you will learn how to create React and Node.js applications from scratch and build an amazing online learning platform.
* After learning through this course, you will be able to build any MERN stack application confidently and easily.
* There is a separate section in this course, where you will learn how to test your entire React application using React testing library and jest.

So do check out this amazing course.

Want to stay up to date with regular content regarding JavaScript, React, Node.js? [Follow me on LinkedIn](https://www.linkedin.com/in/yogesh-chavan97/).

