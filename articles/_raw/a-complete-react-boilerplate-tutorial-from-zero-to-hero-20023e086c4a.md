---
title: A Complete React Boilerplate Tutorial — From Zero to Hero
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-04T19:01:41.000Z'
originalURL: https://freecodecamp.org/news/a-complete-react-boilerplate-tutorial-from-zero-to-hero-20023e086c4a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IRVIWE6HiS8wQstgybKwvw.jpeg
tags:
- name: Data Science
  slug: data-science
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Leonardo Maldonado

  When we’re starting learn React, to make our projects we need to make a boilerplate
  from scratch or use some provided by the community. Almost all the times it’s the
  create-react-app that we use to create an app with no build co...'
---

By Leonardo Maldonado

When we’re starting learn React, to make our projects we need to make a boilerplate from scratch or use some provided by the community. Almost all the times it’s the _create-react-app_ that we use to create an app with no build configuration. Or we just make our own simple boilerplate from scratch.

From this, it comes to mind: why not make a boilerplate with all dependencies that I always use and leave it ready? The community also thought that way, so now we have several community-created boilerplates. Some are more complex than others, but they always have the same goal of saving the maximum amount of time.

This article will teach you how you can build your own boilerplate from scratch with the main dependencies used in the React community today. We’re gonna use some of the moderns features most common these days and from there you can customize it any way you want.

[**The boilerplate created by this article will be available here!**](https://github.com/leonardomso/react-bolt)

### Getting started

First of all, we’re going to create a folder to start our boilerplate. You can name it whatever you want, I’m gonna name mine **_react-bolt_**.

Open your terminal, and create it like this:

```
mkdir react-bolt
```

Now, go to your created folder, and type the following command:

```
npm init -y
```

_NPM_ will create a `package.json` file for you, and all the dependencies that you installed and your commands will be there.

Now, we’re going to create the basic folder structure for our boilerplate. It’s gonna be like this for now:

```
react-bolt    |--config    |--src    |--tests
```

### Webpack

Webpack is the most famous module-bundler for JavaScript applications nowadays. Basically, it bundles all your code and generates one or more bundles. You can learn more about it [here](https://webpack.js.org/).

In this boilerplate we’re going to use it, so install all these dependencies:

```
npm install --save-dev webpack webpack-cli webpack-dev-server webpack-merge html-webpack-plugin clean-webpack-plugin img-loader url-loader file-loader 
```

Now in our `config` folder, we’re going to create another folder called `webpack`, then inside that `webpack` folder create 5 files.

Create a file called `paths.js`. Inside that file is going to be the target directory for all your output files.

Inside it, put all this code:

Now, create another file called `rules.js`, and put the following code there:

After that, we’re going to create 3 more files:

`webpack.common.babel.js`

`webpack.dev.babel.js`

`webpack.prod.babel.js`

Basically, in our `webpack.common.babel.js` file, we’ve set up our entry and output configuration and included as well any plugins that are required. In the `webpack.dev.babel.js` file, we’ve set the mode to development. And in our `webpack.prod.babel.js` file, we’ve set the mode to production.

After that, in our root folder, we’re going to create the last webpack file called `webpack.config.js` and put in the following code:

Our webpack config is ready, so now we’re going to work on other parts of the boilerplate with Babel, ESLint, Prettier, etc.

### Babel

I think that almost everyone who works with React has probably heard about Babel and how this simple transpiler helps our lives. If you don’t know what it is, Babel it’s basically a transpiler that converts your JavaScript code into plain old ES5 JavaScript that can run in any browser.

We’re going to use a bunch of Babel plugins, so in our root folder, install:

```
npm install --save-dev @babel/core @babe/cli @babel/node @babel/plugin-proposal-class-properties @babel/plugin-proposal-object-rest-spread @babel/plugin-syntax-dynamic-import @babel/plugin-syntax-import-meta @babel/plugin-transform-async-to-generator @babel/plugin-transform-runtime @babel/preset-env @babel/preset-react @babel/register @babel/runtime babel-eslint babel-jest babel-loader babel-core@7.0.0-bridge.0
```

After this, we’re gonna create a file in our root folder called `.babelrc` and inside that file, we’re going to put the following code:

Now our project is compiled by Babel, and we can use the next-generation JavaScript syntax without any problems.

### ESLint

The most used tool for linting projects nowadays is ESLint. It is really helpful to find certain classes of bugs, such as those related to variable scope, assignment to undeclared variables, and so on.

First, install the following dependencies:

```
npm install --save-dev eslint eslint-config-airbnb eslint-config-prettier eslint-loader eslint-plugin-babel eslint-plugin-import eslint-plugin-jsx-a11y eslint-plugin-prettier eslint-plugin-react 
```

Then, in our root folder, create a file called `.eslintrc` and put the following code there:

### Prettier

Prettier is basically a code formatter. It parses your code and re-prints it with its own rules that take the maximum line length into account, wrapping code when necessary.

You just need to install it:

```
npm install --save-dev prettier
```

And in our root folder, create a file called `.prettierrc` and put the following code there:

### React

React is an open-source JavaScript application library to build user interfaces. It was developed by Facebook and has a huge community behind it. If you are reading this article, I assume that you already know about React, but if you want to learn more about it, you can read up [here](https://reactjs.org/).

We’re going to install the following dependencies:

```
npm install --save react react-dom cross-env
```

And inside our `src` folder, we’re going to create a simple HTML file `index.html` and put in the following code:

After that, we’re going to create a simple React project. Inside our `src` folder, create a `index.js` file like this:

Inside our `src` folder we’re going to have the following structure:

```
src    |--actions    |--components    |--reducers    |--reducers    |--store
```

Create a file called `App.js` inside the `components` folder, and put in the following code:

### Redux

Redux makes it easy to manage the state of your application. Another way of looking at this is that it helps you manage the data you display and how you respond to user actions. These days a lot of people prefer other options like _MobX_ or just the _setState_ itself, but I’m gonna stick with Redux for this boilerplate.

First, we’re going to install some dependencies:

```
npm install --save redux react-redux redux-thunk
```

Then, we’re going to create our Redux store, and put some state there. In our `store` folder, create an `index.js` file and put that following code there:

Now, inside our `reducers` folder create an `index.js` and put the following code:

Last, we’re gonna to our `index.js` in our `src` folder, and wrap the code with the `<Provider` /> and pas`s our` store as props to make it available to our application.

It’s going to be like this:

All done. Our Redux store is configured and ready to go.

### React Router

React Router is the standard routing library for React. Basically, it keeps your UI in sync with the URL. We’re gonna use it in our boilerplate, so install it:

```
npm install --save react-router-dom
```

After that, go to our `index.js` in our `src` folder and wrap all the code there with the `<BrowserRoute`r>.

Our `index.js` in our `src` folder it’s going to end up like this:

### Styled Components

Styled Components makes CSS easy for everyone, as it helps you organize your React project. Its objective is to write more small and reusable components. We’re gonna use it, and if you want to learn more about it, read up [here](https://www.styled-components.com/).

First, install it:

```
npm install --save styled-components
```

Then, in our `App.js` file inside our `components` folder, we’re going to create a simple title using Styled Components. Our title is going to be like this:

And inside our file, we need to import styled components, so our file is going to end up like this:

### Jest & React Testing Library

Jest is an open-source JavaScript testing library from Facebook. It makes it easy to test your application, and gives us a lot of information about what is giving the right output and what’s not. React Testing Library is a very light-weight solution for testing React components. Basically, this library is a replacement for Enzyme.

Every application needs some kind of tests. I’m not gonna write tests in this article but I’m gonna show you how you can configure these tools to start testing your applications.

First, we’re gonna install both:

```
npm install --save-dev jest jest-dom react-testing-library
```

After that, go to our package.json and put the following after all:

Then, go to our `config` folder, and inside it created another folder called `tests` and inside that folder, create 2 files.

First, create a file called `jest.config.js` and put in the following code:

Then, create a file called `rtl.setup.js` and put in the following code:

All done. Our boilerplate is ready to go and you can use it now.

Now go to our file `package.json` and put in the following code:

Now, if you run the command `npm start` and go to `localhost:8080`, we should see our application working fine!

[**If you want to see my final code, the boilerplate created by this article is available here!**](https://github.com/leonardomso/react-bolt)

I have some ideas for some features that I’d love to include in the boilerplate, so please feel free to contribute!

? F[**ollow me on Twitter!**](https://twitter.com/leonardomso)   
**⭐** F[**ollow me on GitHub!**](https://github.com/leonardomso)

_I’m looking for a remote opportunity, so if have any I’d love to hear about it, so please contact me!_

