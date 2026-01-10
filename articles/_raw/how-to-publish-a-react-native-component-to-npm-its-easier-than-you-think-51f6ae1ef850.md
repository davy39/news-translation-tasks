---
title: How to publish a React Native component to NPM — it’s easier than you think
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-01T19:20:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-publish-a-react-native-component-to-npm-its-easier-than-you-think-51f6ae1ef850
coverImage: https://cdn-media-1.freecodecamp.org/images/0*-eB8L7-mDpQKLYPE
tags:
- name: JavaScript
  slug: javascript
- name: mobile app development
  slug: mobile-app-development
- name: npm
  slug: npm
- name: React
  slug: react
- name: React Native
  slug: react-native
seo_title: null
seo_desc: 'By Colby Miller

  So you want to contribute to the open source community? That’s awesome! Helping
  to grow React Native’s fairly young ecosystem is great.

  When I decided to take on this task not long ago, I noticed there wasn’t much material
  around publ...'
---

By Colby Miller

So you want to contribute to the open source community? That’s awesome! Helping to grow React Native’s fairly young ecosystem is great.

When I decided to take on this task not long ago, I noticed there wasn’t much material around publishing React Native components to NPM. So I’m hoping this post will help make the process much easier for others.

> **Note:** All sample code below is from [react-native-progress-steps](https://www.npmjs.com/package/react-native-progress-steps), my very own first NPM package.

Before we get started, make sure to register for an account on NPM. You can do that [here](https://www.npmjs.com/signup).

### Initial Setup

First, let’s create a folder where our React Native component will live.

```bash
mkdir <folder_name> && cd <folder_name>

# For example
mkdir my-component && cd my-component
```

> **Note:** To keep this article brief, I’m assuming you already have Node and NPM installed on your computer. If that’s not the case, take a look at this [documentation](https://www.npmjs.com/get-npm) for help.

Once inside the folder, we need to initialize a new NPM package by typing `npm init`. This will create a `package.json` file that will hold some important metadata about the React Native component.

A series of questions will be displayed such as package name, version, description, keywords, etc.

**Important:** When asked for the _entry point_, make sure to enter `index.js` and press enter. This will be the file that exports your main component.

```jsson
{
  "name": "react-native-progress-steps",
  "version": "1.0.0",
  "description": "A simple and fully customizable React Native component that implements a progress stepper UI.",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/colbymillerdev/react-native-progress-steps.git"
  },
  "keywords": [
    "react-native",
    "react-component",
    "react-native-component",
    "react",
    "react native",
    "mobile",
    "ios",
    "android",
    "ui",
    "stepper",
    "progress",
    "progress-steps"
  ],
  "author": "Colby Miller",
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/colbymillerdev/react-native-progress-steps/issues"
  },
  "homepage": "https://github.com/colbymillerdev/react-native-progress-steps#readme"
}
```

### Project Structure

The next step is setting up a folder structure for your React Native component. This is really up to you, but I’ll share a simple example of mine below:

![Image](https://cdn-media-1.freecodecamp.org/images/1*jQTDB-sc4d0Dt0o_oT9tEQ.png)

You’ll notice some files that we haven’t created yet. We will be addressing those shortly.

Let’s create the `index.js` file. This will be the most important file for properly exporting/importing your component. Navigate to the root project folder and type `touch index.js`.

There are a few different ways of going about the content inside this file.

* Directly writing the component class inside of the `index.js` file and exporting it there.
* Creating a separate component JavaScript file and exporting it in `index.js`.
* Lastly, creating many component and container JavaScript files and exporting all the necessary ones in the `index.js` file. This is the approach I followed and can be seen in the example below.

```js
import ProgressSteps from './src/ProgressSteps/ProgressSteps';
import ProgressStep from './src/ProgressSteps/ProgressStep';

export { ProgressSteps, ProgressStep };
```

No matter which approach is taken, what’s exported in this file is what the consuming app will ultimately import and render. That’s the important part to remember.

```js
import { ProgressSteps, ProgressStep } from 'react-native-progress-steps';
```

### Dependencies

We have to determine what dependencies need to be installed for our React Native component to work properly.

There are three different types of dependencies:

* **peerDependencies:** These dependencies are required for the component to run; however, they are expected to already be installed on the app. An example of this is `react-native` itself. However, in React Native’s case it is not necessary to add `react-native` as a peer dependency.
* **dependencies:** These are also required for the component to run, but you can’t assume the consuming app has these installed. Some examples would be `lodash` and `prop-types` .
* **devDependencies:** These are more straightforward. They are all the packages required to develop the React Native component. Examples of these would be your linter, test framework, and babel.

### Installing Babel Dependency

Our next step is to hook our component up to Babel. We can simply do this by installing the following dev dependency:

```js
npm install metro-react-native-babel-preset --save-dev
```

After the installation is complete, we need to create a `.babelrc` file and add the following to it:

```json
{
  "presets": ["module:metro-react-native-babel-preset"]
}
```

### Creating .gitignore and .npmignore

One of the final steps is to create the standard `.gitignore` and `.npmignore` files as a best practice. This will also avoid any issues when publishing to NPM.

```
# Logs
*.log
npm-debug.log

# Runtime data
tmp
build
dist

# Dependency directory
node_modules
```

```
# Logs
*.log
npm-debug.log

# Dependency directory
node_modules

# Runtime data
tmp

# Examples (If applicable to your project)
examples
```

### Testing

Normally, it’s relatively straightforward to link and install our package locally to apps, without having to publish to NPM first.

This would be done by using the `npm link` command inside of our packages root directory. Then, navigating to an app and typing `npm link <package-na`me> `then npm i`nstall .

However, at the time of writing this article, React Native and the `npm link` command don’t work nicely together.

There are two solutions I’ve found so far that solve this issue:

#### 1. Installing the package in an application using local path

To do this, navigate to an app and directly install your package there using its directory path.

```bash
npm i <path_to_project>

# For example
npm i ../my-component
```

After making any changes to your package, you’ll have to revisit the app and re-install. This is not an ideal solution, but it is one that works.

#### 2. Creating an Examples folder and using npm pack

The `npm pack` command is a great way to quickly package up your React Native component and have it ready for testing. It creates a `.tgz` file that can then be installed into an already existing application.

Let’s create a `/examples` folder inside of our NPM package’s root directory. This folder will essentially be its own React Native application that runs and displays your examples.

This can be done by creating a React Native project using `react-native init examples`.

> **Note:** This requires having React Native already installed on your computer. You can follow the Facebook guide [here](https://facebook.github.io/react-native/docs/getting-started.html).

After that is finished, run the `npm pack` command to generate a file that will have a naming convention similar to `package-name-0.0.0.tgz`.

Then, go into the `/examples` folder and install your component by running `npm i ../package-name-0.0.0.tgz` or `yarn add ../package-name-0.0.0.tgz` in the terminal. Remember to replace `package-name` and `0.0.0` respectively.

Create a JavaScript file or files that will display your component. For this example, we will call this `ExampleOne.js`. It’s important to point out that you should be importing the component that you just installed using yarn or npm in this file.

Once the file is created, open `App.js` and import/export the example file. Whatever is exported in this file is what will be displayed when running the project on a simulator or device.

```js
import ExampleOne from './ExampleOne'

export default ExampleOne;
```

Finally, we can run the application using `react-native run-ios` or `react-native run-android`. We should now be able to see our component and properly test it.

After making any changes to your NPM packages code, remember to run the `npm pack` command, then go into the `/examples` folder to `npm install` or `yarn add` the `.tgz` file.

> A cool benefit of this option is the ability for other users to run your examples on a simulator or device. This allows them to try out your component without having to import it into their own application first. Also, the `.tgz` file can be easily shared among coworkers, friends, etc.

### Publishing To NPM

Finally, we are ready to share our React Native component with the awesome open source community!

Publishing is very quick and easy. Just log into your NPM account from the terminal using `npm login` then publish using `npm publish` .

One thing to remember is NPM requires us to increment the version in `package.json` each time before publishing.

### Conclusion

We have covered a ton of material in this post. If you run into any issues feel free to drop me a question in the comments below. Thanks for following along, I can’t wait to see what you build!

_Contributions, pull requests, and recommendations are always welcome for [react-native-progress-steps](https://www.npmjs.com/package/react-native-progress-steps). Give it a try in your next project and let me know what you think!_

