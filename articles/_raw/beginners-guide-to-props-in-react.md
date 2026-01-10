---
title: How Props Work in React – A Beginner's Guide
subtitle: ''
author: Temitope Oyedele
co_authors: []
series: null
date: '2022-08-04T17:31:54.000Z'
originalURL: https://freecodecamp.org/news/beginners-guide-to-props-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/A-Beginner-s-Guide-to-Props-in-Reacte--1-.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: React
  slug: react
seo_title: null
seo_desc: "Props are used to store data that can be accessed by the children of a\
  \ React component. \nThey are part of the concept of reusability. Props take the\
  \ place of class attributes and allow you to create consistent interfaces across\
  \ the component hierarch..."
---

Props are used to store data that can be accessed by the children of a React component. 

They are part of the concept of reusability. Props take the place of class attributes and allow you to create consistent interfaces across the component hierarchy.

In this article, we'll learn about props in React. We'll look at what they are and how they work. Then we will look at how props compare to state.

What we'll cover:

* What are props?
* How to declare a prop
* How to use `defaultProps`
* Props vs state in React

So let's get started!

## What Are Props in React?

Props simply stands for properties. They are what make components reusable. Because they perform an essential function – they pass data from one component to another.  

Props act as a channel for component communication. Props are passed from parent to child and help your child access properties that made it into the parent's tree.

Now, imagine we had a component in the form of a product consisting of the name of the product, its description, and price. All we have to do is write the component once and reuse it several times by altering the data that we pass through the props, which renders it to the desired output.

It's worth noting that:

* We use props in both functional and class-based components.
* We pass props from the top to bottom. We can also refer to it as ancestor to descendant, or parent to child.
* Props are read-only. This means that once a component receives a bunch of props, we cannot change it, but we can only use and consume it and cannot modify the properties passed down to the component. If we want to modify that, we'll have to introduce what we call state in React.

## How to Use Props in React

We'll use my earlier explanation about having a product as a component and reusing it several times to demonstrate how to use props. 

The first thing we'll look at is how to use props without destructuring. Then we'll take a look at how to use props with destructuring. 

Knowing how to use props without destructuring is essential as a beginner so you can grasp the idea of how props work.

### How to Use Props Without Destructuring

To get started, let's create a functional component:

```js
import React from "react";
 
function MyProducts() {
  return (
    <div>
  
    </div>
  );
}
 
export default MyProducts;
```

Then we want to initialize our props. So our functional component would look like this:

```js
import React from "react";
 
function MyProducts(props) {
  return (
    <div>
      <h1>{props.name}</h1>
      <p>{props.description}</p>
      <p>{props.price}</p>
    </div>
  );
}
 
export default MyProducts;
```

So basically, we passed in `props` as an argument in our function. `props` gets passed as a parameter to our functional component. We then tried to access it by writing the following: the `props.name`, `props.price`, and `props.description`.

Now that we've done that, we can go back to our `App.js` to render our product and pass some data to these three props. Props are passed in like HTML attributes. Our `App.js` will look like this:

```js
import "./App.css";
import MyProducts from "./MyProducts";
function App() {
  return (
    <div className="App">
      <MyProducts
        name="temitope"
        description="the product has fantastic features"
        price={1000}
      />
    </div>
  );
}
 
export default App;
```

And here's our result:

![Image](https://www.freecodecamp.org/news/content/images/2022/08/props.PNG)

So here's the logic to use props. We first had to initialize it, and we then needed to access the props and what kind of property it holds. Then our rendered components consume those properties and pass data into them.

Props are handy! Why? Because we can make one component reusable in various ways. To confirm this, we'll copy the `MyProducts` we rendered out, pasting in another line but this time passing in some other data:

```js
import "./App.css";
import MyProducts from "./Myproducts";
function App() {
  return (
    <div className="App">
      <MyProducts
        name="temitope"
        description="the product is has fantastic features"
        price={1000}
      />
      <MyProducts
        name="iphone"
        description="awesome camera features!"
        price={5000}
      />
    </div>
  );
}
 
export default App;
```

So you can see we are just reusing the same component with different properties. Let's now look at how to pass in props with destructuring.

### How to Use Props With Destructuring

Destructuring is a JavaScript feature that allows you to extract sections of data from an array or object. Let's look at a brief example of how this works.

Let’s say we have an array of todos and want to get the first two elements in that array. An old way would be to do it like this:

```js
const todo = ["bath","sleep","eat"];
// old way
const firstTodo = todo[0];//bath
const secondTodo = todo[1];//sleep
 
console.log(firstTodo);
console.log(secondTodo);
```

Destructuring offers a much easier way to do this:

```js
const todo = ["bath","sleep","eat"];
 
// destructuring
const [firstTodo, secondTodo] = todo;// bath, sleep
 
console.log(firstTodo);
console.log(secondTodo);


```

In React, destructuring allows us to pull apart or unpack our props, which lets us access our props and use them in a more readable format.

We can use destructuring with the code from the previous section as follows:

```js
import React from "react";
 
function MyProducts({ name, description, price }) {
  return (
    <div>
      <h1>{name}</h1>
      <p>{description}</p>
      <p>{price}</p>
    </div>
  );
}
 
export default MyProducts;

```

The difference between this method and the previous one is that we are pulling apart the props, destructuring them, and then rendering them. If we check our result, we'll see that it's still intact.

Since props can be passed from top to bottom, we can create another child component in which we can pass down the parent's attributes. Let's see how it's done. 

Create another file called `AdditionalDescription` and pass in some props in the form of a name and description in its function:

```js
import React from "react";
 
function AdditionalDescription({ name, description }) {
  return (
    <div>
   
    </div>
 
  );
}
 
export default AdditionalDescription;
```

We'll then have two paragraph tags showing the name and description. This will make this component look like this:

```js
import React from "react";
 
function AdditionalDescription([name, description]) {
  return (
  <div>
      <p>{name}</p>
      <p>{description}</p>
  </div>
  )
}
 
export default AdditionalDescription;
```

Now let's render our `AdditionalDescription` and pass down some props to it:

```js
<AdditionalDescription name={name} description={description} />
```

You'll see that it is taking the props of the parent.

## How to Set a Default Value for Props

The `defaultProps` is a React component property that allows us to set default values for the props argument. It usually comes in handy when we don’t have any props data passed in. 

Let's go ahead and create a default prop:

```js
import React from "react";
 
function MyProducts({ name, description, price }) {
  return (
    <div>
      <h1>{name}</h1>
      <p>{description}</p>
      <p>{price}</p>
    </div>
  );
}
Myproducts.defaultProps = {
  name: "temitope",
  description: "i like this feature",
  price: 500,
};
 
export default MyProducts;
```

We declared default values for our props near the end of the code, just before we exported the component. 

To declare default props, we used the component's name followed by a dot and then `defaultProps`, which is included when you create a React app.

With this, we won't have an empty prop as these values will now be the initial values wherever we import this component. But when we pass data into it, the default values are then overridden.

## Props vs State in React

State is another way to manage your data in React. So how does state differ from props? The first thing to note is while props are `read-only` and are immutable, while states change asynchronously and is mutable.

A state can change over time, and this change can happen as a response to a user action or a system event. State can only be accessed or modified inside the component. 

Props, on the other hand, allow passing of data from one component to another. Here's a table below to show how they differ:

<table style="border:none;border-collapse:collapse;"><colgroup><col width="61"><col width="241"><col width="245"></colgroup><tbody><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">s/n</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Props</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"> state</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">1</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Props are read only</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"> State changes asynchronously</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">2</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">They are immutable</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">They are mutable</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">3</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">They allow you to pass data from one component to another</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">They hold information about the components</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">4</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">They can be passed down and accessed by a child component</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">They cannot be accessed by a child component</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">5</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Props are basically used to communicate between components</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">State is used for rendering dynamic changes</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">6</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Props make components reusable</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">States can’t make components reusable</span></p></td></tr></tbody></table>

## Wrapping Up

This article talked about everything you need to know about props as a beginner. You learned what they are and how to use them. 

We also took a look at how props differ from state, citing some examples which will come in handy so you can understand what props are fully.

Please share this article if you found it helpful. Thanks for reading!

