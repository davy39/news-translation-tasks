---
title: React Projects for Beginners in 2023 – Fun Ideas with Code
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2023-01-10T17:53:44.000Z'
originalURL: https://freecodecamp.org/news/react-projects-for-beginners-easy-ideas-with-code
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/7-react-projects-beginners.png
tags:
- name: projects
  slug: projects
- name: React
  slug: react
seo_title: null
seo_desc: 'You''re ready to start making simple projects with React, but you don''t
  know what to make. Where should you start?

  I have created seven unique and fun React projects for you to make, all of which
  will teach you essential React concepts that you need t...'
---

You're ready to start making simple projects with React, but you don't know what to make. Where should you start?

I have created seven unique and fun React projects for you to make, all of which will teach you essential React concepts that you need to know in 2023. 

Unlike other recommended projects which require you going to use multiple third-party libraries, all of these projects only use the core React library. Each of them use the latest React version (18) and no CSS frameworks. 

My goal in creating this guide is to show you that you don't need a ton of code and special libraries to start building cool things with React. 

Let's get started!

## 1. Image Carousel

The first React project on our list is an image slider or carousel. 

### Final result

%[https://codesandbox.io/s/runtime-field-xp5sol]

### How you will build it

Our carousel should allow the user to click the backwards or forwards button to go to the previous or next image. 

The images will be stored in a simple array. We will see how to use state in order to store the current image. Then we will update that state to go to the previous or next image, according to the button the user pressed. 

If the user has gone through all of the images, you will figure out how to start at the beginning of the array, to allow them to cycle through the images again. If you don't want to use images, you could also use text to make a testimonial carousel that cycles through reviews for a given product. 

Finally, if you want to take your carousel to the next level, try adding a fun transition using CSS to animate the image as it changes.

### React concepts you will learn

* useState (storing and updating state)
* Conditionals (ternaries)
* Lists, keys, and .map()

## 2. FAQ/Accordion

Another common type of component which can utilizes state is an accordion component, which can both reveal and hide text.

### Final result

%[https://codesandbox.io/s/determined-hoover-22hclm]

### How you will build it

You will learn how to toggle state to make sure that each accordion opens and closes after each button press. You will also learn simple conditionals such as the and (&&) operator that will only show the content of the accordion when the accordion state says it is open. 

Finally, we will create an entire FAQ (frequently asked questions) section by displaying multiple accordion components. To do so, we will learn how to pass each accordion's data down into the component using props.

### React concepts you will learn

* Toggling state with useState
* Conditionals (&&)
* Passing data to components via props
* Displaying multiple components with `.map()`

## 3. Quote Generator

Using external APIs and making HTTP requests are an essential part of any React application. To learn how to make HTTP requests in React, we will make a random quote generator.

### Final result

%[https://codesandbox.io/s/zen-diffie-x61ywc]

### How you will build it

Our quote generator will need to use the useEffect hook to perform a "side effect" to fetch the quotes from an external API. After fetching our quotes, we will put them in our local app state, which we will call `quotes`. 

We'll then take that array of quotes and use a function to select a random item within that array. Then we'll put it in another state variable called just `quote`, which can then be displayed to our user. 

We also want to add a "New Quote" button above each quote that will perform the same operation – get a new random quote from our `quotes` array and put it in `quote`.

Finally, the quote isn't loaded in state. So we'll make sure to use the optional chaining operator (?) to safely check our object before we attempt to get a value from that quote in state to make sure our app doesn't throw an error.

### React concepts you will learn

* useEffect (to perform side effects)
* HTTP requests with Fetch API
* Conditional chaining operator (?)

## 4. Shopping list

Next we'll take a look at how to build a shopping list where users can add new items to the list that they'd like to get from the store and delete items from the list.

### Final result

%[https://codesandbox.io/s/modest-feistel-zsttc9]

### How to build it

This project will teach you how to add new items to an array in our local state using the array spread operator. Additionally, you'll learn how to delete any item we like using the `filter` function in JavaScript. 

This project will also get you familiar with typing values into a form input and then retrieving those values when the form is submitted. You'll do this using the `onSubmit` event handler.

One fun way to enhance this project would be to enable our users to double click each item in our list to strike through it to put a line through it in addition to being able to delete it. 

### React concepts you will learn

* Updating lists with useState
* JavaScript array spread operator and `filter` functions
* Forms and inputs in React
* `onSubmit` event handler

## 5. GitHub User Search

In this project, we will use an input's value to search for users in GitHub using their username or email.

### Final result

%[https://codesandbox.io/s/mutable-sky-iesdhc]

### How to build it

You will first store the value typed into the input in a state value called `query`. After that, you will perform an HTTP request to a GitHub API endpoint to then fetch the users' profile which once again uses the browser fetch API. The request URL will use the input value. 

Once the results are fetched, we'll see how to display all the relevant info such as their name, avatar, and a link to go to their profile.

A good way to extend this project would be to attempt to allow search functionality as the user types instead of having to submit the form first. Make sure to use a debounce function to ensure that you do not too many requests to the GitHub API and get a 429 error response (too many requests).

## 6. Video Player

React can also be used to work with the HTML video element and toggle between different videos.

%[https://codesandbox.io/s/gifted-dirac-r6m0ns]

### How to build it

In our project, we will allow users to toggle through several different videos using a radio input. We will not only see how to work with radio inputs in forms in React, but how to pass props down to our two components, `Menu` and `Video`. 

In particular, we will learn how to pass down functions to update state in the parent components from the child component. This pattern is called lifting state up and is a very important pattern to know in React.

A fun way to improve this project would be to add a button to extend the functionality of the video player. For example, to add buttons to control whether the video is looped, whether the video autoplays, and more.

### React concepts you will learn

* Radio inputs in React
* Passing functions as props
* Lifting state up in React

## 7. BMI Calculator

Finally we will build a simple BMI (body mass index) calculator which will use a person's weight and height in order to calculate their body mass index as a number.

%[https://codesandbox.io/s/festive-water-c70hv3]

### How to build it

We will use a couple of range inputs to enable our users to select their weight and height on a sliding scale. 

Body mass index is calculated based off of the stored weight and height values. Our goal will be to calculated output their body mass index instantly, according to whatever values are stored in the `weight` and `height` state variables. 

To do so, we will use the `useMemo` React hook to performantly calculate this value whenever either of these two values changed.

### React concepts you will learn

* Range inputs in React
* useMemo (to performantly perform calculations)

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

