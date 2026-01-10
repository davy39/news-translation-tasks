---
title: How to Build an Interactive Accordion Component with React and GSAP
subtitle: ''
author: David Jaja
co_authors: []
series: null
date: '2023-04-25T15:47:34.000Z'
originalURL: https://freecodecamp.org/news/build-an-interactive-accordion-component-with-react-and-gsap
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Cover-image-1.png
tags:
- name: animation
  slug: animation
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "As websites become more sophisticated and user expectations continue to\
  \ rise, web developers must search for ways to create more engaging and interactive\
  \ user interfaces. \nOne powerful tool in a developer's arsenal is the accordion\
  \ component, a versa..."
---

As websites become more sophisticated and user expectations continue to rise, web developers must search for ways to create more engaging and interactive user interfaces. 

One powerful tool in a developer's arsenal is the accordion component, a versatile and widely-used element found on nearly every website. 

In this article, we'll explore how to create a dynamic and visually-stunning accordion component using React and the GreenSock Animation Platform library (GSAP). 

By combining the flexibility of React with the animation capabilities of GSAP, we'll craft a seamless and immersive user experience that will leave your visitors wanting more. So buckle up and get ready to advance your web development skills!

## Prerequisites

* Fundamentals of HTML and CSS
* Fundamentals of ES6 JavaScript
* Fundamentals of React and React Hooks.

## What We'll Cover:

1. [What is an accordion component?](#heading-what-is-an-accordion-component)
2. [The importance of accordion components in web design](#heading-the-importance-of-accordion-components-in-web-design)
3. [A quick overview of React and GSAP](#heading-a-quick-overview-of-react-and-gsap)
4. [How to set up your development environment](#heading-how-to-set-up-your-development-environment)
5. [Breakdown of the project](#heading-breakdown-of-the-project)  
– [The user interface section](#heading-the-user-interface-section)  
– [The functionality section](#heading-the-functionality-section)  
– [The animation section](#heading-the-animation-section)
6. [Conclusion](#heading-conclusion)

## What is an Accordion Component?

An accordion component is a UI element used to present a list of items in a compact manner. It consists of a vertical list of headers that expand and collapse their corresponding content when clicked. 

This type of component is helpful because it allows users to quickly scan a list and expand only relevant items.

## The Importance of Accordion Components in Web Design

Accordion components have become an essential part of modern web design, as they allow website developers to display large amounts of information in a compact and organized way.  

Accordion components are particularly useful for content-heavy websites where users may become overwhelmed by too much information on a single page. 

They also serve uses such as:

* Navigation: Accordion components provide a simple and intuitive way for users to navigate through a website. By organizing content into collapsible sections, users can quickly find what they are looking for, without having to scroll through long pages.
* Space-saving: Accordion components help save screen real estate by allowing website designers and developers to display multiple sections of content in a compact form factor. This is particularly important for mobile devices, where screen real estate is limited.
* User experience: Accordion components can help improve the user experience by reducing clutter and making it easier for users to find the information they need. By keeping the user interface clean and organised, users are less likely to become overwhelmed or frustrated. Additionally, the interactive nature of accordion components can make the user experience more engaging and enjoyable.

## A Quick Overview of React and GSAP

React is a JavaScript framework that streamlines the creation of dynamic user interfaces. It achieves this by enabling developers to create individual, reusable components that can be pieced together to form intricate and interactive interfaces. 

This process involves breaking down the interface into smaller components that are more manageable and can be updated independently without affecting the entire UI.

GSAP, also known as GreenSock Animation Platform, is a JavaScript library designed to create high-quality animations and interactive experiences on the web. 

This library offers a comprehensive set of tools to produce animations that are visually appealing and optimized for performance. With GSAP, developers can create animations with precision and have complete control over the animation's behaviour.

When used together, React and GSAP can create highly interactive and visually stunning user interfaces, such as accordion components. React provides the framework for creating the accordion component, while GSAP provides the tools for animating the component and making it interactive.

## How to Set Up Your Development Environment

Before you can begin creating components in a React application, you need to set up your development environment. This includes installing [Node.js](https://nodejs.org/en/download) and [npm](https://www.npmjs.com/package/download) (Node Package Manager) on your computer.

### How to Create a React Project

After installing Node.js and npm, you can use the Create React App command-line tool to create a new React project. In your local terminal, run the command:

npx create-react-app react-gsap-dropdown

Then, open that folder with your code editor. This is what it should look like:

![Image](https://www.freecodecamp.org/news/content/images/2023/04/001---Initial-view-after-cra.png)
_Initial view after creating react app_

**Note**: I'll be using the [VSCode Editor](https://code.visualstudio.com/download) for development in this tutorial, but any modern text editor should be sufficient.

Following that, remove all of the boilerplate styles and unnecessary files from your app.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/002---After-clearing-clutter-files.PNG)
_After clearing clutter files and styles_

The next step in the setup process is to install GSAP in your React app. Simply open the terminal in your code editor and run:

npm install gsap

![Image](https://www.freecodecamp.org/news/content/images/2024/04/installing-gsap.png)
_Installing gsap_

All that remains is to run `npm start`, which launches a development server in your browser and displays a blank page.

## Breakdown of the Project

Before you begin building your project, it is important to understand that it is divided into three parts:

* The User Interface section
* The Functionality section
* The Animation section

### The User Interface Section

This section includes all of the mockups and styling needed to render your component on the page. Here’s a step-by-step of this section’s progress

First, create a parent element in your App component called `accordion__container`_._ This element holds all the accordion items you wish to create.

Next, create three child items representing each accordion item which you would make expandable based on user interaction. So far your code structure should look something like this;

```html
<div className="App">
    <div className="accordion__container">
       <div className="accordion__item"></div>
       <div className="accordion__item"></div>
       <div className="accordion__item"></div>
    </div>
</div>
```

In each accordion item, nest two child elements, the `accordion__header` and `accordion__details`. The `accordion__header` will hold the information displayed when the `accordion__item` is compact, and the `accordion__details` will hold the information when it’s expanded.

```html
<div className="App">
    <div className="accordion__container">
       <div className="accordion__item"> 
          <div className="accordion__header"></div>
          <div className="accordion__details"></div>
       <div className="accordion__item">
          <div className="accordion__header"></div>
          <div className="accordion__details"></div>
       </div>
       <div className="accordion__item"> 
          <div className="accordion__header"></div>
          <div className="accordion__details"></div>
       </div>
    </div>
</div>
```

Adding content to both child elements gives you the following code:

```html
<div className="accordion__container">
        <div className="accordion__item">
          <div className="accordion__header">
            <p className="accordion__number">01</p>
            <p className="accordion__name">The World's Tallest Building</p>
          </div>

          <div className="accordion__details">
            <ul>
              <li>
                The current tallest building in the world is the Burj Khalifa,
                located in Dubai, United Arab Emirates.
              </li>
              <li>
                It stands at a height of 828 meters (2,716 feet) tall and has
                163 floors.
              </li>
              <li>
                The building took six years to construct and was completed in
                2010.
              </li>
            </ul>
          </div>
        </div>

        <div className="accordion__item">
          <div className="accordion__header">
            <p className="accordion__number">02</p>
            <p className="accordion__name">
              Famous Inventors and Their Inventions
            </p>
          </div>
          <div className="accordion__details">
            <ul>
              <li>
                Nikola Tesla, a Serbian-American inventor, is credited with the
                invention of the AC (alternating current) electrical system.
              </li>
              <li>
                Thomas Edison, an American inventor, is credited with the
                invention of the light bulb.
              </li>
              <li>
                Alexander Graham Bell, a Scottish-born American inventor, is
                credited with the invention of the telephone.
              </li>
            </ul>
          </div>
        </div>
        <div className="accordion__item">
          <div className="accordion__header">
            <p className="accordion__number">03</p>
            <p className="accordion__name">Largest Deserts in the World</p>
          </div>
          <div className="accordion__details">
            <ul>
              <li>
                The Sahara Desert, located in Africa, is the largest hot desert
                in the world and covers an area of 9.2 million square kilometers
                (3.6 million square miles).
              </li>
              <li>
                The Antarctic Desert, located in Antarctica, is the largest cold
                desert in the world and covers an area of 14 million square
                kilometers (5.4 million square miles).
              </li>
              <li>
                The Arabian Desert, located in the Middle East, is the
                third-largest desert in the world and covers an area of 2.33
                million square kilometers (900,000 square miles).
              </li>
            </ul>
          </div>
        </div>
      </div>
```

We added a `number` and `name` element to the `accordion__header` element, and an unordered list with list items to the `accordion__details` element.

Taking a look at the component in your browser, you should see this:

![Image](https://www.freecodecamp.org/news/content/images/2023/04/004---Initial-component-render-with-no-styling.png)
_Initial component render with no styling_

At the moment, your component doesn’t look like much, so add the styling below.

```css

@import url("https://fonts.googleapis.com/css2?family=Dongle:wght@300;400&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
body {
  font-family: "Dongle", sans-serif;
}
.App {
  min-height: 100vh;
  display: flex;
  justify-content: center;
}
.accordion__container {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-top: 25px;
}
.accordion__item {
  display: flex;
  flex-direction: column;
  width: 750px;
  box-shadow: 0 0 32px rgba(0, 0, 0, 0.1);
  border-top: 4px solid transparent;
}
.accordion__header {
  display: flex;
  gap: 2rem;
  align-items: center;
  cursor: pointer;
  padding: 1rem 2rem;
}
.accordion__header:hover {
  background: #e7eaed;
}
.accordion__number {
  font-size: 40px;
  color: #ced4da;
}
.accordion__name {
  flex: 1;
  font-size: 40px;
}
.accordion__details {
  padding: 0 2rem;
}
.accordion__details ul {
  font-size: 30px;
  padding: 1rem 2rem;
  list-style-type: circle;
}
```

This styling gives the `accordion__container` a fixed width and uses some Flexbox techniques together with basic CSS to give the component a nicer-looking appearance.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/005---Component-with-stylings-applied-1.png)
_Rendered component with styling added_

As you can see, your component is already well laid out and more appealing to users. But all the details of each accordion item are visible without any human interaction. 

To solve this, you'll want to hide all the content in each `accordion__details` container by reducing its height and hiding any overflow.

```css
.accordion__details {
  overflow: hidden;
  height: 0;
}
```

This code produces this result:

![Image](https://www.freecodecamp.org/news/content/images/2023/04/006--Component-after-hiding-details.PNG)
_Component after hiding details_

With this, you’ve concluded the interface section and can now move on to dynamically revealing the content of any accordion item you click on.

### The Functionality Section

In this section, we’re going to tackle the following:

* Dynamically display the details of each accordion based on a user’s click.
* Ensure only one accordion tab is open at a time

Starting off, create an `open` class which will contain styles that only the currently clicked accordion will have. This class will be added to any accordion item you click on.

```css
.open {
  border-color: #087f5b;
}

.open .accordion__header,
.open .accordion__number {
  color: #087f5b;
}

.open .accordion__details {
  height: auto;
}
```

Then you'll create a variable with the `useState` hook. This hook is used to hold the current state of an accordion item (that is, if it’s open or not).

```js
const [openAccordion, setOpenAccordion] = useState(null);
```

After that, create a callback function that takes in a distinct index value from each `accordion__item` and compares it with the value in your state variable (`openAccordion`). The way the function works is, if the index value is distinct from the `openAccordion` value, the function sets the `openAccordion` value to the index value, else it sets the `openAccordion` to null.

```js
 const handleAccordionClick = (index) => {
    if (index !== openAccordion) {
        setOpenAccordion(index);
     } else {
       setOpenAccordion(null);
    }
  };
```

This logic is used to conditionally render a class in your markup (that is, add or remove a class based on the item you click on). To make this function work, you use an `onClick` event on each `accordion__header`, and call each `handleAccordionClick` with a distinct `index` value.

```js
<div className="accordion__container">
        <div className="accordion__item">
          <div
            className="accordion__header"
             // HERE
            onClick={() => handleAccordionClick(0)}
          >
            <p className="accordion__number">01</p>
            <p className="accordion__name">The World's Tallest Building</p>
          </div>

          <div className="accordion__details">
            <ul>
              <li>
                The current tallest building in the world is the Burj Khalifa,
                located in Dubai, United Arab Emirates.
              </li>
              <li>
                It stands at a height of 828 meters (2,716 feet) tall and has
                163 floors.
              </li>
              <li>
                The building took six years to construct and was completed in
                2010.
              </li>
            </ul>
          </div>
        </div>

        <div className="accordion__item">
          <div
            className="accordion__header"
             // HERE
            onClick={() => handleAccordionClick(1)}
          >
            <p className="accordion__number">02</p>
            <p className="accordion__name">
              Famous Inventors and Their Inventions
            </p>
          </div>
          <div className="accordion__details">
            <ul>
              <li>
                Nikola Tesla, a Serbian-American inventor, is credited with the
                invention of the AC (alternating current) electrical system.
              </li>
              <li>
                Thomas Edison, an American inventor, is credited with the
                invention of the light bulb.
              </li>
              <li>
                Alexander Graham Bell, a Scottish-born American inventor, is
                credited with the invention of the telephone.
              </li>
            </ul>
          </div>
        </div>
        <div className="accordion__item">
          <div
            className="accordion__header"
            // HERE
            onClick={() => handleAccordionClick(2)}
          >
            <p className="accordion__number">03</p>
            <p className="accordion__name">Largest Deserts in the World</p>
          </div>
          <div className="accordion__details">
            <ul>
              <li>
                The Sahara Desert, located in Africa, is the largest hot desert
                in the world and covers an area of 9.2 million square kilometers
                (3.6 million square miles).
              </li>
              <li>
                The Antarctic Desert, located in Antarctica, is the largest cold
                desert in the world and covers an area of 14 million square
                kilometers (5.4 million square miles).
              </li>
              <li>
                The Arabian Desert, located in the Middle East, is the
                third-largest desert in the world and covers an area of 2.33
                million square kilometers (900,000 square miles).
              </li>
            </ul>
          </div>
        </div>
      </div>

```

To confirm your logic, log both the `openAccordion` value and the `index` value to the console, and click on each accordion item.

```js
  const handleAccordionClick = (index) => {
    console.log(openAccordion, index);
    if (index !== openAccordion) {
      setOpenAccordion(index);
    } else {
      setOpenAccordion(null);
    }
  };
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Testing-for-switching-logic.gif)
_Testing the accordion logic_

As you can see, clicking on the first item logs the current value of the `openAccordion` (null) and the current index (0) to the console. It also sets the value of `openAccordion` to the current index_._ 

When you click on the next item, you notice that the `openAccordion` value was set to the previous index, implying that the value of the `openAccordion` was conditionally altered based on the user’s click.

Finally, clicking on the same element twice first sets the `openAccordion` to that element’s index, then to `null` since the else block of the function is fired when `openAccordion === index`_._ 

To show the content of each `accordion__item`, use a ternary operator to conditionally add the open class to each item.

```js
<div className="App">

      <div className="accordion__container">
        <div
        // HERE
          className={`accordion__item  ${openAccordion === 0 ? "open" : ""}`}
        >
          <div
            className="accordion__header"
            onClick={() => handleAccordionClick(0)}
          >
            <p className="accordion__number">01</p>
            <p className="accordion__name">The World's Tallest Building</p>
          </div>

          <div className="accordion__details">
            <ul>
              <li>
                The current tallest building in the world is the Burj Khalifa,
                located in Dubai, United Arab Emirates.
              </li>
              <li>
                It stands at a height of 828 meters (2,716 feet) tall and has
                163 floors.
              </li>
              <li>
                The building took six years to construct and was completed in
                2010.
              </li>
            </ul>
          </div>
        </div>

        <div
        // HERE
          className={`accordion__item  ${openAccordion === 1 ? "open" : ""}`}
        >
          <div
            className="accordion__header"
            onClick={() => handleAccordionClick(1)}
          >
            <p className="accordion__number">02</p>
            <p className="accordion__name">
              Famous Inventors and Their Inventions
            </p>
          </div>
          <div className="accordion__details">
            <ul>
              <li>
                Nikola Tesla, a Serbian-American inventor, is credited with the
                invention of the AC (alternating current) electrical system.
              </li>
              <li>
                Thomas Edison, an American inventor, is credited with the
                invention of the light bulb.
              </li>
              <li>
                Alexander Graham Bell, a Scottish-born American inventor, is
                credited with the invention of the telephone.
              </li>
            </ul>
          </div>
        </div>
        <div
        // HERE
          className={`accordion__item  ${openAccordion === 2 ? "open" : ""}`}
        >
          <div
            className="accordion__header"
            onClick={() => handleAccordionClick(2)}
          >
            <p className="accordion__number">03</p>
            <p className="accordion__name">Largest Deserts in the World</p>
          </div>
          <div className="accordion__details">
            <ul>
              <li>
                The Sahara Desert, located in Africa, is the largest hot desert
                in the world and covers an area of 9.2 million square kilometers
                (3.6 million square miles).
              </li>
              <li>
                The Antarctic Desert, located in Antarctica, is the largest cold
                desert in the world and covers an area of 14 million square
                kilometers (5.4 million square miles).
              </li>
              <li>
                The Arabian Desert, located in the Middle East, is the
                third-largest desert in the world and covers an area of 2.33
                million square kilometers (900,000 square miles).
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>


```

The ternary operator checks if each `index` value matches the `openAccordion` value and adds the `open` class to the `accordion__item` if it does.

Testing your accordion component now gives the following result:

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Accordion-Working-without-animation-1.gif)
_Working accordion without animation_

As you can see, your accordion is already fully functional. Due to the logic you implemented with the ternary operator, only one accordion item can be opened at a time. Kudos!

Alas, your component is a little boring, right? It probably looks like every other accordion you’ve seen out there. So let’s spice up yours and make it the _talk of the tech community_ by animating it 😉.

### The Animation Section

At the moment when you toggle in the `open` class, the `accordion__details` element goes from showing no content to the full content in a split second without any animation whatsoever. It does this by alternating the value of the height from 0 to auto. 

To make the accordion more interactive, you’ll use GSAP to animate the height of each accordion component when an accordion item is clicked.

Start by creating a reference of all the accordion items:

```js
const accordionRefs = useRef([]);
```

**Note**: The `useRef` hook takes in an array because you’re selecting multiple elements. To distinctively target each element, use a `ref` attribute and pass in each individual index in the `ref`.

```js
<div className="App">
      <div className="accordion__container">
        <div
          className={`accordion__item  ${openAccordion === 0 ? "open" : ""}`}
           // HERE
          ref={(el) => (accordionRefs.current[0] = el)}
        >
          <div
            className="accordion__header"
            onClick={() => handleAccordionClick(0)}
          >
            <p className="accordion__number">01</p>
            <p className="accordion__name">The World's Tallest Building</p>
                     </div>

          <div
            className="accordion__details"
            
          >
            <ul>
              <li>
                The current tallest building in the world is the Burj Khalifa,
                located in Dubai, United Arab Emirates.
              </li>
              <li>
                It stands at a height of 828 meters (2,716 feet) tall and has
                163 floors.
              </li>
              <li>
                The building took six years to construct and was completed in
                2010.
              </li>
            </ul>
          </div>
        </div>

        <div
          className={`accordion__item ${openAccordion === 1 ? "open" : ""}`}
           // HERE
          ref={(el) => (accordionRefs.current[1] = el)}
        >
          <div
            className="accordion__header"
            onClick={() => handleAccordionClick(1)}
          >
            <p className="accordion__number">02</p>
            <p className="accordion__name">
              Famous Inventors and Their Inventions
            </p>
                      </div>
          <div
            className="accordion__details"
            
          >
            <ul>
              <li>
                Nikola Tesla, a Serbian-American inventor, is credited with the
                invention of the AC (alternating current) electrical system.
              </li>
              <li>
                Thomas Edison, an American inventor, is credited with the
                invention of the light bulb.
              </li>
              <li>
                Alexander Graham Bell, a Scottish-born American inventor, is
                credited with the invention of the telephone.
              </li>
            </ul>
          </div>
        </div>
        <div
          className={`accordion__item ${openAccordion === 2 ? "open" : ""}`}
          // HERE
          ref={(el) => (accordionRefs.current[2] = el)}
        >
          <div
            className="accordion__header"
            onClick={() => handleAccordionClick(2)}
          >
            <p className="accordion__number">03</p>
            <p className="accordion__name">Largest Deserts in the World</p>
                      </div>
          <div
            className="accordion__details"
            
          >
            <ul>
              <li>
                The Sahara Desert, located in Africa, is the largest hot desert
                in the world and covers an area of 9.2 million square kilometers
                (3.6 million square miles).
              </li>
              <li>
                The Antarctic Desert, located in Antarctica, is the largest cold
                desert in the world and covers an area of 14 million square
                kilometers (5.4 million square miles).
              </li>
              <li>
                The Arabian Desert, located in the Middle East, is the
                third-largest desert in the world and covers an area of 2.33
                million square kilometers (900,000 square miles).
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>

```

Next, modify the `handleAccordionClick` function to add GSAP animations.

```js
if (index === openAccordion) {
      gsap.to(
        accordionRefs.current[index].querySelector(".accordion__details"),
        {
          height: 0,
          duration: 1,
          ease: "power1.inOut",
         }
      );
    }
```

Explaining the code snippet above:

* The conditional statement first checks if the index of the accordion item clicked matches the current state of the accordion.
* Next, we use a GSAP method to add animations when the condition is true. The `gsap.to` method allows you to define the animation properties for an element and then smoothly transition the element from its current state to the specified end state over a period of time. The `gsap.to` method takes in 2 parameters, the target element and the specified behaviour of that target element.
* We used a DOM traversing attribute (`.querySelector`) to select the element with the class name `accordion__details` inside that accordion item and attached some animation and styling to it.

**Note:** This code block will fire each time a particular accordion item is clicked twice, (when `index === openAccordion`), making this a closing animation.

Next you have to account for opening animations and closing previously open accordion items.

```js
else {
      if (openAccordion !== null) {
        gsap.to(
          accordionRefs.current[openAccordion].querySelector(
            ".accordion__details"
          ),
          {
            height: 0,
            duration: 1,
            ease: "power1.inOut",
          }
        );
      }
      setOpenAccordion(index);
      gsap.fromTo(
        accordionRefs.current[index].querySelector(".accordion__details"),
        { height: 0 },
        {
          height: "auto",
          duration: 1,
          ease: "power1.inOut",
        }
      );
    }
```

* The else block checks if the current value of the accordion is not null (if an accordion header has already been clicked) and uses GSAP to close the previously opened accordion by using the value stored in the `openAccordion` to target the appropriate element.
* Then it updates the `openAccordion` value to the currently clicked element’s index. Finally, it uses a `gsap.fromTo` method to specify the animation of opening an accordion item. The `gsap.fromTo` takes in a starting and ending condition and animates the accordion item accordingly (from height: 0 to height: auto).

Taking a look at the accordion now, you'll see the following result:

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Final-version-with-a-bug.gif)
_Final version with a bug_



And with that, you’ve successfully crafted an interactive accordion component, congrats! 🎉

There’s a small bug though. If you click on an accordion item after opening and closing it, it fails to open. This is because after the accordion item closes, the value of the `openAccordion` is still set to that accordion item’s index. This makes the code behave like there’s still an open accordion item even after closing it. 

To solve this, attach an `onComplete` event to the `handleAccordionClick` function that sets the value of openAccordion to null after the animation completes. This way, each time you close the accordion, the value of `openAccordion` is reset and the accordion item can be reopened.

```js
  const handleAccordionClick = (index) => {
    if (index === openAccordion) {
      gsap.to(
        accordionRefs.current[index].querySelector(".accordion__details"),
        {
          height: 0,
          duration: 1,
          ease: "power1.inOut",
          onComplete: () => setOpenAccordion(null),
        }
      );
      console.log(openAccordion);
    } else {
      if (openAccordion !== null) {
        gsap.to(
          accordionRefs.current[openAccordion].querySelector(
            ".accordion__details"
          ),
          {
            height: 0,
            duration: 1,
            ease: "power1.inOut",
          }
        );
      }
      setOpenAccordion(index);
      gsap.fromTo(
        accordionRefs.current[index].querySelector(".accordion__details"),
        { height: 0 },
        {
          height: "auto",
          duration: 1,
          ease: "power1.inOut",
        }
      );
    }
  };
```

And with that, let’s take a look at the final result:

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Final-bug-free-version-1.gif)
_Final bug free version_

For ease of accessibility, here’s the final full code:

```js
import { useRef, useState } from "react";
import "./App.css";
import { gsap } from "gsap";
function App() {
  const [openAccordion, setOpenAccordion] = useState(null);
  const accordionRefs = useRef([]);

  const handleAccordionClick = (index) => {
    if (index === openAccordion) {
      gsap.to(
        accordionRefs.current[index].querySelector(".accordion__details"),
        {
          height: 0,
          duration: 1,
          ease: "power1.inOut",
          onComplete: () => setOpenAccordion(null),
        }
      );
      // console.log(openAccordion);
    } else {
      if (openAccordion !== null) {
        gsap.to(
          accordionRefs.current[openAccordion].querySelector(
            ".accordion__details"
          ),
          {
            height: 0,
            duration: 1,
            ease: "power1.inOut",
          }
        );
      }
      setOpenAccordion(index);
      gsap.fromTo(
        accordionRefs.current[index].querySelector(".accordion__details"),
        { height: 0 },
        {
          height: "auto",
          duration: 1,
          ease: "power1.inOut",
        }
      );
    }
  };

  return (
    <div className="App">
      <div className="accordion__container">
        <div
          className={`accordion__item  ${openAccordion === 0 ? "open" : ""}`}
          ref={(el) => (accordionRefs.current[0] = el)}
        >
          <div
            className="accordion__header"
            onClick={() => handleAccordionClick(0)}
          >
            <p className="accordion__number">01</p>
            <p className="accordion__name">The World's Tallest Building</p>
          </div>

          <div className="accordion__details">
            <ul>
              <li>
                The current tallest building in the world is the Burj Khalifa,
                located in Dubai, United Arab Emirates.
              </li>
              <li>
                It stands at a height of 828 meters (2,716 feet) tall and has
                163 floors.
              </li>
              <li>
                The building took six years to construct and was completed in
                2010.
              </li>
            </ul>
          </div>
        </div>

        <div
          className={`accordion__item ${openAccordion === 1 ? "open" : ""}`}
          ref={(el) => (accordionRefs.current[1] = el)}
        >
          <div
            className="accordion__header"
            onClick={() => handleAccordionClick(1)}
          >
            <p className="accordion__number">02</p>
            <p className="accordion__name">
              Famous Inventors and Their Inventions
            </p>
          </div>
          <div className="accordion__details">
            <ul>
              <li>
                Nikola Tesla, a Serbian-American inventor, is credited with the
                invention of the AC (alternating current) electrical system.
              </li>
              <li>
                Thomas Edison, an American inventor, is credited with the
                invention of the light bulb.
              </li>
              <li>
                Alexander Graham Bell, a Scottish-born American inventor, is
                credited with the invention of the telephone.
              </li>
            </ul>
          </div>
        </div>
        <div
          className={`accordion__item ${openAccordion === 2 ? "open" : ""}`}
          ref={(el) => (accordionRefs.current[2] = el)}
        >
          <div
            className="accordion__header"
            onClick={() => handleAccordionClick(2)}
          >
            <p className="accordion__number">03</p>
            <p className="accordion__name">Largest Deserts in the World</p>
          </div>
          <div className="accordion__details">
            <ul>
              <li>
                The Sahara Desert, located in Africa, is the largest hot desert
                in the world and covers an area of 9.2 million square kilometers
                (3.6 million square miles).
              </li>
              <li>
                The Antarctic Desert, located in Antarctica, is the largest cold
                desert in the world and covers an area of 14 million square
                kilometers (5.4 million square miles).
              </li>
              <li>
                The Arabian Desert, located in the Middle East, is the
                third-largest desert in the world and covers an area of 2.33
                million square kilometers (900,000 square miles).
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}
export default App;
```

Here’s a link to the repository: [Github](https://github.com/Daiveedjay/React-Gsap-Accordion)

And the live version: [Live Demo](https://react-gsap-accordion.netlify.app)

As a bonus, I prepared a JSON file in the repo containing all the information filled into the accordion component to better aid you in writing cleaner and reusable code.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/007-Json-file.png)
_JSON file_

## Conclusion

In this tutorial, you learned how to create an accordion component using React and GSAP that's not only functional but also looks super cool! 

Now you can impress your friends and colleagues with your accordion-making skills, and who knows – maybe you'll start a new trend of accordion-themed websites :) Just remember to use your powers for good and not evil, and always accordion responsibly.

### Contact Information

Want to connect or contact me? Feel free to hit me up on the following:

* Twitter: [@jajadavid8](https://twitter.com/JajaDavid8)
* LinkedIn: [David Jaja](https://www.linkedin.com/in/david-jaja-8084251b4/)
* Email: Jajadavidjid@gmail.com


