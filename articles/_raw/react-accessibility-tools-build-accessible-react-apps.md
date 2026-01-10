---
title: React Accessibility Tools – How to Build More Accessible React Apps
subtitle: ''
author: Joseph Mawa
co_authors: []
series: null
date: '2021-09-27T14:18:59.000Z'
originalURL: https://freecodecamp.org/news/react-accessibility-tools-build-accessible-react-apps
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/tool-box.jpg
tags:
- name: Accessibility
  slug: accessibility
- name: React
  slug: react
seo_title: null
seo_desc: 'Making a website or web app accessible improves the user experience for
  people with disabilities and for all users as well.

  Since developers deal with tight deadlines and competing priorities, it is easy
  to accidentally ship unresolved accessibility ...'
---

Making a website or web app accessible improves the user experience for people with disabilities and for all users as well.

Since developers deal with tight deadlines and competing priorities, it is easy to accidentally ship unresolved accessibility issues to production. And things becomes even more complex when working with JavaScript frameworks such as React which involves writing JSX.

But fortunately, there are tools that you can take advantage of to lint or evaluate common accessibility issues in your text editor or the browser.

This article will shed light on these existing accessibility tools and how you can use them to build more accessible React applications.

## What is web accessibility?

A website or web app is said to be accessible if it doesn’t exclude people with disabilities from using it on account of their disability.

Having an accessible website removes barriers and ensures that both disabled and non-disabled persons have equal access to the web content and functionality.

The benefits of making your website accessible to people with disabilities will extend to all users including non-disabled persons.

## Why you should pay attention to accessibility

I can't emphasize the importance of accessibility enough. If you don't pay attention to it right from the beginning of your project, you risk turning accessibility into a burden and an expensive one in the future if you start retrofitting.

Making your site accessible should be an integral part of your project right from the word go. It should not be an afterthought.

I have highlighted below why you need to focus on accessibility right from the beginning:

### Follows SEO best practices

Some of the basic accessibility requirements such as using semantic HTML elements, proper use of heading elements, and adding descriptive `alt` attributes to `img` tags are also SEO best practices.

### Improves UX for all users

Improving accessibility for people with disabilities will improve the experience for all your users.

For example, adding a sufficient contrast ratio is not only helpful for people with low vision, color blindness, or cognitive impairment but it's also helpful to people working in different lighting conditions.

Similarly adding an `alt` attribute with appropriate text will help people using screen readers as well as those with slow internet connections when the image fails to load or takes too long to load.

### It's the right thing to do

By making your website accessible, you are doing the right thing. They too have the right to access the service you are offering and some are your clients. Besides, it won’t be good for you or your business if you are accused of discrimination because your site is inaccessible to PWDs. It will damage your brand and reputation.

### Avoids legal issues

Finally, you might run into legal accessibility requirements depending on where you live and work. Some countries have legislation that requires websites to be accessible to people with disabilities.

## Accessibility standards and guidelines

There are several different accessibility standards and guidelines. The most notable and widely recognized standards were developed by the [World Wide Web Consortium (W3C)](https://www.w3.org/Consortium/) through its [Web Accessibility Initiative (WAI)](https://www.w3.org/WAI/about/).

I have highlighted some of these standards and guidelines in the sub-sections below.

### [Web Content Accessibility Guidelines (WCAG) 2.1](https://www.w3.org/WAI/standards-guidelines/wcag/)

WCAG is one of the internationally recognized standards for web content accessibility.

It was developed by W3C through a participatory process with input from a number of individual and institutional stakeholders from around the world.

This standard explains how to make web content more accessible to people with disabilities. It has also been [ISO approved](https://www.iso.org/standard/58625.html).

According to W3C, WCAG was created primarily to serve as a go-to standard for individuals, organizations, and governments internationally on matters of web content accessibility.

### [Authoring Tools Accessibility Guidelines (ATAG) 2.0](https://www.w3.org/WAI/standards-guidelines/atag/)

ATAG is a set of accessibility guidelines that you can use for designing tools for authoring web content.

This guideline helps you make sure that you produce authoring tools that are accessible to people with disabilities. The tools should, in turn, help authors create accessible web content.

### [User Agent Accessibility Guidelines (UAAG) 2.0](https://www.w3.org/WAI/standards-guidelines/uaag/)

The UAAG 2.0 is a sister to the WCAG. This set of guidelines spell out how you can make browsers, browser extensions, media players, and other user agents accessible to people with disabilities.

It is used by browser vendors and browser extension makers to address certain accessibility issues such as text customization in the browser.

In the next section, we shall highlight a couple of tools that can help you flag basic accessibility issues in your React applications.

## Accessibility Tools for Your React Applications

It is easy to unintentionally ship accessibility issues to production despite your best efforts to do otherwise. In this section, we'll shed light on some tools you can use to highlight common accessibility issues.

It might be tempting to omit certain accessibility features if you are dealing with tight deadlines. So it's helpful to have accessibility tools in your setup that notify you of accessibility defects you might have missed.

This is is by no means an exhaustive list of accessibility tools. If there are other tools that you think are useful but are not included here, do get in touch with me on [Twitter](https://twitter.com/mjmawa). I will be happy to update this article. Someone might find them useful too.

Though these tools will catch some common accessibility issues that you can measure programmatically, they won't do your job for you. It is your responsibility to make a deliberate effort to develop more accessible and inclusive digital products right from the project's conception.

I have categorized the tools we are going to cover into two categories, namely:

* Accessibility tools you can integrate into your React project that have been developed with React in mind.
    
* General accessibility audit tools which you can use to audit sites built with or without React.
    

In the sub-sections below, I'll highlight the tools that you can use in your React projects. They are purposely created for use with React or JSX.

### Accessibility Tools Built for React

#### [eslint-plugin-jsx-a11y](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y)

You can use this tool for linting accessibility issues on JSX elements in your React projects. You can use it in conjunction with tools such as eslint for linting your project for accessibility standards right in your text editor.

Since it is distributed via npm, you can install it by running the command below in your project:

```sh
# using npm as package manager

npm install eslint-plugin-jsx-a11y --save-dev

# using yarn as package manager

yarn add eslint-plugin-jsx-a11y --dev
```

Any React project which you've created using `create-react-app` comes with this tool already configured – but it has only a subset of the configurable accessibility rules enabled by default.

You can enable additional rules by creating an `.eslintrc` configuration file in your project and adding the following code to it. The code below activates the recommended rules:

```js

{
  "extends": ["react-app", "plugin:jsx-a11y/recommended"],
  "plugins": ["jsx-a11y"]
}
```

If you want to flag accessibility issues in a custom React project, you need to install `eslint` and add `"jsx-a11y"` to the plugins field of your `.eslintrc` configuration file.

It will then flag accessibility issues that it can identify programmatically and warn you right in your text editor depending on your configuration.

```js

{  "plugins": [    "jsx-a11y"  ]}
```

For more info about how to configure this linting tool in a custom React project, check the project [README](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y#readme) on GitHub.

#### [axe accessibility linter](https://marketplace.visualstudio.com/items?itemName=deque-systems.vscode-axe-linter)

Axe accessibility linter is a Visual Studio Code extension that you can use for linting React, HTML, Vue, and Markdown for some common accessibility defects.

It checks for accessibility issues in `.js`, `.jsx`, `.ts`, `.tsx`, `.vue`, `.html`, `.htm`, `.md` and `.markdown` files.

You don’t need configuration to start using axe accessibility linter after installation. You install it from VS code marketplace and it automatically starts linting compatible files for accessibility defects out of the box without the need for additional configuration.

For a complete list of rules used by axe accessibility linter, check the extension page on VS Code marketplace.

You can also go ahead and configure the tool if you wish by turning some rules on and off by adding the `axe-linter.yml` configuration file at the root of your project.

You have an option of disabling accessibility rules individually or in a group using the WCAG standard. Using this feature in your project will ensure all members of your team adhere to the same accessibility standard.

You can add the following to your `axe-linter.yml` file to enable or disable certain rules individually. For a complete list of configurable rules, check the axe accessibility linter extension page at the VS Code marketplace.

```yml

# To enable/disable rules at individual level
rules:
  accessibility-rule: false # turn off rule
  another-accessibility-rule: true # turn on rule
```

Alternatively, you can add the following to your `axe-linter.yml` configuration file to disable rules as a group using specific WCAG standards.

For a complete list of the configurable WCAG standards, check the axe accessibility linter extension page at the VS Code marketplace.

```yml


# To enable/disable rules at group level based on WCAG standard

tags: 
  - wcag2a # Disable all rules for WCAG 2.0 level A
  - wcag21a # Disable all rules for WCAG 2.1 level A
```

#### [axe-core-react](https://www.npmjs.com/package/@axe-core/react)

This accessibility testing tool is developed and maintained by [Deque Labs](https://www.deque.com/), the same folks behind axe accessibility linter.

`axe-core-react` was originally referred to as `react-axe`. You can run it in your React project in development and accessibility defects are highlighted in the Chrome DevTools console whenever your component updates.

It can really help you catch some accessibility issues early in development. At the moment, `axe-core-react` works best with Google chrome. Unlike the first two, it tests the accessibility of the rendered DOM instead of the JSX element you write in the React components.

```js

npm install @axe-core/react --save-dev
```

You can then run the package in development after the installation.

The code below illustrates how you can run `axe-core-react` in your React application using the most basic configuration. There are additional configuration options which you can read about on the package [README](https://github.com/dequelabs/axe-core-npm/blob/develop/packages/react/README.md) on GitHub.

```js

const React = require('react');
const ReactDOM = require('react-dom');

// Make sure to run @axe-core/react in development

if (process.env.NODE_ENV !== 'production') {
  const axe = require('@axe-core/react');
  axe(React, ReactDOM, 1000);
}

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```

You can use the tools mentioned above directly in your React application to catch and fix common accessibility issues.

In the next section, we will look at a few other accessibility tools that are not directly related to React but are useful for identifying basic accessibility defects in a React application.

### Other accessibility tools

There are a number of tools out there that you can use to detect common accessibility issues in the browser. I have highlighted a couple of these tools below.

#### [Axe DevTools browser extension](https://www.deque.com/axe/)

This is a browser extension you can use for conducting a simple audit of your web page for common accessibility issues.

Your app needs to be hosted somewhere before using this browser extension to check for accessibility issues. It categorizes accessibility defects into critical, serious, moderate, and minor.

#### [WAVE Evaluation Tool browser extension](https://wave.webaim.org/extension/)

This is another chrome browser extension you can use to identify accessibility issues in your website.

Just like the Axe DevTools chrome browser extension, this extension requires you to host the app before you use it for auditing your web app for accessibility defects.

#### [Google’s Lighthouse in Chrome DevTools](https://developers.google.com/web/tools/lighthouse)

You can use Google’s Lighthouse Chrome DevTools to audit your website for accessibility issues. It generates a report which you can use to fix defects in your website.

There is an endless list of general web accessibility evaluation tools out there. You can pick the one that meets your needs.

For a comprehensive list, you can check the [web accessibility evaluation tools list by W3C](https://www.w3.org/WAI/ER/tools/) or [accessibility tools by a11y project](https://www.a11yproject.com/resources/#tools).

## Conclusion

Using tools such as eslint-plugin-jsx-a11y, axe accessibility linter, and axe-core-react in your project will go a long way in helping you develop more accessible and inclusive products using React.

Though they come in handy, the tools mentioned here will only flag a certain percentage of accessibility defects – mainly those that are possible to detect programmatically.

So it's really important to integrate automated testing, manual testing, and actual user testing in your development because automated testing alone may not be able to detect even 50 percent of accessibility issues in your project.
