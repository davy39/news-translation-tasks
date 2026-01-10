---
title: What is Storybook and How Can I Use It to Create a Component Library in React?
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-06-09T14:45:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-storybook-and-how-can-i-use-it-to-create-a-component-libary-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/storybook.jpg
tags:
- name: components
  slug: components
- name: create-react-app
  slug: create-react-app
- name: Design Tools
  slug: design-tools
- name: Developer Tools
  slug: developer-tools
- name: framework
  slug: framework
- name: JavaScript
  slug: javascript
- name: Libraries
  slug: libraries
- name: React
  slug: react
- name: React
  slug: reactjs
- name: Storybook
  slug: storybook
- name: tools
  slug: tools
seo_title: null
seo_desc: "Frameworks like React, Vue, and Angular all help developers create modular\
  \ systems using components, but that doesn't usually include a good way to see them\
  \ all from a higher point of view. \nSo how can we use Storybook to build libraries\
  \ and design s..."
---

Frameworks like React, Vue, and Angular all help developers create modular systems using components, but that doesn't usually include a good way to see them all from a higher point of view. 

So how can we use Storybook to build libraries and design systems that self-document as we build them?

* [What is Storybook?](#heading-what-is-storybook)
* [What are we going to build?](#heading-what-are-we-going-to-build)
* [Step 0: Bootstrapping an app](#heading-step-0-bootstrapping-an-app)
* [Step 1: Installing Storybook](#heading-step-1-installing-storybook)
* [Step 2: Creating a new button](#heading-step-2-creating-a-new-button)
* [Step 3: Using our new Button component](#heading-step-3-using-our-new-button-component)
* [Repeat: Creating a new Header component](#heading-repeat-creating-a-new-header-component)
* [More Storybook features](#heading-more-storybook-features)

%[https://www.youtube.com/watch?v=VApXDsYO5Gg]

## What is Storybook?

[Storybook](https://storybook.js.org/) is a JavaScript tool that allows developers to create organized UI systems making both the building process and documentation more efficient and easier to use.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/loneley-planet-storybook-example.jpg)
_[Lonely Planet's Backpack UI]( https://lonelyplanet.github.io/backpack-ui/?path=/story/cards--card-basic)_

Once you build out a component, Storybook lets you create a "story" file where you can then import your component and create various use case examples in an iFramed sandbox using that component.

This provides an organized and focused environment to build new components and work on existing ones.

## What are we going to build?

We're going to bootstrap a new [React JS](https://reactjs.org/) app using [Create React App](https://reactjs.org/docs/create-a-new-react-app.html).

![Image](https://www.freecodecamp.org/news/content/images/2020/06/storybook-component-example.jpg)

Inside that app, we're going to install Storybook and create a few new components that will help us learn how to create new components that we can work on in a story and then use it in a React app.

## Step 0: Bootstrapping an app

To get started, we're going to start from scratch with [Create React App](https://reactjs.org/docs/create-a-new-react-app.html). This will help us focus on getting productive in Storybook rather than walking through integrating it into a current app.

That said, if you're already working with an app created using Create React App that's not ejected, you should be able to still follow on with Part 1 and beyond just the same!

So let's get started by navigating to where we want to create our new app and run the Create React App command:

```shell
npx create-react-app my-storybook

```

_Note: feel free to replace `my-storybook` with the directory name of your choice._

![Image](https://www.freecodecamp.org/news/content/images/2020/06/create-new-react-app.jpg)
_Bootstrapping with Create React App_

Once that's finished running, you can navigate to the directory:

```shell
cd my-storybook

```

And we're ready to go!

## Step 1: Installing Storybook

Storybook luckily makes it really easy to get started with a standard installation of React. Particularly with Create React App, Storybook automatically detects that we're using an app created using CRA and installs the dependencies and scaffolds everything for us.

### Initializing Storybook

To get started installing Storybook, run:

```shell
npx -p @storybook/cli sb init

```

![Image](https://www.freecodecamp.org/news/content/images/2020/06/initializing-storybook.jpg)
_Initializing Storybook in a React app_

If you aren't using Create React App or it didn't work, you can check out their [available guides in their docs](https://storybook.js.org/docs/guides/guide-react/).

After that's finished, all of our Storybook dependencies should be installed.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/storybook-finished-installing.jpg)
_Finished installing Storybook_

### Starting up Storybook

So now we're ready to get moving! Finally, run:

```shell
yarn storybook
# or
npm run storybook

```

And once everything finishes loading, Storybook will open a new tab in your browser and you should now see a welcome message inside of your new Storybook dashboard!

![Image](https://www.freecodecamp.org/news/content/images/2020/06/storybook-welcome-page.jpg)
_Storybook welcome page_

[Follow along with the commit!](https://github.com/colbyfayock/my-storybook/commit/3e994096384e31cb540150c9f14f41758ef3a746)

## Step 2: Creating a new button

If you took a second to poke around the dashboard, you might have noticed that it comes pre-loaded with a Button that's available as a demo.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/storybook-demo-button.jpg)
_Storybook demo button_

You should also notice if you click the button, you actually see an action print out inside of the Actions tab at the bottom. This shows the event that's captured from the button click.

It's simple, but this is great to get a nice feel about what to expect in storybook. The only issue is, this is meant purely for demonstration purposes, so let's build our own button to replace it.

### Creating a new Button component

To get started, let's first create a few directories:

* Under `src`, create a new folder called `components`
* Under `components`, create a new folder called `Button`

Once you create those folders, create a new file called `index.js` inside of your `src/components/Button` folder and inside add:

```js
// Inside src/components/Button/index.js

export { default } from './Button';

```

This will import the next file we created called `Button.js` which will allow us to more easily import our files with `src/components/Button` instead of `/src/components/Button/Button`.

Next, let's create `Button.js` right next to our `index.js` file with the following content:

```js
// Inside src/components/Button/Button.js

import React from 'react';

const Button = ({ children, ...rest }) => {
  return (
    <button className="button" {...rest}>
      { children }
    </button>
  )
}

export default Button;

```

Here, we're creating a new component called Button that adds a class of `button` to the element and passes through the `children`. We're a additionally [destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment) the rest of the props into the `rest` variable and [spreading](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax) that value into the `<button>` element.

If you've followed along, your files should now look like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/button-reaect-component.jpg)
_Button component in React_

### Using our new Button component

So now that we have our Button component, let's use it!

Open up the file `src/stories/1-Button.stories.js` and replace the line that's importing `Button` with:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/updating-button-storybook-story.jpg)
_Updating the Button Storybook story_

And once you hit save, you can open back up your browser tab with your Storybook dashboard, and you can now see a button that looks mostly similar, but it uses the browser's default styles for the `<button>` element. You'll even notice that if you click it, the event will still be logged under the Actions tab.

### Styling our Button component

Finally, we probably don't want to use the browser default styles, so let's make it look nice.

In our `src/components/Button` directory, add a new file `Button.css` and add the following content:

```css
/* Inside src/components/Button/Button.css */

.button {
  color: white;
  font-weight: bold;
  background-color: blueviolet;
  border: none;
  padding: .8em 1em;
  border-radius: .2rem;
}

```

This applies a few styles to our `.button` class like adding a background color and changing the font color to white.

But if you open Storybook, you'll notice it didn't do anything. To use it, we need to import it into our component.

Inside `src/components/Button/Button.js` add the following at the top under the React import:

```js
import './Button.css';

```

And once you save that and open up your browser, you should now see our new button with our updated styles!

![Image](https://www.freecodecamp.org/news/content/images/2020/06/new-button-storybook.jpg)
_New Button in Storybook_

[Follow along with the commit!](https://github.com/colbyfayock/my-storybook/commit/e71e0e9e666adee0455b0b69118053c2f551ab68)

## Step 3: Using our new Button component

The ultimate goal of our component is to use it right? So let's add it to our app.

### Switching over to the React app

First we'll need to either start our React app in a new terminal tab or kill the Storybook process and start the React process there. To start the React app using Create React App, run:

```shell
yarn start
# or
npm run start

```

Once that loads, we should have our standard Create React App if you're following along with me:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/new-create-react-app.jpg)
_New Create React App_

### Importing and using the new button

Next, inside of `src/App.js`, let's import our new Button at the top of the page:

```js
import Button from './components/Button';

```

With Button imported, we can use it. Here, we can simply add it anywhere we want in the page. I'm going to replace the Learn React link with:

```jsx
<p>
  <Button>Hello, Storybook!</Button>
</p>

```

And if we save and reload the page, we should now see our Button on the page!

![Image](https://www.freecodecamp.org/news/content/images/2020/06/create-react-app-with-new-button.jpg)
_New Button in Create React App_

[Follow along with the commit](https://github.com/colbyfayock/my-storybook/commit/e6071aae5be281101d486c4cc7664bf6cacb4028)

## Repeat: Creating a new Header component

The great thing about Storybook and React (or any of the supported frameworks) is that this process scales to as many components as you want.

So let's build another component!

### Creating our Header component

Similar to our Button, let's start off by creating the set of directories and files that give us our component.

Since we already did this once, I'm going to provide the code without walking through what's going on.

Let's start off by spinning back up our Storybook server with:

```
yarn storybook
# or 
npm run storybook

```

Create a `Header` directory inside the `src/components` directory.

Create an `index.js` file inside of `src/components/Header` with the following content:

```js
// In src/components/Header/index.js

export { default } from './Header';

```

Create a `Header.js` file inside of `src/components/Header` with the following content:

```jsx
// In src/components/Header/Header.js

import React from 'react';
import './Header.css';

const Header = ({ children }) => {
  return (
    <h2 className="header">
      { children }
    </h2>
  )
}

export default Header;

```

Create a `Header.css` file inside of `src/components/Header` with the following content:

```css
/* In src/components/Header/Header.css */

.header {
  font-family: sans-serif;
  font-size: 2.5em;
  color: blueviolet;
  border-bottom: solid 5px aqua;
  padding-bottom: .2em;
  box-shadow: 0 5px 0 blueviolet;
}

```

Now if you notice, if you try to open up Storybook, again, nothing will happen. This time we need to create a new story file.

### Creating a new Story file

Inside `src/stories`, add a new file called `2-Header.stories.js`:

```jsx
// Inside src/stories/2-Header.stories.js

import React from 'react';

import Header from '../components/Header';

export default {
  title: 'Header',
  component: Header,
};

export const Text = () => <Header>Hello Header</Header>;

```

Here's a breakdown of our story file:

* First, we import our component – this is pretty standard any time we want to use it
* The first thing we export is a `default` object. With Storybook, it expects the default export to be the configuration of our story, so here we provide it with a title and we pass in the component that we're using for this story
* The second and last thing we export is the `Text` constant. With Storybook, any non-default export will be considered a variation that will get nested under the title that you provide in the default export

And if you save this file and open up your Storybook dashboard in the browser, you should now see the new header!

![Image](https://www.freecodecamp.org/news/content/images/2020/06/new-header-storybook-story.jpg)
_New Header component in Storybook_

### Using the Header component

Using our component is just the same as our Button component, so inside of `src/App.js`, let's add our Header.

After starting your React server, first import our new Header:

```js
// In src/App.js

import Header from './components/Header';

```

Then add it to the top of the page:

```jsx
// In src/App.js

<Header>My App</Header>

```

And if you open the page, we'll see our new Header!

![Image](https://www.freecodecamp.org/news/content/images/2020/06/create-react-app-with-header-and-button.jpg)
_Create React App with new Header and Button components_

[Follow along with the commit!](https://github.com/colbyfayock/my-storybook/commit/e1c59eccaf5f4146a2fe039dca8874609d615194)

## Adding more components

As you've noticed with our second Repeat step – adding a new component is pretty much the same process for any type of component we want to add. Once we have it in our library, we can develop it in a focused environment and then import it to our app to use.

You can now use this to manage your library of components and better maintain an entire system for your project!

## More Storybook features

Storybook doesn't stop with just adding components, it provides the ability to configure [Addons](https://storybook.js.org/addons/) that enhance the core capabilities opening up a lot of possibilities.

Here are some of my favorites...

### Story Source

When building a component system, the hope is that people can easily use these components. But if you don't have documentation, someone would have to open up the file or try to find another use example.

Instead, [Story Source](https://github.com/storybookjs/storybook/tree/master/addons/storysource) shows the code source of the story file you created allowing someone browsing your Storybook dashboard to get an example right along with the component output!

![Image](https://www.freecodecamp.org/news/content/images/2020/06/storybook-source-demo.gif)
_Storybook Story Source demo_

### Storyshots

If you're a fan of automated testing, you might have heard of using [Jest](https://jestjs.io/) or another tool for adding snapshot testing to your app.

[StoryShots](https://github.com/storybookjs/storybook/tree/master/addons/storyshots/storyshots-core) is a way to easily add Jest snapshot testing to your component system. It creates snapshots based off of the stories you create so you can make sure that your components aren't fundamentally changing (or breaking) during development.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/storybook-snapshot-example.jpg)
_Snapshot example with StoryShots_

## What's your favorite part of Storybook?

[Share with me on Twitter!](https://twitter.com/colbyfayock)

## Continue the conversation!

%[https://twitter.com/colbyfayock/status/1270392710260719616]

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?️ Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">✉️ Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>

