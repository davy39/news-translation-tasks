---
title: How to Automate Accessibility Tests with Cypress
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-14T19:00:42.000Z'
originalURL: https://freecodecamp.org/news/automating-accessibility-tests-with-cypress
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/cypress-io-logo-social-share-8fb8a1db3cdc0b289fad927694ecb415-1.png
tags:
- name: Accessibility
  slug: accessibility
- name: Testing
  slug: testing
seo_title: null
seo_desc: "By Leonardo Faria\nIn my previous post, I covered how to add screenshot\
  \ testing in Cypress to ensure components don't unintentionally change over time.\
  \ \nNow, I will share how to automate accessibility tests with Cypress.\nWhy should\
  \ we care about acces..."
---

By Leonardo Faria

In my [previous post](https://www.freecodecamp.org/news/how-to-add-screenshot-testing-with-cypress-to-your-project/), I covered how to add screenshot testing in Cypress to ensure components don't unintentionally change over time. 

Now, I will share how to automate accessibility tests with Cypress.

## Why should we care about accessibility? 

Short answer: because it is the right thing to do.

Long answer: an accessible web can help people with disabilities improve their lives. 

There are different kinds of disabilities, including auditory, cognitive, neurological, physical, speech and visual. And our goal as product creators, engineers, and designers is to create experiences that include all people. 

It is also important to mention that web accessibility also benefits people _without_ disabilities. 

For example, accessible sites help people with changing abilities due to ageing or people with slow Internet connections or those using devices with small screens. 

And a disability can also be temporary. For example, someone with a broken arm can't type and use a mouse at the same time.

If you want to educate yourself about the topic, I can recommend the [W3C Web Accessibility Initiative (W3C WAI)](https://www.w3.org/WAI/) and [The A11Y Project](https://www.a11yproject.com/).

## Accessibility testing techniques

There are different ways to test if your website/app is accessible. The W3C WAI has a [list of 140+ tools](https://www.w3.org/WAI/ER/tools/) to help you determine if your website/app meets accessibility guidelines. 

You can also add in your strategy:

- Real user testing: companies like [Fable](https://www.makeitfable.com/) connect you and people with disabilities so that your research and user testing can help you meet your compliance goals.
- Browser extensions: [axe](https://www.deque.com/axe/browser-extensions/) is a recommended extension for Chrome, Firefox, and Edge that helps identify and resolve common accessibility issues.

The [accessibility engine of axe is open-source](https://github.com/dequelabs/axe-core) and it can be used in different ways, as this post will show.

## Before we start

I created a [sample website](https://cypress-accessibility-example.vercel.app/) to mimic a Component Library. It is a very simple website created with Tailwind CSS and hosted in Vercel and it documents 2 components: [badge](https://cypress-accessibility-example.vercel.app/badge.html) and [button](https://cypress-accessibility-example.vercel.app/button.html).

You can check out the [source code](https://github.com/leonardofaria/cypress-accessibility-example) on GitHub. The website is static and it is inside the `public` folder. You can see the website locally by running `npm run serve` and checking in the browser [http://localhost:8000](http://localhost:8000).

![Sample website](https://leonardofaria.net/wp-content/uploads/2020/08/cypress-sample-website.png)

## Adding Cypress and cypress-axe

Start by cloning the [example repository](https://github.com/leonardofaria/cypress-example). Next, create a new branch and install [cypress-axe](https://www.npmjs.com/package/cypress-axe), the package responsible for tying the axe engine to Cypress.

```bash
git checkout -b add-cypress
npm install -D cypress cypress-axe
```

Next, create a `cypress/support/index.js` file containing:

```
import 'cypress-axe'
```

This import will inject all the functions we need for our tests.

## Creating the accessibility test

Time to create the accessibility test. Here is the plan:

1. Cypress will visit each page (badge and button) of the project.
2. Cypress will test each example in the page. The [Badge page](https://cypress-example.vercel.app/badge.html) has 2 examples (Default and Pill), while the [Button page](https://cypress-example.vercel.app/badge.html) has 3 examples (Default, Pill and Outline). 

All these examples are inside an `<div>` element with a `cypress-wrapper`. This class was added with the only intention to identify what needs to be tested.

The first step is creating the Cypress configuration file (`cypress.json`):

```json
{
  "baseUrl": "http://localhost:8000/",
  "video": false
}
```

The `baseUrl` is the website running locally. As I mentioned before, `npm run serve` will serve the content of the `public` folder. The second option, `video` disables Cypress video recording, which won't be used in the project.

Time to create the test. In `cypress/integration/accessibility.spec.js`, add:

```js
const routes = ['badge.html', 'button.html'];

describe('Component accessibility test', () => {
  routes.forEach((route) => {
    const componentName = route.replace('.html', '');
    const testName = `${componentName} has no detectable accessibility violations on load`;

    it(testName, () => {
      cy.visit(route);
      cy.injectAxe();
      
      cy.get('.cypress-wrapper').each((element, index) => {
        cy.checkA11y(
          '.cypress-wrapper',
          {
            runOnly: {
              type: 'tag',
              values: ['wcag2a'],
            },
          }
        );
      });
    });
  });
});
```

In the code above, I am creating dynamic tests based in the `routes` array. The test will check each `.cypress-wrapper` element against WCAG 2.0 Level A rules. 

There are different standards / purposes, as the table below shows: 

| Tag Name         | Accessibility Standard / Purpose                     |
| ---------------- | ---------------------------------------------------- |
| `wcag2a`         | WCAG 2.0 Level A                                     |
| `wcag2aa`        | WCAG 2.0 Level AA                                    |
| `wcag21a`        | WCAG 2.1 Level A                                     |
| `wcag21aa`       | WCAG 2.1 Level AA                                    |
| `best-practice`  | Common accessibility best practices                  |
| `wcag***`        | WCAG success criterion e.g. wcag111 maps to SC 1.1.1 |
| `ACT`            | W3C approved Accessibility Conformance Testing rules |
| `section508`     | Old Section 508 rules                                |
| `section508.*.*` | Requirement in old Section 508                       |

You can find more information about it in the [axe-core docs](https://github.com/dequelabs/axe-core/blob/develop/doc/API.md#axe-core-tags).

Last, let's create inside the `package.json` command to trigger the tests:

```json
{
  "test": "cypress"
}  
```

From here, there are 2 options: run Cypress in headless mode with `npm run cypress run` or use the Cypress Test Runner with `npm run cypress open`.

### Headless option

Using `npm run test run`, the output should be similar to the next image:

![Output of first test](https://leonardofaria.net/wp-content/uploads/2020/08/cypress-accessibility-first-test.jpg)

The tests will pass since the components have no accessibility issues.

### Test Runner option

Using `npm run test open`, Cypress Test Runner will be opened and you can follow step by step the tests.

![Cypress Test Runner screenshot](https://leonardofaria.net/wp-content/uploads/2020/08/cypress-accessibility-test-runner.jpg)

Our first milestone is done. Let's merge this branch to master. If you want to see the work done so far, jump in my [Pull Request](https://github.com/leonardofaria/cypress-accessility-example/pull/1/files). 

## Testing in real life

Imagine we are updating the website and we want to identify the buttons with ids. The `id` property must be unique in the document, as we can't have 2 elements with the same one. But we forgot about that and 3 buttons have the same id.

Cypress will fail and the output will look something like this: 

![Output of failed test](https://leonardofaria.net/wp-content/uploads/2020/08/cypress-accessibility-failed-test.jpg)

Let's improve the output of our tests by showing a table of found issues. First, let's create a new branch:

```bash
git checkout -b improve-cypress-tests
```

Next, create the `cypress/plugins/index.js` file with the following content: 

```js
module.exports = (on, config) => {
  on('task', {
    log(message) {
      console.log(message)
 
      return null
    },
    table(message) {
      console.table(message)
 
      return null
    }
  })
}
```

This will execute code in Node via the `task` plugin event of Cypress. Next, let's go back to the `accessibility.spec.js` file and add the following function in the top of the file:

```js
const terminalLog = (violations) => {
  cy.task(
    'log',
    `${violations.length} accessibility violation${
      violations.length === 1 ? '' : 's'
    } ${violations.length === 1 ? 'was' : 'were'} detected`
  )
  // pluck specific keys to keep the table readable
  const violationData = violations.map(
    ({ id, impact, description, nodes }) => ({
      id,
      impact,
      description,
      nodes: nodes.length
    })
  )
 
  cy.task('table', violationData)
}
```

The `violations` array contains all information about the failing elements. You can tweak this code to include, for instance, the element source code in the test output.

Last, let's call the function inside the tests. Modify the `checkA11y` function to: 

```js
cy.checkA11y(
  '.cypress-wrapper',
  {
    runOnly: {
      type: 'tag',
      values: ['wcag2a'],
    },
  },
  terminalLog,
);
```

When you run the test again, you'll get a table containing the issues reported by axe:

![Output of failed test with a nice table](https://leonardofaria.net/wp-content/uploads/2020/08/cypress-accessibility-failed-test-table.jpg)

If you have any questions, please check the [Pull request](https://github.com/leonardofaria/cypress-accessibility-example/pull/2/files) in Github. 

## Next steps

From here, you can continue your journey toward making products more accessible. As some next steps, I would recommend:

- Adding these tests in your CI solution - I wrote about [integrating Cypress inside Semaphore](https://www.freecodecamp.org/news/2020/08/03/adding-screenshot-testing-with-cypress-in-your-project/#adding-ci)
- Finding the best way to customize the output of tests to improve troubleshooting issues
- Learning more about how axe works.

I hope that you have learned that accessibility testing is not difficult and it doesn't require much to start. Automation powered by axe can definitely help us to create better user experiences for all people.

--

Questions? Comments? This post is also in [my blog](https://leonardofaria.net/2020/08/13/automating-accessibility-tests-with-cypress/). If you like this content, follow me on [Twitter](https://twitter.com/leozera) and [GitHub](https://github.com/leonardofaria). 


