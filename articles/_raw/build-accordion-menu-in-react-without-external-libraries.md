---
title: How to Build an Accordion Menu in React from Scratch – No External Libraries
  Required
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2021-03-15T22:52:29.000Z'
originalURL: https://freecodecamp.org/news/build-accordion-menu-in-react-without-external-libraries
coverImage: https://cdn-media-2.freecodecamp.org/w1280/604df0d628094f59be2558d6.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: null
seo_desc: 'There are many ways to use accordion menus, like displaying a list of FAQs,
  showing various menus and submenus, displaying the locations of a particular company,
  and so on.

  In this article, we''ll see how to build an accordion menu in React completely...'
---

There are many ways to use accordion menus, like displaying a list of FAQs, showing various menus and submenus, displaying the locations of a particular company, and so on.

In this article, we'll see how to build an accordion menu in React completely from scratch, step-by-step, without using any external libraries.

We will be using React Hooks syntax for building this application in React. So if you're new to React Hooks, check out my [Introduction to React Hooks](https://levelup.gitconnected.com/an-introduction-to-react-hooks-50281fd961fe?source=friends_link&sk=89baff89ec8bc637e7c13b7554904e54) article to learn the basics of Hooks.

**You can see the live demo of the application [here](https://react-accordion-demo.netlify.app/).**

So let's get started.

## Initial Project Setup

Create a new project using `create-react-app`

```javascript
npx create-react-app react-accordion-demo

```

Once the project is created, delete all files from the `src` folder and create `index.js`, `App.js`, and `styles.css` files inside the `src` folder. Also, create a new folder with the name `utils` inside the `src` folder.

Open the `styles.css` file and add the contents from [here](https://github.com/myogeshchavan97/react-accordion-demo/blob/master/src/styles.css) inside it.

## How to Create the Initial Pages

Open the `src/App.js` file and add the following content inside it:

```jsx
import React from 'react';

const App = () => {
  const accordionData = {
    title: 'Section 1',
    content: `Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quis sapiente
      laborum cupiditate possimus labore, hic temporibus velit dicta earum
      suscipit commodi eum enim atque at? Et perspiciatis dolore iure
      voluptatem.`
  };

  const { title, content } = accordionData;

  return (
    <React.Fragment>
      <h1>React Accordion Demo</h1>
      <div className="accordion">
        <div className="accordion-item">
          <div className="accordion-title">
            <div>{title}</div>
            <div>+</div>
          </div>
          <div className="accordion-content">{content}</div>
        </div>
      </div>
    </React.Fragment>
  );
};

export default App;

```

Here, we use the `accordionData` object properties to display the accordion content.

For the `content` property we use ES6 template literal syntax (``) so we can spread the content across multiple lines, and we've used some dummy lorem ipsum text.

Now, open the `src/index.js` file and add the following content inside it:

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './styles.css';

ReactDOM.render(<App />, document.getElementById('root'));

```

Now, if you run the application using the `yarn start` command from the terminal, you will see the following screen:

![Initial Accordion](https://gist.github.com/myogeshchavan97/98ae4f4ead57fde8d47fcf7641220b72/raw/92ab4961521a20180285b6fdf5179b6d17fbcdff/accordion_initial.png)

## How to Open and Close the Accordion Menu

As you can see above, we display a single section as a part of the accordion. But by default, the accordion is expanded and we can't close it. So let's add functionality to open and close the accordion.

Add a new state inside the component as shown below:

```js
const [isActive, setIsActive] = useState(false);

```

Here, we've defined the `isActive` state. Based on that, we'll hide or show the accordion content.

Also import the `useState` hook at the top of the file:

```js
import React, { useState } from 'react';

```

Now, for the `div` with class `accordion-title`, add the `onClick` handler like this:

```jsx
<div className="accordion">
  <div className="accordion-item">
    <div
      className="accordion-title"
      onClick={() => setIsActive(!isActive)}
    >
      <div>{title}</div>
      <div>{isActive ? '-' : '+'}</div>
    </div>
    {isActive && <div className="accordion-content">{content}</div>}
  </div>
</div>

```

Here, we're inverting the `isActive` state value when we click on the `accordion-title` div. If the value of `isActive` is `false`, we're setting it to `true` and vice-versa.

We're also showing the `+` or `-` sign depending on the value of `isActive` using the ternary operator.

And if the `isActive` state value is `true` then we're only showing the accordion content as shown below:

```jsx
{isActive && <div className="accordion-content">{content}</div>}

```

Now, if you check the application, you will see the following screen:

![Open and close accordion](https://gist.github.com/myogeshchavan97/98ae4f4ead57fde8d47fcf7641220b72/raw/92ab4961521a20180285b6fdf5179b6d17fbcdff/open_close.gif)

As you can see, initially, the accordion is closed. When we click on the title, the accordion opens and we can click on it again to close it.

## How to add Multiple Sections in Accordion

This works fine for a single section of the accordion. But if we have multiple sections, it will not be good to copy-paste the same JSX code again and again with different content.

So let's create a separate component to just display the accordion. Then based on the number of sections, we'll loop over the component to display multiple sections.

Create a new `Accordion.js` file inside the `src` folder and add the following contents inside it:

```jsx
import React, { useState } from 'react';

const Accordion = ({ title, content }) => {
  const [isActive, setIsActive] = useState(false);

  return (
    <div className="accordion-item">
      <div className="accordion-title" onClick={() => setIsActive(!isActive)}>
        <div>{title}</div>
        <div>{isActive ? '-' : '+'}</div>
      </div>
      {isActive && <div className="accordion-content">{content}</div>}
    </div>
  );
};

export default Accordion;

```

Here, we've moved the state and `accordion-item` div from the `App.js` file into `Accordion.js`. We're passing the dynamic `title` and `content` props to the component using ES6 destructuring syntax like this:

```js
const Accordion = ({ title, content }) => {

```

Now, open the `App.js` file and replace it with the following content:

```jsx
import React from 'react';
import Accordion from './Accordion';

const App = () => {
  const accordionData = [
    {
      title: 'Section 1',
      content: `Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quis sapiente
      laborum cupiditate possimus labore, hic temporibus velit dicta earum
      suscipit commodi eum enim atque at? Et perspiciatis dolore iure
      voluptatem.`
    },
    {
      title: 'Section 2',
      content: `Lorem ipsum, dolor sit amet consectetur adipisicing elit. Mollitia veniam
      reprehenderit nam assumenda voluptatem ut. Ipsum eius dicta, officiis
      quaerat iure quos dolorum accusantium ducimus in illum vero commodi
      pariatur? Impedit autem esse nostrum quasi, fugiat a aut error cumque
      quidem maiores doloremque est numquam praesentium eos voluptatem amet!
      Repudiandae, mollitia id reprehenderit a ab odit!`
    },
    {
      title: 'Section 3',
      content: `Sapiente expedita hic obcaecati, laboriosam similique omnis architecto ducimus magnam accusantium corrupti
      quam sint dolore pariatur perspiciatis, necessitatibus rem vel dignissimos
      dolor ut sequi minus iste? Quas?`
    }
  ];

  return (
    <div>
      <h1>React Accordion Demo</h1>
      <div className="accordion">
        {accordionData.map(({ title, content }) => (
          <Accordion title={title} content={content} />
        ))}
      </div>
    </div>
  );
};

export default App;

```

Here, we've converted the `accordionData` from an object to an array of objects. We're looping over it using the array map method, and passing the corresponding `title` and `content` to the `Accordion` component.

Now if you check the application, you will see that the three sections get displayed and we can open and close each section as shown below:

![final working accordion](https://gist.github.com/myogeshchavan97/98ae4f4ead57fde8d47fcf7641220b72/raw/92ab4961521a20180285b6fdf5179b6d17fbcdff/final_working.gif)

## How to Refactor the Code

So as you can see, by just moving the accordion section out into a separate component and passing the dynamic content as props, we're successfully able to create a working version of an accordion from scratch.

It's a better practice to keep the static data in a separate file. So let's move the `accordionData` array to a different file and import it into `App.js`.

Create a new file called `content.js` inside the `utils` folder and add the following content inside it:

```js
export const accordionData = [
  {
    title: 'Section 1',
    content: `Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quis sapiente
    laborum cupiditate possimus labore, hic temporibus velit dicta earum
    suscipit commodi eum enim atque at? Et perspiciatis dolore iure
    voluptatem.`
  },
  {
    title: 'Section 2',
    content: `Lorem ipsum, dolor sit amet consectetur adipisicing elit. Mollitia veniam
    reprehenderit nam assumenda voluptatem ut. Ipsum eius dicta, officiis
    quaerat iure quos dolorum accusantium ducimus in illum vero commodi
    pariatur? Impedit autem esse nostrum quasi, fugiat a aut error cumque
    quidem maiores doloremque est numquam praesentium eos voluptatem amet!
    Repudiandae, mollitia id reprehenderit a ab odit!`
  },
  {
    title: 'Section 3',
    content: `Sapiente expedita hic obcaecati, laboriosam similique omnis architecto ducimus magnam accusantium corrupti
    quam sint dolore pariatur perspiciatis, necessitatibus rem vel dignissimos
    dolor ut sequi minus iste? Quas?`
  }
];

```

Now, open `App.js` and replace it with the following content:

```jsx
import React from 'react';
import Accordion from './Accordion';
import { accordionData } from './utils/content';

const App = () => {
  return (
    <div>
      <h1>React Accordion Demo</h1>
      <div className="accordion">
        {accordionData.map(({ title, content }) => (
          <Accordion title={title} content={content} />
        ))}
      </div>
    </div>
  );
};

export default App;

```

Here, we've just imported the static data from the external file and removed it from the `App.js` file.

So now the code looks clean and easy to understand and the functionality is working as before.

![final working accordion](https://gist.github.com/myogeshchavan97/98ae4f4ead57fde8d47fcf7641220b72/raw/92ab4961521a20180285b6fdf5179b6d17fbcdff/final_working.gif)

## Closing points

We're done building out the functionality of our app.

**You can find the complete GitHub source code for this application in [this repository](https://github.com/myogeshchavan97/react-accordion-demo).**

### Thanks for reading!

Want to learn all ES6+ features in detail including let and const, promises, various promise methods, array and object destructuring, arrow functions, async/await, import and export and a whole lot more from scratch?

Check out my [Mastering Modern JavaScript](https://modernjavascript.yogeshchavan.dev/) book. This book covers all the pre-requisites for learning React and helps you to become better at JavaScript and React.

<a href="https://modernjavascript.yogeshchavan.dev/" target="_blank"><img src="https://gist.github.com/myogeshchavan97/98ae4f4ead57fde8d47fcf7641220b72/raw/92ab4961521a20180285b6fdf5179b6d17fbcdff/freecodecamp_image.jpeg" alt="Mastering Modern JavaScript"></a>


