---
title: Real-world ReactNative apps made easy with React Native Elements, Jest, and
  MobX MST
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-25T18:12:34.000Z'
originalURL: https://freecodecamp.org/news/real-world-reactnative-apps-made-easy-with-react-native-elements-jest-and-mobx-mst-15003ccefef1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Q_Olvnw5k9PVenJrWCvXow.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
- name: Testing
  slug: testing
seo_title: null
seo_desc: 'By Qaiser Abbas

  In this post, we’ll build a real-world mobile application in ReactNative. We’ll
  also explore some of the development practices and libraries, including the following:


  directory structure

  state management (in Mobx)

  code styling and li...'
---

By Qaiser Abbas

In this post, we’ll build a real-world mobile application in ReactNative. We’ll also explore some of the development practices and libraries, including the following:

* directory structure
* state management (in Mobx)
* code styling and linting tools ([Prettier](https://prettier.io/), [ESLint](https://eslint.org/), and [Arirbnb style guide](https://github.com/airbnb/javascript))
* screen navigation using [react-navigation](https://reactnavigation.org/)
* user interface using [React Native Elements](https://react-native-training.github.io/react-native-elements/)
* and an important, but often ignored part: unit-testing your application (via [Jest](https://facebook.github.io/jest/) and [Enzyme](https://github.com/airbnb/enzyme)).

So let’s get started!

### State management in React

React and ReactNative have made building Single Page Applications and Mobile Applications fun and easy, but they only cover the view of the applications. State Management and UI design can still be a painful part of building the app.

There are several popular State Management libraries available for React. I’ve used Redux, Mobx, and RxJS. While all three of them are good in their own ways, I’ve enjoyed MobX the most because of its simplicity, elegance, and powerful state management.

[Redux](https://redux.js.org/introduction/three-principles), based primarily on the concepts of functional programming and pure functions, tries to solve the complexity of state management by imposing some restrictions on when updates are possible. These restrictions are reflected in three basic principles: a single source of truth, read-only state, and pure functions. You can read more about [these principles in the Redux documentation](https://redux.js.org/introduction/three-principles).

While I’m a fan of functional programming, I’ve experienced that you have to deal with a lot of unnecessary boilerplate code when working with Redux. You also have to write code for dispatching actions and transforming state yourself.

Mobx, on the other hand, does this job for you, making it easier to maintain and more fun to work with. You need the right amount of code and restrictions in MobX to achieve superior state management and a good developer experience.

In Redux, you also have to spend a substantial amount of time normalizing and de-normalizing your data. In MobX, you don’t need to normalize the data, and MobX automatically tracks the relations between state and derivations. We’ll go into this later.

[RxJS](http://reactivex.io/rxjs) is a reactive programming library for JavaScript. It is different from MobX in that RxJS allows you to react to events while in MobX. You observe the values (or state) and it helps you react to changes in state.

Although both RxJS and MobX provide the ability to perform reactive programming, they are quite different in their approaches.

### About our app

The application we’ll be building is for a Book Store. It will mainly consist of two simple views: the Books View and the Authors View.

The app will contain a navigation drawer with two menu options, allowing the user to switch between the two views. The first option will be for navigating to the Books View, and the other option will navigate to the Authors View.

The Books View will contain the list of books, as well as a tab allowing the user to switch between Fiction and Non-Fiction books. The Authors View will containing the list of authors.

We’ll be installing everything on a Mac OS. Most of the commands will be the same when you have Node installed, but if you face any issues, let me know, (or just google it).

#### Topics Covered

We’ll cover different topics and the various libraries necessary to create and test a full blown React Native application:

1. We’ll install `create-react-native-app`, and use it to bootstrap our Book Store application
2. Setup Prettier, ESLint, and the Airbnb style guide for our project
3. Add Drawer and Tabs Navigation using react-navigation
4. Test our React components with Jest and Enzyme
5. Manage the state of our app using MobX (mobx-state-tree). It will also involve some UI changes and more navigation. We’ll sort and filter the books by genre, and allow the user to see the Book detail screen when the user taps on a book.

Here’s a demo of the Bookstore app we’re going to build:

![Image](https://cdn-media-1.freecodecamp.org/images/O6XAotXM0OShzwM92tzzGHonYKrkgto68n-c)
_Demo of our Bookstore App_

#### What we won’t cover

There are a few things we won’t cover in this article, which you may want to consider in your project:

1. Tools for adding static type system in JavaScript, like [flow](https://flow.org/) and [TypeScript](https://www.typescriptlang.org/)
2. Although we will add some styling to our app, we won’t go into details concerning the different options available for adding styles in a ReactNative application. The [styled-components](https://github.com/styled-components/styled-components) library is one of the most popular for both React and ReactNative applications.
3. We won’t build a separate backend for our application. We will go through integration with the Google Books API, but we’ll use mock data for the most part.

### Create a React Native application using create-react-native-app CLI (CRNA)

[Create React Native App](https://github.com/react-community/create-react-native-app) is a tool created by [Facebook](https://code.facebook.com/) and the [Expo](https://expo.io/) team that makes it a breeze to get started with a React Native project. We’ll initialize our ReactNative app using [CRNA](https://github.com/react-community/create-react-native-app) CLI. So let’s get started!

Assuming that you have [Node](https://nodejs.org/en/download/) already installed, , we need to install `create-react-native-app` globally, so that we can initialize a new React Native project for our Book Store.

```
npm install -g create-react-native-app
```

Now, we can use the create-react-native-app CLI to create our new React Native project. Let’s name it `bookstore-app`:

```
create-react-native-app bookstore-app
```

Once CRNA is done bootstrapping our React Native application, it will show some helpful commands. Let’s change the directory to the newly created CRNA app, and start it.

```
cd bookstore-app npm start
```

This will start the packager, giving the option to launch the iOS or Android simulator, or open the app on a real device.

If you face any issues, please refer to either the [React Native’s getting started guide](https://facebook.github.io/react-native/docs/getting-started.html) or [Create React Native app (CRNA) guide](https://github.com/react-community/create-react-native-app/blob/master/react-native-scripts/template/README.md).

#### Opening the CRNA app on a real device via Expo

When the app is started via `npm start`, a QR code will be displayed in your terminal. The easiest way to look at our bootstrapped app is using the Expo app. To do that:

1. Install the [Expo](https://expo.io/) client app on your iOS or Android device.
2. Make sure that you are connected to the same wireless network as your computer.
3. Using the Expo app, scan the QR code from your terminal to open your project.

#### Opening the CRNA app in a simulator

To run the app on iOS Simulator, you’ll need to install Xcode. To run the app on an Android Virtual Device, you need to setup the Android development environment. Look at the react-native getting started guide for both the setups.

### Setup Prettier, ESLint, and an Airbnb style guide

In this section, we’ll setup Prettier, ESLint, and Airbnb style guide to make sure our code not only looks pretty, but also runs code linting.

#### Why use a linting tool?

JavaScript is a dynamic language, and doesn’t have a static type system like languages such as C++ and Java. Because of this dynamic nature, JavaScript lacks the kind of tools available for static analysis that many other languages offer.

This results in hard-to-find bugs related to data types, and requires more effort in debugging and troubleshooting these issues, especially for inexperienced JavaScript developers.

Since it’s not a compiled language, error are discovered when the JavaScript code is executed at runtime. There are tools like TypeScript and flow that help catch these kind of errors by adding a static type system to JavaScript, but we won’t be going into either of these tools in this tutorial.

On the other hand, there are linting tools like ESLint available that perform static analysis of the JavaScript code based on configurable rules. They highlight problems in the code that may be potential bugs, which helps developers discover problems in their code before it is executed.

#### Install and Setup ESLint

A good linting tool is extremely important to ensure that quality is baked in from the beginning and errors are found early. ESLint also helps you implement style guidelines.

To make sure we write high quality code and have the right tools from the very beginning of our Bookstore project, we’ll start our tutorial by first implementing linting tools. You can learn more about [ESLint on their website](https://eslint.org/docs/about/).

ESLint is fully configurable and customizable. You can set your rules according to your preferences. However, different linting rules configurations have have been provided by the community. One of the popular ones is the Airbnb style guide, and this is the one we’ll use. This will include Airbnb’s ESLint rules, including ECMAScript 6+ and React.

First, we’ll install ESLint by running this command in the terminal:

We’ll use Airbnb’s [eslint-config-airbnb](https://github.com/airbnb/javascript/tree/master/packages/eslint-config-airbnb), which contains Airbnb’s ESLint rules, including ECMAScript 6+ and React. It requires specific versions of ESLint, eslint-plugin-import, eslint-plugin-react, and eslint-plugin-jsx-a11y. To list the peer dependencies and versions, run this command:

```
npm info "eslint-config-airbnb@latest" peerDependencies
```

At the time of this writing, these are the versions shown in the output from the above command:

```
{ eslint: '^4.9.0',  'eslint-plugin-import': '^2.7.0',  'eslint-plugin-jsx-a11y': '^6.0.2',  'eslint-plugin-react': '^7.4.0' }
```

So let’s install these specific dependency versions by running this command:

```
npm install -D eslint@^4.9.0 eslint-plugin-import@^2.7.0 eslint-plugin-jsx-a11y@^6.0.2 eslint-plugin-react@^7.4.0
```

This will install the necessary dependencies and generate the `.eslintrc.js` file in the project root directory. The .eslintrc.js file should have the following configurations:

```
module.exports = {  "extends": "airbnb"};
```

#### Code styling

While we have the linting covered with ESLint and the Airbnb style guide, a big part of code quality is consistent code styling. When you’re working on a team, you want to make sure that the code formatting and indentation is consistent throughout the team. Prettier is just the tool for that. It ensures that all the code conforms to a consistent style.

We’ll also add the [ESLint plugin for Prettier](https://github.com/prettier/eslint-plugin-prettier), which will add Prettier as an ESLint rule and report differences as individual ESLint issues.

Now, there may be conflicts between the ESLint rules and the code formatting done by Prettier. Fortunately, there is a plugin available called [eslint-config-prettier](https://github.com/prettier/eslint-config-prettier) that turns off all rules that are unnecessary or might conflict with Prettier.

#### Install and Setup Prettier with ESLint

Let’s install all the necessary packages, Prettier, and eslint-plugin-prettier. We’ll also need to install eslint-config-airbnb for this:

```
npm install -D prettier prettier-eslint eslint-plugin-prettier eslint-config-prettier eslint-config-airbnb
```

**NOTE:** If ESLint is installed globally, then make sure eslint-plugin-prettier is also installed globally. A globally-installed ESLint cannot find a locally-installed plugin.

To enable eslint-plugin-prettier plugin, update your .eslintrc.js file to add the “prettier” plugin. And to show linting error on Prettier formatting rules, add the “rule” to show error on “prettier/prettier”. Here’s our updated .eslintrc.js:

```
module.exports = {  "extends": [    "airbnb",    "prettier"  ],  rules: {    "prettier/prettier": "error",  },}
```

[eslint-config-prettier](https://github.com/prettier/eslint-config-prettier) also ships with a CLI tool to help you check if your configuration contains any rules that are unnecessary or conflict with Prettier. Let’s be proactive and do that.

First, add a script for it to package.json:

```
{  "scripts": {    "eslint-check": "eslint --print-config .eslintrc.js | eslint-config-prettier-check"  }}
```

Now, run the “eslint-check” command to see ESLint and Prettier’s conflicting rules:

```
npm run eslint-check
```

This will list the conflicting rules in the terminal. Let’s turn off the conflicting rules by updating the .eslintrc.js file. I also prefer singleQuote and trailingComma, so I’ll configure those rules as well. This is what our .eslintrc.js file looks like now:

```
module.exports = {  "parser": "babel-eslint",  "extends": [    "airbnb",    "prettier"  ],  "plugins": [    "prettier"  ],  "rules": {    "prettier/prettier": "error",    "react/jsx-closing-bracket-location": "off",    "react/jsx-closing-tag-location": "off",    "react/jsx-curly-spacing": "off",    "react/jsx-equals-spacing": "off",    "react/jsx-first-prop-new-line": "off",    "react/jsx-indent": "off",    "react/jsx-indent-props": "off",    "react/jsx-max-props-per-line": "off",    "react/jsx-tag-spacing": "off",    "react/jsx-wrap-multilines": "off"  }}
```

If you now run `eslint` with the `--fix` flag, the code will be automatically formatted according to the Prettier styles.

#### Configure VS Code to run ESLint on save

We can configure any IDE to automatically run ESLint on Save or as we type. Since we have also configured Prettier along with ESLint, our code will automatically be pretiffied. VS Code is an IDE popular in the JavaScript community, so I’ll show how to setup ESLint’s auto-fix on save using VS Code, but the steps would be similar in any IDE.

To configure VS Code to automatically run ESLint on Save, we first need to install the ESLint extension. Go to Extensions, search for the “ESLint” extension, and install it. Once the ESLint extension is installed, go to `Preferences > User Setti`ngs, and set “eslint.autoFixOnSave” to true. Also make sure that “files.autoSave” is either set to “off”, “onFocusChange” or “onWindowChange”.

Now, open the file App.js. If the ESLint is configured correctly, you should see some linting error, like the “react/prefer-stateless-function”, “react/jsx-filename-extension”, and “no-use-before-define” errors. Let’s turn those “off” in the .eslintrc.js file. I also prefer singleQuote and trailingComma as I mentioned above, so I’ll configure those rules as well.

Here is the updated .eslintrc.js file.

```
module.exports = {  "parser": "babel-eslint",  "extends": [    "airbnb",    "prettier"  ],  "plugins": [    "prettier"  ],  "rules": {    "prettier/prettier": [      "error",      {        "singleQuote": true,        "trailingComma": "all",      }    ],    "react/prefer-stateless-function": "off",    "react/jsx-filename-extension": "off",    "no-use-before-define": "off",    "react/jsx-closing-bracket-location": "off",    "react/jsx-curly-spacing": "off",    "react/jsx-equals-spacing": "off",    "react/jsx-first-prop-new-line": "off",    "react/jsx-indent": "off",    "react/jsx-indent-props": "off",    "react/jsx-max-props-per-line": "off",    "react/jsx-tag-spacing": "off",    "react/jsx-wrap-multilines": "off"  }}
```

I know this was a lot of work, considering that we haven’t even started working on our app yet! But trust me, this setup will be very beneficial for your projects in the long run, even if you’re a one person team. When you’re working with other developers, linting and programming standards will go a long way in reducing code defects and ensuring consistency in code style.

You can find the changes made in this section in [this branch](https://github.com/qaiser110/ReactNative-Bookstore-App-Tutorial/tree/1-prettier-eslint-airbnb-styleguide-setup) of the tutorial repository.

### Drawer and Tabs Navigation using react-navigation

In this section, we’ll add the Drawer and Tabs Navigation using react-navigation.

Our Bookstore app will contain a navigation drawer with two menu options. The first menu item for the **AuthorsScreen**, containing the list of authors. The second menu item for the **BooksScreen**, containing the list of books.

Tapping on a book will take the user to the BookDetail Screen. For navigation between the different views, we’ll use [React Navigation](https://reactnavigation.org/docs/en/hello-react-navigation.html) to add navigation to our app. So let’s install it first:

```
npm install --save react-navigation
```

#### createStackNavigator

Our ReactNative app will contain two modules:

* an Author module allowing the users to browse list of authors
* a Books module, containing the list of books.

The Author and Book modules will be implemented using the StackNavigator from [React Navigation](https://reactnavigation.org/). Think of StackNavigator as the history stack in a web browser. When the user clicks on a link, the URL is pushed to the browser history stack, and removed from the top of the history stack when the user presses the back button.

```
export const BookStack = createStackNavigator({  Books: {    screen: BooksScreen,  },})
```

```
export const AuthorStack = createStackNavigator({  Authors: {    screen: AuthorsScreen,  },})
```

For BooksScreen and AuthorsScreen, we’ll simply add two stateless [react components](https://reactjs.org/docs/components-and-props.html) for now, with some buttons to test our screen navigation and drawer functionality:

```
const BooksScreen = ({ navigation }) => (  <View>    <Button      onPress={() => navigation.navigate('Authors')}      title="Go to Authors"    />    <Button onPress={() => navigation.openDrawer()} title="Open Drawer" />  </View>)
```

```
const AuthorsScreen = ({ navigation }) => (  <Button    onPress={() => navigation.navigate('Books')}    title="Go back to Books"  />)
```

`navigation.openDrawer()` will trigger the drawer to open. `navigation.navigate()` allows the app to navigate to different screens.

In our application, we’ll add a Drawer which will maintain the menu for our Author and Book modules. We’ll implement the drawer using React Navigation’s [createDrawerNavigator](https://reactnavigation.org/docs/en/drawer-based-navigation.html).

The first menu in the drawer will be for the Author module, and the second for the Book module. Author and Book Stack Navigators will both be inside the main DrawerStack.

Here’s the code for the drawer implementation:

```
const App = createDrawerNavigator({  Books: {    screen: BookStack,  },  Authors: {    screen: AuthorStack,  },})
```

Here’s a [diff of our latest changes](https://github.com/qaiser110/ReactNative-Bookstore-App-Tutorial/tree/1-prettier-eslint-airbnb-styleguide-setup).

In the file App.js, we’ve made the following changes:

1. We renamed the default export to App
2. We added two stateless components for our screens, BooksScreen and AuthorsScreen.
3. We added the StackNavigator from [React Navigation](https://reactnavigation.org/) to implement navigation for our app.
4. We used [createDrawerNavigator()](https://reactnavigation.org/docs/en/drawer-based-navigation.html) from react-navigation to implement the Drawer Navigation. This renders the Drawer content, along with the menu options for Books and Authors.

And after making the above changes, here’s what our UI looks like when we click on the “Open Drawer” button and navigate between screens.

![Image](https://cdn-media-1.freecodecamp.org/images/Sr1hvC3EvNusiCwezGk-WvtgzzdsE2tsxtym)

#### Directory Structure

It’s important to think about your application and how you’ll structure of your files and resources in the beginning of the project. While there are several ways you could structure your application code, I prefer co-locating files and tests using a feature-based architecture. Co-locating files related to a particular feature or module has a number of benefits.

Let’s create an src directory where we’ll keep all our source files. Inside it, create two directories: one for the book view, named “book”, and the other for the author view, named “author”.

Create index.js files within each of the two directories we just added. These files will export the components for each of our views. Move the code from App.js for the BookView and AuthorView components into these files, and import them instead.

It’s important to note that refactoring should be a big part of the development workflow. We should continuously refactor our code to prepare ourselves for future changes and challenges. This has a big impact on productivity and change management in the long run.

Our app should still work as it was before the refactor. Here’s the [file diff of our recent changes](https://github.com/qaiser110/ReactNative-Bookstore-App-Tutorial/commit/d0377da1c3797e2dd9a35237533ae5815af1b582).

Each of the screens will have a title, which means that we’ll be duplicating the same code along with the styles. To keep our code DRY, let’s move the title to a separate file `src/components/Title.js`, and reuse it where needed. We’ll also move the main views into a new parent directory `src/views` to keep them separate from other components.

#### Tab Navigation

The business requirement for our app is to have three tabs in the books view, to show all books by default, and additional tabs to show filtered books for the fiction and non-fiction books. Let’s use the [createBottomTabNavigator](https://reactnavigation.org/docs/en/tab-based-navigation.html) from react-navigation to implement the Tab Navigation.

```
import { createBottomTabNavigator } from 'react-navigation'
```

```
import { AllBooksTab, FictionBooksTab, NonfictionBooksTab } from ' components/book-type-tabs'
```

```
export default createBottomTabNavigator({  'All Books': AllBooksTab,  Fiction: FictionBooksTab,  Nonfiction: NonfictionBooksTab,})
```

We should also add a title on every screen to identify the currently selected screen. Let’s create a separate directory `src/components` for all the common components, and create a file for our `Title` component inside this new directory.

```
// src/components/Title.jsimport React from 'react'import { StyleSheet, Text } from 'react-native'
```

```
const styles = StyleSheet.create({  header: {    textAlign: 'center',    padding: 20,    marginTop: 20,    fontSize: 20,    color: '#fff',    backgroundColor: '#434343',  },})
```

```
export default ({ text }) => <Text style={styles.header}>{text}</Text>
```

Note that we’ve also added `style` to the `<Te`xt> component, importing `both Styl`eShee`t an`d Text `from react-`native.

We’ll add the `Title` to each view component, providing the title `text` in the props. Also, since the Authors view just contains a list of authors, we don’t need a StackNavigator for it, so we’ll change it to a plain React component. Here’s what our `src/views/author/index.js` file looks like now:

```
// src/views/author/index.js
```

```
import Title from '../../components/Title'
```

```
export default ({ navigation }) => (  <View>    <Title text="Authors List" />    <Button onPress={() => navigation.openDrawer()} title="Open Drawer" />    <Button onPress={() => navigation.navigate('Books')} title="Go to Books" />  </View>)
```

Now, when we open the Books menu from the drawer, we’re able to switch tabs by clicking on the tabs at the bottom.

With those changes, we have our app’s navigations all done. Here’s the [diff for our recent changes](https://github.com/qaiser110/ReactNative-Bookstore-App-Tutorial/commit/007ec23b049f45bf38279c39e22f32db894f16a7).

### React Native Elements

There are several UI component libraries for adding React Native components with style. Some of the more poular ones are [React Native Elements](https://react-native-training.github.io/react-native-elements/)NativeBase, and [Ignite](https://infinite.red/ignite). We’ll be using React Native Elements for our Bookstore app. So let’s first install react-native-elements:

```
npm install --save react-native-elements
```

#### Creating our Authors List using react-native-elements

Let’s use the **ListItem** component from React Native Elements to add a list of authors in our Author screen.

For the Authors List, we’ll use the data and code from the [ListItem](https://react-native-training.github.io/react-native-elements/docs/listitem.html) demo. We’ll revisit **ListItem** into more detail when we implement the Book List screen.

Here’s the [diff for our recent changes](https://github.com/qaiser110/ReactNative-Bookstore-App-Tutorial/commit/11435b4c79ba718f4f8d4d12fe0b28ef707e4d1c).

### Testing ReactNative components with Jest and Enzyme

In this section, we’ll add some unit tests using Jest and Enzyme.

#### Jest and Enzyme setup

Having unit tests for your code is really important so that you can have confidence in your code when you want to change something. It really pays off when you’re adding more features, and you can make changes without the fear of breaking some existing functionality of your application as a result of the change. You know that your unit tests provide the safety net for your application from leaking out any defects into the production.

We’ll use Jest as our testing framework along with Airbnb’s JavaScript testing utility [Enzyme](https://github.com/airbnb/enzyme). Enzyme has a flexible and intuitive interface that makes it very easy to assert, manipulate, and traverse React Components.

The create-react-native-app kit already includes all the related Jest libraries and configurations. To work with Enzyme, we need to install `enzyme` and some related dependencies. Since we’re using React 16, we’ll be adding `react-dom@16` and `enzyme-adapter-react-16`.

```
npm install -D enzyme react-dom@16 enzyme-adapter-react-16
```

We need to configure `enzyme-adapter-react-16`. We’ll do this during Jest setup. Create `jestSetup.js` file project’s root, with the following code:

```
import { configure } from 'enzyme'import Adapter from 'enzyme-adapter-react-16'
```

```
configure({ adapter: new Adapter() })
```

Now, add this file to Jest’s configuration in `package.json`:

```
"jest": {    "preset": "jest-expo",    "setupTestFrameworkScriptFile": "<rootDir>/jestSetup.js"  },
```

### Enzyme and snapshot tests for our Title component

Now, we’re all set to add Enzyme tests. I prefer having tests co-located with my code. Let’s create a simple test for our Title component by adding a test file next to our Title component. In this test, we’ll simply shallow render the Title component, create a snapshot, and verify the component styles. Create the file `src/components/__tests__/Title.js`, with the following content:

```
import React from 'react'import { shallow } from 'enzyme'import Title from '../Title'
```

```
it('renders correctly', () => {  const wrapper = shallow(<Title text="Sample Text" />)  expect(wrapper).toMatchSnapshot()
```

```
expect(wrapper.prop('accessible')).toBe(true)  expect(wrapper.prop('style')).toEqual({    backgroundColor: '#434343',    color: '#fff',    fontSize: 20,    marginTop: 20,    padding: 20,    textAlign: 'center',  })})
```

Let’s run our our tests:

```
npm test
```

The tests should pass and generate a snapshot, giving the following output:

![Image](https://cdn-media-1.freecodecamp.org/images/rnOmkEVYHmHIuhP7gRLEdtNxtIKgcf0zPGZE)

In case you’re not familiar with Jest Snapshot testing, it is a great way to test React components or different kinds of outputs in general.

Basically, the `toMatchSnapshot()` call renders your component and creates a snapshot in the `__snapshots__` directory (if the snapshot doesn’t already exist). After that, each time you re-run your tests, Jest will compare the output of the rendered component with that of the snapshot, and will fail if there is a mismatch. It will show the difference between the expected and the actual output. You can then review the differences, and if this difference is valid due to some change that you’ve implemented, you can re-run the tests with an `-u` flag, which signals Jest to update the snapshot with the new updates.

Here’s the [diff for our changes so far for Jest and Enzyme test](https://github.com/qaiser110/ReactNative-Bookstore-App-Tutorial/commit/8280243d7c9cab6b69b2b2ed530756fe8a4bdcca), including the generated snapshot.

### enzyme-to-json serializer

If you open up the snapshot file (`src/components/__tests__/__snapshots__/Title.js.snap`), you’ll notice that the content is not very readable. It is obfuscated by the code from the Enzyme wrappers, since we’re using Enzyme to render our component. Fortunately, there is the [enzyme-to-json](https://github.com/adriantoine/enzyme-to-json) library available that converts the Enzyme wrappers to a format compatible with Jest snapshot testing.

Let’s install enzyme-to-json:

```
npm install -D enzyme-to-json
```

And add it to Jest configurations as the snapshot serializer in `pacakge.json`:

```
"jest": {    ...    "snapshotSerializers": ["enzyme-to-json/serializer"]  },
```

Since we now expect the snapshot to be different from the previous snapshot, we’ll pass the `-u` flag to update the snapshot:

```
npm test -- -u
```

If you open up the snapshot file again, you’ll see that the snapshot for the rendered Title component is correct.

We’ll dive more into Jest testing in the later sections.

### Managing state with React Navigation and Mobx Store

![Image](https://cdn-media-1.freecodecamp.org/images/fG6h6BpuhAsx4uUAxBFw61ltncJ2ltF523Fm)

#### MobX or Redux for state management

While React is great for managing the view of your application, you generally need tools for store management of your application. I say generally, because you may not need a state management library at all — it all depends on the type of application you are building.

There are several state management libraries out there, but the most popular are Redux and MobX. We’ll be using Mobx store for our Bookstore application.

I generally prefer MobX to Redux for store management, because I feel that it takes a lot more time to add new store data in Redux compared to MobX.

**Some downsides to Redux:**

* You need to add a lot of boilerplate code.
* You have to write code for dispatching actions and transforming state yourself.
* It forces you to implement things in a specific way. While this would be a good thing in some applications, I find that the amount of time it takes might not be worth it for many applications.

**Some advantages of MobX:**

* It adds that boilerplate for you, and does it well. I find it very easy to work with, whether it’s initial setup, or adding more functionality.
* It doesn’t force you to implement your data flow in a specific way, and you have much more freedom. But again, that might be more problematic than helpful if you don’t setup your MobX stores correctly..

I know this is a sensitive topic, and I don’t want to start a debate here, so I’ll leave this topic for another day. But if you want more perspective on this, there are [several](https://www.robinwieruch.de/redux-mobx-confusion/) [perspectives](https://medium.com/@adamrackis/a-redux-enthusiast-tries-mobx-af675f468c11) on this debate around the internet. Redux and MobX are both great tools for store management.

We’ll be gradually adding functionality to our store instead of adding it all at once, just to show you how easy it is to add more features to MobX stores.

### MobX State Tree

We won’t use Mobx directly, but a wrapper on MobX called [mobx-state-tree](https://github.com/mobxjs/mobx-state-tree). They’ve done a fine job of describing themselves, so I’ll just quote them here:

> Simply put, mobx-state-tree tries to combine the best features of both immutability (transactionality, traceability and composition) and mutability (discoverability, co-location and encapsulation). — MST Github page

Let’s install [mobx](https://github.com/mobxjs/mobx) along with [mobx-react](https://github.com/mobxjs/mobx-react) and [mobx-state-tree](https://github.com/mobxjs/mobx-state-tree)

`npm install --save mobx mobx-react mobx-state-tree`

We’ll be using the Google Books API to fetch the books for our app. If you want to follow along, you’ll have to create a project in the Google Developers Console, enable Google Books API on it, and create an API Key in the project. Once you have the API Key, create a file `keys.json` in the project root, with the following content (replace `YOUR_GOOGLE_BOOKS_API_KEY` with your API key):

```
{  "GBOOKS_KEY": "YOUR_GOOGLE_BOOKS_API_KEY"}
```

**NOTE**: If you don’t want to go through this process of getting an API key, don’t worry. We won’t be using the Google API directly, and will mock the data instead.

Google Books API endpoint `books/v1/volumes` returns an array of `items` where each item contains information on a specific book. Here’s a cut down version of a book:

```
{  kind: "books#volume",  id: "r_YQVeefU28C",  etag: "HeC4avg1XlM",  selfLink: "https://www.googleapis.com/books/v1/volumes/r_YQVeefU28C",  volumeInfo: {    title: "Breaking Everyday Addictions",    subtitle: "Finding Freedom from the Things That Trip Us Up",    authors: [      "David Hawkins"    ],    publisher: "Harvest House Publishers",    publishedDate: "2008-07-01",    description: "Addiction is a rapidly growing problem among Christians and non-Christians alike. Even socially acceptable behaviors, ...",    pageCount: 256,    printType: "BOOK",    categories: [      "Addicts"    ],    imageLinks: {      smallThumbnail: "http://books.google.com/books/content?id=r_YQVeefU28C",      thumbnail: "http://books.google.com/books/content?id=r_YQVeefU28C&printsec=frontcover"    },    language: "en",    previewLink: "http://books.google.com.au/books?id=r_YQVeefU28C&printsec=frontcover",    infoLink: "https://play.google.com/store/books/details?id=r_YQVeefU28C&source=gbs_api",    canonicalVolumeLink: "https://market.android.com/details?id=book-r_YQVeefU28C"  }}
```

We won’t be using all the fields returned in the API response. So we’ll create our MST model for only the data we need in our ReactNative app. Let’s define our Book model in MST.

Create a new directory structure `stores/book` inside `src`, and create a new file `index.js` inside it:

```
// src/stores/book/index.jsimport { types as t } from 'mobx-state-tree'
```

```
const Book = t.model('Book', {  id: t.identifier(),  title: t.string,  pageCount: t.number,  authors: t.array(t.string),  image: t.string,  genre: t.maybe(t.string),  inStock: t.optional(t.boolean, true),})
```

In the above MST node definition, our `Book` model type is defining the shape of our node — of type `Book` — in the in the MobX State Tree. The `types.model`type in MST is used to describe the shape of an object. Giving the model a name isn’t required, but is recommended for debugging purpose.

The second argument, the properties argument, is a key-value pair, where the key is the name of a property, and the value is its type. In our model, `id` is the **identifier**, `title` is of type **string**, `pageCount` is of type **number**, `authors` is an **array of strings**, `genre` is of type **string**, `inStock` of type **boolean**, and `image` of type **string**.

All the data is required by default to create a valid node in the tree, so if we tried to insert a node without a title, MST won’t allow it, and will throw an error.

The `genre` will be mapped to the `categories` field (first index value of the categories array) of the Google Books API data. It may or may not be there in the response. Therefore, we’ve made it of type `maybe`. If the data for **genre** is not there in the response, `genre` will be set to `null` in MST, but if it’s there, it must be of type **string** for it to be valid.

Since `inStock` is our own field, and is not returned in the response from the Google Books API, we’ve made it optional and have given it a default value of true. We could have simply assigned it the value `true`, since for primitive types MST can infer type from the default value. So `inStock: true` is the same as `inStock: t.optional(t.boolean, true)`.

The [creating models](https://github.com/mobxjs/mobx-state-tree#creating-models) section of the _mobx-state-tree_ documentation goes into detail about creating models in MST.

```
// src/stores/book/index.jsconst BookStore = t  .model('BookStore', {    books: t.array(Book),  })  .actions(self => {    function updateBooks(books) {      books.forEach(book => {        self.books.push({          id: book.id,          title: book.volumeInfo.title,          authors: book.volumeInfo.authors,          publisher: book.volumeInfo.publisher,          image: book.volumeInfo.imageLinks.smallThumbnail,        })      })    }
```

```
const loadBooks = process(function* loadBooks() {      try {        const books = yield api.fetchBooks()        updateBooks(books)      } catch (err) {        console.error('Failed to load books ', err)      }    })
```

```
return {      loadBooks,    }  })
```

MST trees are protected by default. This means that only the MST actions can change the state of the tree.

We’ve defined two actions: `updateBooks` is a function that is only called by the `loadBooks` function, so we’re not exposing it to the outside world. `loadBooks` on the other hand, is exposed (we’re returning it), and can be called from outside the `BookStore`.

Asynchronous actions in MST are written using generators, and always return a promise. In our case, `loadBooks` needs to be asynchronous, since we’re making an Ajax call to the Google Books API.

We’ll maintain a single instance of the `BookStore`. If the store already exists, we’ll return the existing store. If not, we’ll create one and return that new store:

```
// src/stores/book/index.jslet store = null
```

```
export default () => {  if (store) return store
```

```
store = BookStore.create({ books: {} })  return store}
```

### Using the MST store in our view

Let’s start with the All Books view. To do that, we’ll create a new file containing our `BookListView` component:

```
import React, { Component } from 'react'import { observer } from 'mobx-react'import BookStore from '../../../stores/book'import BookList from './BookList'
```

```
@observerclass BookListView extends Component {  async componentWillMount() {    this.store = BookStore()    await this.store.loadBooks()  }
```

```
render() {    return <BookList books={this.store.books} />  }}
```

As you can see, we’re initializing the `BookStore` in `componentWillMount`, and then calling `loadBooks()` to fetch the books from the Google Books API asynchronously. The `BookList` component iterates over the `books` array inside the **BookStore**, and renders the `Book` component for each book. Now, we just need to add this `BookListView` component to `AllBooksTab`.

If you start the app now, you’ll see that the books are loading as expected.

Note that I’m using Pascal case naming convention for a file that returns a single React component as the default export. For everything else, I use Kebab case. You may decide to choose a different naming convention for your project.

If you run `npm start` now, you should see a list of books fetched by the Google API.

![Image](https://cdn-media-1.freecodecamp.org/images/nmTNdCQktTI9ubQUzbG3qA3wZ5eent99FzjJ)

Here’s the [diff for our changes so far](https://github.com/qaiser110/ReactNative-Bookstore-App-Tutorial/commit/ad23749ed9ed8ba157fade215ce20df0c2312ede).

### Adding tests for our MST BookStore

Let’s add some unit tests for our BookStore. However, our store is talking to our API, which calls the Google API. We can add integration tests for our store, but to add unit tests, we need to mock the API somehow.

A simple way to mock the API is to use [Jest Manual Mocks](https://facebook.github.io/jest/docs/en/manual-mocks.html) by creating the `__mocks__` directory next to our existing `api.js` file. Inside it, create another `api.js`, the mocked version of our API fetch calls. Then, we just call `jest.mock('../api')`in our test to use this mocked version.

#### Dependency Injection in MobX State Tree

We won’t be using Jest Manual Mocks. I’d like to show you another feature in MST, and demonstrate how easy it is to mock our API using MST. We’ll use Dependency injection in MobX State Tree to provide an easy way to mock the API calls, making our store easy to test. Note that our MST store can also be tested without Dependency Injection using Jest Mocks, but we’re doing it this way just for demonstration.

It is possible to inject environment-specific data to a state tree by passing an object as the second argument to the `BookStore.create()` call. This object will be accessible by any model in the tree by calling `getEnv()`. We’ll be injecting a mock API in our BookStore, so let’s first add the optional `api` parameter to the default export, and set it to the actual `bookApi` by default.

```
// src/stores/book/index.jslet store = null
```

```
export default () => {  if (store) return store
```

```
store = BookStore.create({ books: {} })  return store}
```

Now, add an [MST View](https://github.com/mobxjs/mobx-state-tree#views) for the injected API by grabbing it using `getEnv()`. Then use it in the `loadBooks` function as `self.api.fetchBooks()`:

```
// src/stores/book/index.js// ....views(self => ({    get api() {      return getEnv(self).api    },}))
```

Let’s now create a mock API with the same fetch function as the real API fetch function:

```
// src/stores/book/mock-api/api.jsconst books = require('./books')
```

```
const delayedPromise = (data, delaySecs = 2) =>  new Promise(resolve => setTimeout(() => resolve(data), delaySecs * 1000))
```

```
const fetchBooks = () => delayedPromise(books)
```

```
export default {  fetchBooks,}
```

I’ve added a delay in response so that the response is not sent immediately. I’ve also created a JSON file with the some data similar to that of the response sent by the Google Books API `src/stores/book/mock-api/books.json`.

Now, we’re ready to inject the mock API into our tests. Create a new test file for our store with the following content:

```
// src/stores/book/__tests__/index.jsimport { BookStore } from '../index'import api from '../mock-api/api'
```

```
it('bookstore fetches data', async () => {  const store = BookStore.create({ books: [] }, { api })  await store.loadBooks()  expect(store.books.length).toBe(10)})
```

Run the store test:

```
npm test src/stores/book/__tests__/index.js
```

You should see the test pass.

#### Adding the books filter and applying TDD

I believe in a hybrid approach to Test Driven Development. In my experience, it works best if you add some basic functionality first when starting a project, or when you’re adding a new module or a major functionality from scratch. Once the basic setup and structure is implemented, then TDD works really well.

But I do believe that TDD is the best way to approach a problem space in code. It not only forces you to have better code quality and design, but also ensures that you have atomic unit tests. Additionally it makes sure your unit tests are more focused on testing specific functionality, rather than stuffing too many assertions in a test.

Before we start adding our tests and making changes to our store, I’ll change the delay in our mock API to 300 millisecs to ensure that our tests run faster.

```
const fetchBooks = () => delayedPromise(books, 0.3)
```

We want a `filter` field in our `BookStore` model, and a `setGenre()` action in our store for changing the value of the this `filter`.

```
it(`filter is set when setGenre() is called with a valid filter value`, async () => {  store.setGenre('Nonfiction')  expect(store.filter).toBe('Nonfiction')})
```

We want to run tests only for our BookStore, and keep the tests running and watching for changes. They will re-run when the code has been changed. So we’ll use the watch command and use file path pattern matching:

```
npm test stores/book -- --watch
```

The above test should fail, because we haven’t written the code yet to make the test pass. The way that TDD works is that you write an atomic test to test the smallest unit of a business requirement. Then you add code to make just that test pass. You go through the same process iteratively, until you’ve added all the business requirements. To make our test pass, we’ll have to add a `filter`field of ENUM type in our `BookStore` model:

```
.model('BookStore', {    books: t.array(Book),    filter: t.optional(        t.enumeration('FilterEnum', ['All', 'Fiction', 'Nonfiction']),        'All'    ),})
```

And add an MST action which will allow us to change the filter value:

```
const setGenre = genre => {  self.filter = genre}
```

```
return {  //...  setGenre,}
```

With these two changes, we should be in the green. Let’s also add a negative test for an invalid filter value:

```
it(`filter is NOT set when setGenre() is called with an invalid filter value`, async () => {  expect(() => store.setGenre('Adventure')).toThrow()})
```

And this test should also pass. This is because we’re using an ENUM type in our MST store, and the only allowed values are `All`, `Fiction`, and `Nonfiction`.

Here’s the [diff of our recent changes](https://github.com/qaiser110/ReactNative-Bookstore-App-Tutorial/commit/925920c430a3449b9e1010b11d1d662c8e88ac6a).

#### Sorting and filtering the books

The first index value in the `categories` field of the mock data categorizes the book as **Fiction** or **Nonfiction**. We will use it to filter the books for our **Fiction** and **Nonfiction** tabs, respectively.

We also want our books to always be sorted by title. Let’s add a test for this:

Let’s first add a test for sorting the books:

```
it(`Books are sorted by title`, async () => {  const books = store.sortedBooks  expect(books[0].title).toBe('By The Book')  expect(books[1].title).toBe('Jane Eyre')})
```

To make our test pass, we’ll add a view named `sortedBooks` in our `BookStore`model:

```
get sortedBooks() {  return self.books.sort(sortFn)},
```

And with this change, we should be in the green again.

### About MST Views

We just added the `sortedBooks` view in our `BookStore` model. To understand how MST Views work, we’ll have to understand MobX. The key concept behind MobX is: anything that can be derived from the application state should be derived, automatically.

In [this egghead.io video](https://egghead.io/lessons/javascript-derive-computed-values-and-manage-side-effects-with-mobx-reactions), the MobX creator [Michel Weststrate](https://twitter.com/mweststrate) explains the key concepts behind MobX. I’ll quote a key concept here:

> MobX is built around four core concepts. Actions, observable state, computed values, and reactions… Find the smallest amount of state you need, and derive all the other things… — [Michel Weststrate](https://twitter.com/mweststrate)

The computed values should be pure functions, and in terms of depending only on observable values or other computed values they should have no side effects. Computed properties are lazily evaluated, and their value is evaluated only when their value is requested. The computed values are also cached in MobX, and this cached value is returned when this computed property is accessed. When there’s a change in any of the observable values being used in it, the Computed property is recomputed.

[MST Views](https://github.com/mobxjs/mobx-state-tree#views) are derived from the current observable state. Views can be with or without arguments. Views without arguments are basically [Computed values](https://mobx.js.org/refguide/computed-decorator.html) from MobX, defined using getter functions. When an observable value is changed from an MST action, the affected view gets recomputed, triggering a change (reaction) in the `@observer` components.

### Adding tests for genre filter

We know that there are seven Nonfiction books in the mock data. Let’s now add a test for filtering by `genre`:

```
it(`Books are sorted by title`, async () => {  store.setGenre('Nonfiction')  const books = store.sortedBooks  expect(books.length).toBe(7)})
```

To make filtering by genre work, we’ll add a `genre` field of string type in our `Book` model, and map it to the `volumeInfo.categories[0]` received from the API response. We’ll also change the `sortedBooks` view getter in our `BookStore`model to filter the books before sorting them:

```
get sortedBooks() {  return self.filter === 'All'    ? self.books.sort(sortFn)    : self.books.filter(bk => bk.genre === self.filter).sort(sortFn)},
```

And again, all tests are passing.

Here’s the [diff of our recent changes](https://github.com/qaiser110/ReactNative-Bookstore-App-Tutorial/commit/620be74af6c5bbf119478405388c8bf978d85586).

### Update the UI on tab change

**NOTE**: From here on, we’ll use the mock data for our actual API calls instead of making Ajax requests to Google Books API. To do this, I’ve changed the `bookApi` in the `stores/book/index.js` to point to the mock API (`./mock-api/api.js`).

Note also that the display for all three tabs (“All”, “Fiction” and “NonFiction”) is similar. The layout and format of the items would be the same, but the only difference is the data that they’ll display. And since MobX allows us to keep our data completely separate from the view, we can get rid of the three separate views, and use the same component for all the three tabs.

This means that we don’t need the three separate tabs anymore. So we’ll delete the `book-type-tabs.js` file, and use the `BookListView` component directly in our **TabNavigator** for all three tabs. We’ll use the `tabBarOnPress` callback to trigger the call to `setGenre()` in our `BookStore`. The `routeName`, available on the navigation state object, is passed in to `setGenre()` to update the filter when user presses a tab.

Here’s the updated TabNavigator:

```
// src/views/book/index.js
```

```
export default observer(  createBottomTabNavigator(    {      All: BookListView,      Fiction: BookListView,      Nonfiction: BookListView,    },    {      navigationOptions: ({ navigation }) => ({        tabBarOnPress: () => {          const { routeName } = navigation.state          const store = BkStore()          store.setGenre(routeName)        },      }),    }  ))
```

Note that we’re wrapping `createBottomTabNavigator` in MobX `observer`. This is what converts a React component class or stand-alone render function into a reactive component. In our case, we want the filter in our BookStore to change when `tabBarOnPress` is called.

We’ll also change the view to get sortedBooks instead of books.

```
// src/views/book/components/BookListView.js
```

```
class BookListView extends Component {  async componentWillMount() {    this.store = BkStore()    await this.store.loadBooks()  }
```

```
render() {    const { routeName } = this.props.navigation.state    return (      <View>        <Title text={`${routeName} Books`} />        <BookList books={this.store.sortedBooks} />      &lt;/View>    )  }}
```

### Styling our Book list

Our Book list just lists the name and author of each book, but we haven’t added any styling to it yet. Let’s do that using the `ListItem` component from `react-native-elements`. This is a simple change:

```
// src/views/book/components/Book.js
```

```
import { ListItem } from 'react-native-elements'
```

```
export default observer(({ book }) => (  <ListItem    avatar={{ uri: book.image }}    title={book.title}    subtitle={`by ${book.authors.join(', ')}`}  />))
```

And here’s what our view looks like now:

![BookList with react-native-elements.png](./BookList with react-native-elements.png)

Here’s the [diff of our recent changes](https://github.com/qaiser110/ReactNative-Bookstore-App-Tutorial/commit/b3ec126149833056e4e417218eca2e674b3b272d).

### Add Book details

We’ll add a field `selectedBook` to our `BookStore` which will point to the selected Book model.

```
selectedBook: t.maybe(t.reference(Book))
```

We’re using a MST reference for our `selectedBook` observable. [References in MST stores](https://github.com/mobxjs/mobx-state-tree#references-and-identifiers) make it easy to make references to data and interact with it, while keeping the data normalized in the background.

We’ll also add an action to change this reference:

```
const selectBook = book => {  self.selectedBook = book}
```

When a user taps on a book in the `BookListView`, we want to navigate the user to the `BookDetail` screen. So we’ll create a `showBookDetail` function for this, and pass it as a prop to the child components:

```
// src/views/book/components/BookListView.jsconst showBookDetail = book => {  this.store.selectBook(book)  this.props.navigation.navigate('BookDetail')}
```

In the `Book` component, we call the above `showBookDetail` function on `onPress`event on the Book `ListItem`:

```
// src/views/book/components/Book.js
```

```
onPress={() => showBookDetail(book)}
```

Let’s now create the `BookDetailView` that will be displayed when a user presses a book:

```
// src/views/book/components/BookDetailView.js
```

```
export default observer(() => {  const store = BkStore()  const book = store.selectedBook
```

```
return (    <View>      <View>        <Card title={book.title}>          <View>            <Image              resizeMode="cover"              style={{ width: '60%', height: 300 }}              source={{ uri: book.image }}            />            <Text>Title: {book.title}</Text>            <Text>Genre: {book.genre}</Text>            <Text>No of pages: {book.pageCount}</Text>            <Text>Authors: {book.authors.join(', ')}</Text>            <Text>Published by: {book.publisher}</Text>          </View>        </Card>      </View>    </View>  )})
```

Previously we only had tabs, but now we want to show the detail when the user taps on a book. So we’ll export a `createStackNavigator` instead of exporting `createBottomTabNavigator` directly. The `createStackNavigator` will have two screens on the stack, the `BookList` and the `BookDetail` screen:

```
// src/views/book/index.jsexport default createStackNavigator({  BookList: BookListTabs,  BookDetail: BookDetailView,})
```

Note that we’re having the List view and the Detail view inside the `createStackNavigator`. This is because we want to share the the same `BookDetailView` only with different content (filtered books). If we wanted a different detail view to show up from different tabs, then we would have created two separate StackNavigators, and included them inside a TabNavigator. Something like this:

```
const TabStackA = createStackNavigator({  Main: MainScreen,  Detail: DetailScreen,});
```

```
const TabStackB = createStackNavigator({  Main: MainScreen,  Detail: DetailScreen,});
```

```
export default createBottomTabNavigator(  {    TabA: TabStackA,    TabB: TabStackB,  })
```

Here’s the [diff of our recent changes](https://github.com/qaiser110/ReactNative-Bookstore-App-Tutorial/commit/0a40ffd056eb160e07e24a0dd83ada953776c703).

### Styling the tabs

Our tab labels look a bit small, and are hitting the bottom of the screen. Let’s fix that by increasing the `fontSize` and adding some `padding`:

```
// src/views/book/index.js
```

```
const BookListTabs = observer(  createBottomTabNavigator(    {      All: BookListView,      Fiction: BookListView,      Nonfiction: BookListView,    },    {      navigationOptions: ({ navigation }) => ({        // ...      }),      tabBarOptions: {        labelStyle: {          fontSize: 16,          padding: 10,        },      },    }  ))
```

Let’s run our app, tap on a book, and the Book detail screen should be displayed with the book details. Here’s [the repo](https://github.com/qaiser110/ReactNative-Bookstore-App-Tutorial) of our finished app.

### Thank you for reading!

And that concludes our tutorial on creating a ReactNative application with MobX store. I hope you enjoyed the post and found it useful.

_Originally published at [qaiser.com.au](https://qaiser.com.au/react-native-tutorial)._

