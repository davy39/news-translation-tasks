---
title: How to Build a Stepper Component in React
subtitle: ''
author: Olabisi Olaoye
co_authors: []
series: null
date: '2024-01-10T15:28:54.000Z'
originalURL: https://freecodecamp.org/news/build-a-stepper-component-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/Your-paragraph-text-3.png
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: null
seo_desc: I was working on a React project recently, and I realized that there were
  so many UI components that I had to build to get things done quickly. So I began
  to explore a lot of UI libraries like Material UI or Chakra UI. Then I started wondering
  why I ...
---

I was working on a React project recently, and I realized that there were so many UI components that I had to build to get things done quickly. So I began to explore a lot of UI libraries like [Material UI](https://mui.com) or [Chakra UI](https://chakra-ui.com/). Then I started wondering why I hadn't attempted to build some of these components myself. 

So, I decided to embark on an adventure to build as many components as I could. Sure, it would take more time, but I would get to learn how these components are being built.

In this guide, you'll learn how to build a stepper, a UI component that guides a user through a process by dividing it into a number of steps. We'll achieve this with React and Tailwind CSS, an open-source, utility-first CSS framework which allows you to style your HTML directly without having to open a `.css` file. 

Here are some prerequisites you need before you can effectively follow this guide:

* Familiarity with HTML, CSS, and JavaScript
* Knowledge of React fundamentals

## How to Set Up the Project

First, you need to create a React project. In the terminal of your text editor and at your chosen directory, type in this command:

```bash
npx create-react-app my-stepper
```

Next, install Tailwind CSS in your project with this command:

```bash
npm install -D tailwindcss
```

When this is done, a tailwind.config.js file is automatically created for you in the root directory of the project. It initially contains no config in particular, so you'll have to add the paths to your template files like this:

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

## How to Build the Stepper Layout

Next, create a Stepper component in the `src` directory of your project. It should be able to move to the next step by showing some visible color change or helper text, or both. For example, an inactive step can be gray in color and an active step can be blue. 

Basically, we should be able to move back and forth between steps. The layout will only involve a circle and a connector line for now, but later some JavaScript will help to replicate the circles and connector lines depending on how many steps the stepper will consist of.

```javascript
//Stepper.js
export default function Stepper () {
    return (
        <div className="flex items-center">
            <div className="rounded-full bg-blue-500 w-6 h-6"></div>
            <span className="h-1 w-8 bg-blue-500"></span>
        </div>
    )
}
```

In the code block above, I styled the basic stepper look: a rounded circle with a blue background, and a short line right beside it. They will both be replicated, depending on the number of steps you want to show.

For the purpose of this guide, you can add two buttons in the `App` component to switch back and forth between steps. Then the Stepper component can be rendered just above them like this:

```javascript
//App.js
import { useState } from 'react';
import Stepper from './Stepper';

export default function App()  {
    return (
        <main>
            <Stepper />
            <div>
                <button>Previous step</button>
                <button>Next step</button>
            </div>
        </main>
    )
}
```

## How to Add Functionality to the Stepper

To make a basic stepper work, there are two things to take note of: how many steps there are in total, and what the current step is. 

If you're dealing with five steps, for instance, you need to know which step is the active one. This means that you'll need these two bits of information inside the `Stepper` component in the form of props. 

From the total number of steps passed into the component, you can generate a group of circles and connector lines that number of times. You can use JavaScript's inbuilt `Array.from()` function to create an array of steps like this:

```javascript
export default function Stepper ({currentStep, numberOfSteps}) {
    return (
        <div className="flex items-center">
        {Array.from({length: numberOfSteps}).map((_, index) => (
        	<React.Fragment key={index}>
          		<div className={`w-6 h-6 rounded-full`}></div>
				<div className={`w-12 h-1`}></div> 
        	</React.Fragment>
      	))}
        </div>
    )
}
```

In the code block above, I used `React.Fragment` so I wouldn't have to wrap the circle div and the connector div in a redundant div (JSX expressions must have only one parent element). 

Also, when mapping the array, I used the `_` symbol as the first parameter in the `map` function because we don't need it. It's more of a 'throwaway' parameter that we don't use because we just need to access the index parameter of the array.

Let's do a bit of styling. Each active step has to have some distinct color to indicate to the user that it's the current step in the component. 

To implement this, create an `activeColor` function that takes in as an argument the current index of the array generated from `Array.from()`, and compares it with the `currentStep` variable. If the current index matches the current step, a distinct color is used, otherwise an inactive color is used.

```javascript
const activeColor = (index) => currentStep === index ? "bg-blue-500" : "bg-gray-300"
```

The condition incorporated in the `activeColor` function above states, in simple terms, "at this point in our array of steps, are we at the current step? If so, the step color is blue. Otherwise, it's gray." 

Now, add that line of code to the `Stepper` component and call the function in the class name of each circle and connector line.

```javascript
export default function Stepper ({currentStep, numberOfSteps}) {
  const activeColor = (index) => currentStep >= index ? 'bg-blue-500' : 'bg-gray-300'

  return (
    <div className="flex items-center">
      {Array.from({length: numberOfSteps}).map((_, index) => (
        <React.Fragment key={index}>
          <div className={`w-6 h-6 rounded-full ${activeColor(index)}`}>  
          </div>
		  <div className={`w-12 h-1 ${activeColor(index)}`}></div>
        </React.Fragment>
      ))}
    </div>
  )
}
```

There's a bit of a problem, though. Because the circle and connector line is just being replicated with respect to the number of steps, this is the current result:  


![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-167.png)
_Stepper showing the extra connector line at the end_

There's an extra connector line at the end – but we can easily fix this by conditionally rendering it. The condition will simply check whether the current index in the array is on the final step. If so, then there's no need to render a connector line. This way, that lone connector line disappears on the last step. 

```javascript
const isFinalStep = (index) => index === numberOfSteps - 1
```

So when I call this function in the `Stepper` component's JSX, the connector line will only be displayed if that step isn't the current index of the array isn't equal to the number of steps (minus one, since we are working with a zero-indexed array). The `Stepper` component, all finished, will then look like this:

```javascript
import React from 'react';

export default function Stepper ({currentStep, numberOfSteps}) {
  const activeColor = (index) => currentStep >= index ? 'bg-blue-500' : 'bg-gray-300'
  const isFinalStep = (index) => index === numberOfSteps - 1

  return (
    <div className="flex items-center">
      {Array.from({length: numberOfSteps}).map((_, index) => (
        <React.Fragment key={index}>
          <div className={`w-6 h-6 rounded-full ${activeColor(index)}`}></div>
          {isFinalStep(index) ? null : <div className={`w-12 h-1 ${activeColor(index)}`}></div>}
        </React.Fragment>
      ))}
    </div>
  )
}
```

## How to Pass in the Props

Since the `Stepper` component accepts `currentStep` and `numberOfSteps` as props, these two need to be defined in the `App` component. 

Remember, the current step changes, so it needs to be tracked. You can use React's `useState` hook for this. The initial state is set to zero, which is the first step. For the purpose of this guide, I'll be using five steps.

```javascript
//App.js

export default function App() {
    const [currentStep, setCurrentStep] = React.useState(0)
    const NUMBER_OF_STEPS = 5

    return (
        //...some code
        <Stepper currentStep={currentStep} numberOfSteps={NUMBER_OF_STEPS}/>
        //...some code
    )
}
```

## How to Move Back and Forth Between Steps

The last thing left to do is to add some functionality to those two buttons in the `App` component. 

Create two functions, `goToPreviousStep` and `goToNextStep`, which will simply decrement or increment the current step state. 

To prevent the previous button from decrementing past zero, since the first step has an index of zero, you can add a condition to check whether the current step is greater than or equal to zero. That will be the lower boundary of the stepper. 

For the next button, the current step should not go past the number of steps minus one, since we are dealing with a [zero-indexed](https://en.wikipedia.org/wiki/Zero-based_numbering) array.

Here's the final code for the `App` component:

```javascript
import React from 'react';
import Stepper from './Stepper';

export default function App() {
  const [currentStep, setCurrentStep] = React.useState(0)
  const NUMBER_OF_STEPS = 5

  const goToNextStep = () => setCurrentStep(prev => prev === NUMBER_OF_STEPS - 1 ? prev : prev + 1)
  const goToPreviousStep = () => setCurrentStep(prev => prev <= 0 ? prev : prev - 1)

  return (
    <div>
      <h1 className="text-2xl">Here is the stepper in action!</h1>
      <br/>
      <Stepper currentStep={currentStep} numberOfSteps={NUMBER_OF_STEPS}/>
      <br/>
      <section className="flex gap-10">
        <button 
		  onClick={goToPreviousStep} 
		  className="bg-blue-600 text-white p-2 rounded-md"
		>
          Previous step
        </button>
        <button 
		  onClick={goToNextStep} 
		  className="bg-blue-600 text-white p-2 rounded-md"
		>
          Next step
      	</button>
      </section>
    </div>
  );
}

```

And that's it! You've successfully built a stepper component in a React project. You can play around with this [working demo on Stackblitz](https://stackblitz.com/edit/stackblitz-starters-ga6rgw?file=src%2FApp.js). Please let me know your thoughts and suggestions about this article.

Bonus: You can take this code up a notch by adding labels and descriptions to each step.

Thanks for reading!

