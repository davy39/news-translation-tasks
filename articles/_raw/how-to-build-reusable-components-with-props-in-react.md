---
title: How to Build Reusable Components with Props in React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-13T17:14:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-reusable-components-with-props-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/reusable-components-image.png
tags:
- name: components
  slug: components
- name: React
  slug: react
seo_title: null
seo_desc: 'By Alvin Okoro

  Props are one of the most important building blocks of React.js. When you need to
  pass data down from a parent component to a child component, props make this possible.

  In this article we''ll learn how to work with props and build reusa...'
---

By Alvin Okoro

Props are one of the most important building blocks of React.js. When you need to pass data down from a parent component to a child component, props make this possible.

In this article we'll learn how to work with props and build reusable components in React.

## What Are Props in React?

Props is short for properties. They represent information you want to pass down to a specific component so that component can reuse that info. 

Information you can pass down as props ranges from className to height, width, and much more. This makes it so easy to create reusable items such as buttons, cards, input elements, and so on.

## How to Work with Props in React

Now that you know what props are and the major work they do in components, it's time to demonstrate how to work with props when you're creating reusable component in React. 

Assuming you have a new or existing React application, create two new files. We'll call the first file **Author.jsx** and the second file **AuthorProfile.jsx**_._ 

Now open your "Author.jsx" file and add the following code:

```javascript
export default function Author({name, imageUrl}){
	return (
    	<div className="author">
          <h2>{name}</h2>
          <img src={imageUrl} alt={name}/>
        </div>
    )
}
```

What do we have in the code above?

We have our regular functional component in React and then we have the props – `name` and `imageUrl`. They're destructured and passed right into our function so we can really reuse this Author component in any section of our application.

Now to reuse the Author.jsx component in our AuthorProfile.jsx, we can do this:

```javascript
import Author from "./Author"

export default function AuthorProfile(){
	return (
      <div className="author-profile">
      	<Author name="Alvin"  
        imageUrl="https://avatars.githubusercontent.com/u/43749581?v=4" />
      </div>
    )
}
```

First we have to import the component into where we want to reuse it, as you can see in the first line of the above code where we have our import statement.

Second, because we passed in `name` and `imageUrl` as props in the author component earlier, the author component expects the same data to be passed into it at first.

We can make many components reusable in this way in a large codebase with the help of props. And this helps us structure our code properly.

Sweet!

## Props Example

Let's demonstrate how props are helpful with a final example – but this time around, we'll create a reusable button with the help of props.

Create a new file called PrimaryButton.jsx. In the PrimaryButton file, let's do this:

```javascript
export default function PrimaryButton({width,
  height,
  backgroundColor,
  color,
  border,
  borderColor,
  fontSize,
  buttonText,}) {
	return (
    	<button style={{width, height, backgroundColor, color, border, borderColor, fontSize}}>
           {buttonText}
        </button>
    )
}
```

Awesome, now we have a button which we can use anywhere in our application. Instead of repeating or creating buttons over and over again, we can simply import the reusable button, pass in the required data, and we are good to go.

## Wrapping Up

Now you've learned how to build reusable components in React with the help of props. Try out more examples on your own and happy hacking!

