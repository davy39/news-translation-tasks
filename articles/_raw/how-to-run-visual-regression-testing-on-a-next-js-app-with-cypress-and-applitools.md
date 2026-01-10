---
title: How to run Visual Regression Testing on a Next.js App with Cypress and Applitools
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-12-10T16:14:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-run-visual-regression-testing-on-a-next-js-app-with-cypress-and-applitools
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/applitools.jpg
tags:
- name: Next.js
  slug: nextjs
- name: Testing
  slug: testing
- name: user testing
  slug: user-testing
seo_title: null
seo_desc: "A critical component of any development project is the tests that make\
  \ sure that project is always doing exactly what it’s supposed to be doing. \nThere\
  \ are a ton of testing tools available to us, but not all of them test what someone\
  \ actually experie..."
---

A critical component of any development project is the tests that make sure that project is always doing exactly what it’s supposed to be doing. 

There are a ton of testing tools available to us, but not all of them test what someone actually experiences. How can we use Applitools to visually test our project and make sure it’s actually working right?

* [What is Visual Regression Testing?](#heading-what-is-visual-regression-testing)
* [What is Cypress?](#heading-what-is-cypress)
* [What is Applitools?](#heading-what-is-applitools)
* [What are we going to build?](#heading-what-are-we-going-to-build)
* [Step 0: Creating a new React application with Next.js](#heading-step-0-creating-a-new-react-application-with-nextjs)
* [Step 1: Installing and configuring Cypress in a Next.js app](#heading-step-1-installing-and-configuring-cypress-in-a-nextjs-app)
* [Step 2: Creating your first Cypress test in a Next.js app](#heading-step-2-creating-your-first-cypress-test-in-a-nextjs-app)
* [Step 3: Installing and configuring Applitools Eyes](#heading-step-3-installing-and-configuring-applitools-eyes)
* [Step 4: Visual regression testing with Applitools Eyes](#heading-step-4-visual-regression-testing-with-applitools-eyes)

%[https://www.youtube.com/watch?v=3dF4t56LHhs]

You can also check out [my live stream](https://www.youtube.com/watch?v=Bei0Cvu7D7I) from [my Twitch channel](https://twitch.tv/colbyfayock) where I walked through the entire process of setting up a new app and testing it with Cypress and Applitools.

And full disclosure, I recently accepted a job as a Developer Advocate with Applitools. But you can do this tutorial using its free tier, with no credit card required.

## What is Visual Regression Testing?

Similar to most tests, Visual Regression Testing is a type of test that will run periodically and at various stages of a project’s lifecycle like on pull request or production deployment to make sure everything in the app is functioning properly.

What Visual Regression Testing does differently, though, is it directly compares visual snapshots of your project. It detects any changes in content, layout, or any other detail you’d like either by statically visiting a page or interacting with it to preview the result of that interaction.

## What is Cypress?

[Cypress](https://www.cypress.io/) is a JavaScript-based testing framework that we’ll use to run our test suite. It runs tests in the browser, allowing us to directly check the state of our project where people will actually use it.

The great thing about Cypress is it also provides the ability to interact with the page. For instance, if we want to test that someone using our app is able to log in, we can enter credentials and submit the login form, then check that the authentication process properly worked.

## What is Applitools?

[Applitools](https://info.applitools.com/ucXr9) is a visual testing tool and automation platform that lets us visually compare our app at different points in time, giving us the ability to check if something changed or isn’t functioning properly.

While Applitools has a few different features we can take advantage of, we’re going to focus on using the Eyes API, which we’ll use to capture our snapshot and send it up to the Applitools dashboard.

## What are we going to build?

While we can really run Cypress and Applitools on a [variety of project types](https://info.applitools.com/ucXsd), we’re going to use Next.js to quickly spin up a new [React](https://reactjs.org/) application. This will allow us to focus on the testing tools rather than the app itself.

Once we have our app set up, we’ll install Cypress and Applitools so we can use them to run our visual regression testing.

_Note: you’ll need to have an Applitools account in order to set up visual regression testing. You can [sign up for a free account](https://info.applitools.com/ucXsg) at applitools.com._

## Step 0: Creating a new React application with Next.js

To get started, we’re going to use [Create Next App](https://nextjs.org/docs/api-reference/create-next-app) to create a new Next.js app.

Once you’re in the directory that you want to create your new project in, inside of your terminal run:

```
npx create-next-app my-testing-app

```

_Note: you can change the project name from `my-testing-app` to whatever you would like._

This will clone the default Next.js example from GitHub, install the dependencies, and immediately allow us to get productive with our testing tools.

Once it’s finished, navigate into your new project:

```
cd my-testing-app

```

Start your development server:

```
npm run dev

```

And now your site should be available at [http://localhost:3000](http://localhost:3000)!

![Image](https://www.freecodecamp.org/news/content/images/2020/12/new-nextjs-app.jpg)
_New Next.js App_

## Step 1: Installing and configuring Cypress in a Next.js app

Now that we have our app set up, we want to install Cypress so that we can use it to run our tests.

Back inside of our terminal, we can install Cypress with:

```
npm install cypress --save-dev

```

Here, we’re including the `—save-dev` flag, as we don’t need Cypress to run in the production version of our application, so we install it as a dev dependency.

Once that’s complete, we need a way to run Cypress from the command line. While we can navigate to Cypress itself, we can instead add a new script command, which will make it easier to run Cypress.

Inside of `package.json`, under `scripts`, add the following:

```json
"cy:open": "cypress open"

```

Now, inside our terminal, we can run that script to open Cypress:

```
npm run cy:open

```

If this is the first time you’re running Cypress, it might take an extra second and install Cypress in your project.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/opening-cypress-in-terminal.jpg)
_Opening Cypress for the first time_

Once finished, Cypress will open a new dialogue panel that will serve as your dashboard for running tests for your project.

You’ll also notice that Cypress lets you know they also added a new directory to your project at `cypress`. This includes example files that let you see how Cypress works and immediately get started.

To try this out, on the right side of the Cypress panel, click **Run 19 integration specs**.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/cypress-run-all-tests.jpg)

Cypress will then open up a new browser and run through all of the example tests.

Next, we’ll add some of our own tests.

[Follow along with the commit!](https://github.com/colbyfayock/my-testing-app/commit/ba73974d4521443d64fa4bddbc07500c0bb7b74f)

## Step 2: Creating your first Cypress test in a Next.js app

Now that we can successfully run our tests, let’s try adding our own.

We don’t need really any of the tests that Cypress included in the examples, so let’s remove the entire `integration/examples` directory.

Then, create a new file under `integration` called `home.spec.js` and inside add the following:

```javascript
/// <reference types="cypress" />

context('Home', () => {
  beforeEach(() => {
    cy.visit('http://localhost:3000');
  });

  it('should find the title of the homepage', () => {
    cy.get('h1').contains('Welcome');
  });
});

```

In the code above, we’re:

* First adding Cypress as a reference type, which allows Cypress to find the file and know that it should use it to run a test
* Creating a new context for our test and defining it as Home
* Telling Cypress that before each test, we want it to visit our homepage
* Defining a test that grabs the h1 and checks that it contains “Welcome”

If we now look back at Cypress, we’ll see that we only have that one Integration Test. If we click it and try to run the test, we’ll see that we actually get an error, as we never started up our development server, meaning it’s not available.

To fix this, we’re going to use a tool called [start-server-and-test](https://www.npmjs.com/package/start-server-and-test).

This package will do what the name implies, it will:

* Start our server based on the command we provide
* Run the tests that we provide
* Stop the server once complete

To add it, inside of our terminal let’s run:

```
npm install start-server-and-test --save-dev

```

Then, inside of our `package.json` file, we’re going to add another new command to the `scripts` object:

```json
"test": "start-server-and-test dev 3000 cy:open"

```

Here, we’re telling start-server-and-test that we want to run the `dev` command to start our server, that it will be available at port 3000, and that we want to run the `cy:open` command after to run our tests.

And if we go back to our terminal and run:

```
npm run test

```

We’ll see that Cypress opens up like before. But if we now run our test, we can see that it successfully opens up our Next.js app and it sees the word “Welcome” inside of our `h1`!

![Image](https://www.freecodecamp.org/news/content/images/2020/12/successful-test-cypress.jpg)
_Successfully running a test in Cypress_

[Follow along with the commit](https://github.com/colbyfayock/my-testing-app/commit/b7fdcada3c6642521baa8c34949c4b9df3e56c18).

## Step 3: Installing and configuring Applitools Eyes

With Cypress successfully running our tests, we can now hook into our tests and use Applitools to run visual regression testing on our project.

Before we dive in, make sure you have a [free account](https://info.applitools.com/ucXsg) set up over at Applitools, which we’ll need in order to set up an API key.

To get started, we’re going to need to install the Eyes library to our project.

In our terminal, we can run:

```
npm install @applitools/eyes-cypress --save-dev

```

Which will install the [Cypress-specific SDK for Applitools Eyes](https://www.npmjs.com/package/@applitools/eyes-cypress).

Once that’s finished installing, we can run the Eyes setup script.

```
npx eyes-setup

```

This will go through the project and add the necessary configurations to Cypress to make Eyes work properly.

Finally, we’ll need to make our Applitools API key available whenever we run our tests.

To start, we need to find our API key in our Applitools account.

Inside the Applitools dashboard, select **My API Key** under the account dropdown.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/applitools-finding-api-key.jpg)
_Finding the Applitools API key_

It will open a dialogue where you can select and copy your API key.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/applitools-api-key.jpg)
_Copying the Applitools API key_

You’ll want to save this API key for later when we run our tests.

Next, we’ll want to be able to set our API key. We can do this a few ways:

* [Export the environment variable](https://docs.cypress.io/guides/guides/environment-variables.html#Option-3-CYPRESS) in our shell before running the tests
* Prepend the API key to the test command
* Add the API key to the [applitools.config.js](https://www.npmjs.com/package/@applitools/eyes-cypress#advanced-configuration) file
* Create an environment variable using dotenv and the [cypres-dotenv](https://github.com/morficus/cypress-dotenv) package

For this demo, we’re going to run our test by prepending the API key to our command. This will allow us to quickly test this out.

To do this, any time we run a command like `npm run test`, we’re going to include our API key in front of it like:

```
APPLITOOLS_API_KEY="abcd1234" npm run test

```

_Note: remember to replace the API key with your unique ID._

And now, we should be ready to add our first test.

[Follow along with the commit!](https://github.com/colbyfayock/my-testing-app/commit/0b11b0238270b320969ac9982b271a48981634f4)

## Step 4: Visual regression testing with Applitools Eyes

We have Cypress and Applitools both configured and ready to go, meaning we can now add Applitools Eyes to visually test our app!

Our app doesn’t have a lot of functionality yet., so we can start off with a basic check that makes sure our homepage looks the way it’s supposed to each time our tests run.

To start, inside of our `cypres/integrations/home.spec.js` file, let’s add the following right below our existing `it` statement:

```javascript
it('should verify the homepage looks as expected', () => {
  cy.eyesOpen({
    appName: 'My App',
    testName: 'Homepage Check',
  });

  cy.eyesCheckWindow({
    tag: 'App Window',
    target: 'window',
    fully: true
  });

  cy.eyesClose();
});

```

Here’s what we’re doing here:

* First, we’re “opening the eyes” of Applitools, which will prepare the Eyes functionality to check our app
* Next, we’re running a check on the window of our application, essentially capturing a screenshot of our app and sending it to Applitools
* Finally, we “close the eyes” of Applitools, letting Eyes know that we’re running our checks

Now, if we run our test command and start our test:

```
APPLITOOLS_API_KEY="abcd1234" npm run test

```

We can see that Cypress runs our new test case which doesn’t appear that it’s doing anything inside of our browser, but shows a passing indicator.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/successul-applitools-check.jpg)
_Successfully ran an Applitools Eyes check in Cypress_

Now, if we go back to our Applitools dashboard:

![Image](https://www.freecodecamp.org/news/content/images/2020/12/applitools-eyes-first-snapshot.jpg)
_First snapshot in Applitools_

We can see that we have a new “run” titled Homepage Check (which we specified in the code) which shows that it passed with a snapshot of our app.

Now, having this screenshot alone isn’t what makes this powerful. From now on, any time we run this test, Applitools will compare our app against this original snapshot and let us know if anything changed.

To test this out, we’re going to change the color of title of our page. This might seem like a simple change, but style changes can be more challenging for tools like Cypress alone to detect an issue, which is where Applitools Eyes will shine with its snapshot comparison.

Inside of `styles/Home.module.css` file, let’s add the following to the `.title` class:

```css
color: #ddd;
```

![Image](https://www.freecodecamp.org/news/content/images/2020/12/nextjs-app-title-color-change.jpg)
_Next.js app with light gray title_

While we may not have intentionally made a change like this in practice, this could have happened if we were changing styles that cascade to our title. This makes our title hard to read, but that makes this perfect for a test case.

Now, let’s run our tests again:

```
APPLITOOLS_API_KEY="abcd1234" npm run test
```

But this time, we can see that our test fails! 

![Image](https://www.freecodecamp.org/news/content/images/2020/12/cypress-failed-applitools-eyes-test-error.jpg)
_Cypress throwing an error with the Applitools Eyes check_

Our Applitools test fails because it states that “Eyes-Cypress detected diffs or errors during execution of visual tests”.

If we look inside of our Applitools dashboard:

![Image](https://www.freecodecamp.org/news/content/images/2020/12/applitools-eyes-text-change-detected.jpg)
_Change detected in text of app title in Applitools Eyes_

We can see that we now have an “Unresolved” run where Applitools shows us the differences on the page, which in our case, is the "Welcome to" part of our title.

This is super useful when working on projects where it can be challenging to test every single page or type of page in an app. We can make sure that if anything changes or breaks, it will immediately get flagged in Applitools.

From here, if we’re happy with color change, we can accept the new version of our app.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/applitools-eyes-accept-reject-changes.jpg)
_Accept or reject changes in Applitools Eyes_

Otherwise we can reject it and let our team know that it needs to be fixed.

[Follow along with the commit!](https://github.com/colbyfayock/my-testing-app/commit/6c5f5655d0e15878e870a893652201979244e986)

## What’s next?

Between Cypress and Applitools, we have a lot of things we can do to make sure that our app is behaving the way we want it to.

Most of the time when we’re building an app, we’re building that app so people can interact with it.

Using Cypress, we can click on different parts of the page, changing the state of the page, then run a check with Applitools Eyes to make sure it’s functioning the way we expect it to.

We can also have Cypress run on different browsers to make sure our app is working properly everywhere someone is trying to use it!

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">🐦 Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">📺 Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">📫 Sign Up For My Newsletter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://github.com/sponsors/colbyfayock" style="text-decoration: none;">💝 Sponsor Me</a>
    </li>
  </ul>
</div>

