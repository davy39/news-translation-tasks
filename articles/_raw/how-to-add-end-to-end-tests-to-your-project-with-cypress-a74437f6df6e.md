---
title: How to add end to end tests to your project with Cypress
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-05T23:16:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-end-to-end-tests-to-your-project-with-cypress-a74437f6df6e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LpbDW-kW6Jh85WFAFEKwlQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
- name: Software Testing
  slug: software-testing
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Austin Tackaberry

  In this post, I will walk through the process of adding Cypress end-to-end tests
  to an existing project.

  Why end to end testing?

  There are pros and cons to all testing methods. End to end testing is the closest
  to actual user tes...'
---

By Austin Tackaberry

In this post, I will walk through the process of adding Cypress end-to-end tests to an existing project.

### Why end to end testing?

There are pros and cons to all testing methods. End to end testing is the closest to actual user testing which is one of its main advantages. The closer the test is to mimicking the user, the more likely it will catch issues that the user might experience.

If you wanted a user to test tweeting on Twitter, you might tell them something like:

> Go to [https://twitter.com](https://twitter.com,) and log in. Click on the text box with placeholder text of “What’s happening?”, and then type “This is a test tweet”. Click the button with the text, “Tweet”. Now, go to your profile page, and look at the first tweet. The text should equal “This is a test tweet”.

Ideally, you give similar instructions to your end to end test runner.

You could instead have it look for elements by class names or ids, but what if the class names or ids purposely change? Or what if the text changes accidentally? If you told the test runner to click the button by class name, the test could incorrectly pass. You might argue:

> What if you want to change the text on purpose? Maybe you want to change the button text to read “Send” instead of “Tweet”?

That is perhaps a valid argument, but you could also argue that you actually want the test to fail if the text changes. Ultimately, you have to ask yourself, “If this text changed, do I want my tests to break?” In the case of “Send” vs “Tweet”, maybe you don’t want the test to break, but maybe if the text was accidentally deleted or misspelled, then you would want them to break. You can’t really have both, so you need to make the best decision for you and your app.

Some disadvantages to end to end testing are:

* They are “costly”, that is they take a long time to run. Every test requires a full browser to be instantiated with actual browser events which takes more time than unit or integration tests.
* It does a good job of finding problems, but it doesn’t do a good job of helping you solve those problems. Your end to end test might find that the payment system is broken, but it won’t tell you which one of your 10 microservices caused the problem.

### Which end to end testing framework to pick

There are a bunch of end to end testing frameworks out there, and it can be difficult to pick the “right” one. I’ll share my thoughts very briefly though I have admittedly only used Cypress:

**Test Cafe** —This is the latest end to end testing framework, and it seems to be very good. It integrates with Browser Stack, has good browser support, has support for all front-end frameworks, supports ES2015+ syntax and also typescript. It looks like you have to have the paid version to get recorded tests.

**Puppeteer** — This is Google’s open source solution. It seems lightweight and easy to get going. It is open source and runs on Chromium (headless or not). Puppeteer is pitched as a test framework that has rich functionality, better than having no end to end tests but not a full solution. They also just recently shared that they are [experimenting with Firefox](https://twitter.com/ChromiumDev/status/1070790759937269761).

**Cypress —** It is a developer friendly, open source testing framework. Cypress records snapshots and videos of your tests, has a test runner console, and is free. It’s easy to get started for developers and QA engineers. It only currently supports Chrome variants but it [has cross browser support on the roadmap](https://github.com/cypress-io/cypress/issues/310). It doesn’t have native [iframe support](https://github.com/cypress-io/cypress/issues/136), though there are workarounds. Cypress has its own promise-based system that you have to use (can’t use ES6 promises).

Here is a good resource for an in-depth comparison of Cypress and Test Cafe: [https://medium.com/yld-engineering-blog/evaluating-cypress-and-testcafe-for-end-to-end-testing-fcd0303d2103](https://medium.com/yld-engineering-blog/evaluating-cypress-and-testcafe-for-end-to-end-testing-fcd0303d2103)

![Image](https://cdn-media-1.freecodecamp.org/images/46bWXP9x94n3PNT4wmB0KC8H2-kJPmj8b37Z)
_Photo by [Unsplash](https://unsplash.com/photos/cY-SXZp6TUY?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">chuttersnap</a> on <a href="https://unsplash.com/search/photos/options?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Getting Started

The project that I’m going to use is [https://ydkjs-exercises.com](https://ydkjs-exercises.com). It is a single page web application that provides exercises built to help users test their knowledge as they read [You Don’t Know JavaScript](https://github.com/getify/You-Dont-Know-JS). It uses React, React Router, and the React Context API. There are unit/integration tests using jest and react-testing-library. And now I will add end to end testing with Cypress!

I will keep track of the progress via tags, starting with `cypress-0`, and incrementing the integer at each step. [Here is the starting point](https://github.com/austintackaberry/ydkjs-exercises/tree/cypress-0).

The first step is to install Cypress as a `devDependency`:

```
npm install cypress --save-dev
```

The current version of Cypress is v3.1.1. The docs mention that the Cypress npm package is a wrapper around the Cypress binary. And that as of version 3.0, the binary is downloaded to a global cache directory to be used across projects.

Now, let’s open up Cypress. If you are using npm version > 5.2, you can open it using:

```
npx cypress open
```

This opens up Cypress with a welcome modal telling us that they added a bunch of files to our project:

![Image](https://cdn-media-1.freecodecamp.org/images/M41bAYSYx5WSFzrEg8atyQNzd-mLK6-EtOiU)

After clicking to close the modal, we see that there are a bunch of example tests, and we see that we can run them in Chrome 70. If you click on “Runs”, you see that you can set up a Cypress dashboard to look at previous runs. We aren’t going to worry about that, but you could certainly check out that feature.

I chose to track all of these example files in git because I want future contributors to have access to them when they fork the project.

[Here is the current progress up to this point.](https://github.com/austintackaberry/ydkjs-exercises/tree/cypress-1)

### Writing a cypress script

We are almost ready to write our first test. We need to create a directory to store our Cypress tests: `cypress/integration/ydkjs`

Now we need to write the script that will start our dev server, run our Cypress tests, then stop our dev server. This project was bootstrapped with Create React App which means it has a `scripts/start.js` file that is used to start the server. I am going to copy the code from there, paste it into a new `scripts/cypress.js` file, and make some modifications.

The code snippet below is the meat of our new `scripts/cypress.js` file.

```js
return devServer.listen(port, HOST, err => {
    if (err) {
        return console.log(err);
    }
    if (isInteractive) {
        clearConsole();
    }
    console.log(chalk.cyan('Starting the development server...\n'));
    return cypress
        .run({
            spec: './cypress/integration/ydkjs/*.js',
        })
        .then(results => {
            devServer.close();
        });
});
```

It does just what we said it would do. It starts the dev server, runs all the test files in `cypress/integration/ydkjs`, and then it stops the dev server.

Now in `cypress.json` we can add our `baseUrl`:

```js
{
    "baseUrl": "http://localhost:3000"
}
```

Now we can write our first test! Let’s call it `cypress/integration/ydkjs/sidebar.js`, and we will use it to test sidebar functionality. For now, let’s just write a dummy test:

```js
/* globals context cy */
/// <reference types="Cypress" />
context('Sidebar', () => {
    beforeEach(() => {
        cy.visit('/');
    });
    
    it('does something', () => {
        cy.contains('YDKJS Exercises');
    });
});
```

All we are doing here is visiting the base url and finding an element that contains “YDKJS Exercises”. Note that I only added the comment on the first line so that `eslint` doesn’t complain about undefined Cypress variables.

I also added a new script in my `package.json` :

```js
"scripts": {
    ...
    "cypress": "node scripts/cypress.js",
    ...
},
```

So now I can call `npm run cypress` when I want to run my end to end Cypress tests. Now, when I execute that command in the terminal, I see that my server starts, the test runs and passes, and then the server stops. Woohoo!

[Here is the code up to this point.](https://github.com/austintackaberry/ydkjs-exercises/tree/cypress-2)

### Let’s write some real tests!

Now that we have our Cypress script set up to start the server, run the tests, and stop the server, we can start to write some tests!

We already created a `sidebar.js` test file, so let’s write some tests around our sidebar feature. Perhaps, our first test should be testing to make sure that the sidebar closes when we click the X button and reopens when we click the hamburger.

Before we find the X button and click it, let’s make sure that the sidebar is visible upon loading the home page. I can put this in the `beforeEach` method right after I navigate to the home page because I will always want to make sure that the sidebar is visible when I first go to the home page.

```js
beforeEach(() => {
    cy.visit('/');
    cy.contains('Progress').should('exist');
});
```

Now let’s start writing the test. Because the X is actually an SVG, we can’t easily tell Cypress to go find it. So we will find it using a `data-testid` attribute, or `cy.get("[data-testid=closeSidebar]").click()` . I know what you are thinking…

> Ok, I understand that you can’t use text in this case. But why use a data attribute? Why not just use a class name or an id?

The best practice is to use a data attribute. You could use class names but they are subject to change and best optimized for styling.

As for ids, the main issue there is that you can only have one per page which could be annoying. What if you want to get all X buttons on the page and assert that there should be 2 of them? You can’t do that easily using ids.

Our completed test might look something like this:

```js
it('closes when X is clicked and reopens when hamburger is clicked', () => {
    cy.get('[data-testid=closeSidebar]').click();
    cy.contains('Progress').should('not.exist');
    cy.get('[data-testid=openSidebar]').click();
    cy.contains('Progress').should('exist');
});
```

I go to the home page, make sure the sidebar is open, then click the X button and make sure it is closed, then click the hamburger and make sure the sidebar is reopened. When we run it, it passes!

And you can see a video of the test in `cypress/ydkjs/sidebar.js.mp4`! Pretty neat. This is super helpful when your tests are failing, and you don’t know why.

One thing you need to be careful about is that Cypress is a promise-based system. When you execute `cy.contains('Progress').should('not.exist')` , Cypress will not move on to the next line of code until that line is true. If it sees a DOM element that contains ‘Progress’, it will wait until it disappears or until it times out and the test fails.

This system is nice because it makes writing these tests very quick and easy. It can bite you sometimes, though, when you are dealing with asynchronous actions. Maybe you want to make sure that a DOM element doesn’t show up as a result of clicking a button. You could just click the button and then check to see if that DOM element exists right? But what if the DOM element is created a second after clicking the button? Your test would pass when it should have failed.

Let’s write another test.

When we click on a book on the sidebar, we want to navigate to the page associated with that book.

```js
it('navigates to /up-going when Up & Going is picked', () => {
    cy.contains(/Up & Going \(/).click({ force: true });
    cy.url().should('include', '/up-going');
    cy.contains('Chapter 1: Into Programming').should('exist'); 
    cy.contains('Chapter 2: Into JavaScript').should('exist');
});
```

There are a couple things to note regarding this test. On the ydkjs-exercises homepage, the text “Up & Going” is in two locations. Once in the sidebar and once in the middle of the page. On the sidebar, the full text is “Up & Going (0/41)” which means that the user has answered 0 questions out of 41 possible. On the main page, the text is just “Up & Going”. So to make sure that we click on the Up & Going from the sidebar, I use regex to click the element that contains “Up & Going (”. I don’t want it to include the 0 or the 41 because those numbers could change. This might be one of those cases where using a data attribute might be better than using the text like I did in the code snippet above.

I need to force the click event because the anchor tag has the text but it is wrapped by a list item element. After this, I test to make sure that the url is correct, and the content on the page is correct.

[This is the final state of the code.](https://github.com/austintackaberry/ydkjs-exercises/tree/cypress-4)

### Conclusion

As you can see, once you have Cypress installed, you have the proper script set up to start your dev server, and you get to writing the tests, working with Cypress is pretty quick and painless.

Once you get comfortable with it, you can even make your test code reusable by making your own custom Cypress commands!

You could run these tests pre-commit or in a CI environment to ensure that no regressions make their way into production.

Overall, Cypress is a perfectly solid choice if you want to take your testing to the next level with some end to end tests!

Happy coding!

