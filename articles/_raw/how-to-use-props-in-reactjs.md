---
title: How to Use Props in React.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-20T20:16:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-props-in-reactjs
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/How-to-use-props-in-reactjs.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "By Joy O. Oluwafemi\nProps are an important concept to understand in React.\
  \ You use props to pass data and values from one component to another to get dynamic\
  \ and unique outputs. \nWebsites built with React like Facebook, Twitter, and Netflix\
  \ use the s..."
---

By Joy O. Oluwafemi

Props are an important concept to understand in React. You use props to pass data and values from one component to another to get dynamic and unique outputs. 

Websites built with React like Facebook, Twitter, and Netflix use the same design patterns across many sections that just have different data. One of the main ways developers can achieve this functionality is by using props.

This article will explain what props are and we'll look at the syntax for passing and receiving props. Then, to further strengthen your knowledge about props, we will build a section of an e-commerce site which displays information about different products to users.

The concept of props is built on the concept of components. So, to get the most out of this article, you must know [how to set up a React app](https://www.freecodecamp.org/news/the-react-handbook-b71c27b0a795/#how-to-use-create-react-app) and [be familiar with how React components work](https://www.freecodecamp.org/news/the-react-handbook-b71c27b0a795/#components).

## What are React Props?

Props in React are inputs that you pass into components. The props enable the component to access customised data, values, and pieces of information that the inputs hold. 

The term 'props' is an abbreviation for 'properties' which refers to the properties of an object.

As I said in the introduction, the concept of props builds on components. So we can't successfully work with props without having a component to work with. 

Let's build and connect the components that we will be working with in this tutorial together.

Below is the structure of the parent component:

```javascript
import Product from "./Product"

function App() {
  return (
      <div>
      	<h1>PRODUCTS</h1>
      	<div className="App">
      		<Product />
      	</div>
      </div>
  )
}

export default App
```

Below is the structure of the child component:

```javascript
function Product() {
    return (
      <div>
        <img src="https://ng.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/82/6142201/1.jpg?2933" alt="sneakers" />
        <h4>Cyxus</h4>
        <p>Non-Slip Fitness Leisure Running Sneakers</p>
        <h4>$29</h4>
      </div>
    );
}

export default Product
```

Our goal is to be able to display all the different products which vary in name, price, appearance, and description to users. 

Of course, we can reuse the product component as many times as we want by just re-rendering the component. For example:

```javascript
import Product from "./Product"

function App() {
  return (
    <div className="App">
      <Product />
      <Product />
      <Product />
    </div>
  )
}

export default App
```

![Image](https://www.freecodecamp.org/news/content/images/2022/09/props-repeated-design.PNG)
_Live Output_

We can see the React functionality of repeating a particular design without writing much code in play here. 

But we haven't yet achieved our goal, right? While we want to reuse the component, we also want to update the name of the product, the price, the description, and the image without having to hard code any data in the Product.js component. 

This is where we can use props in React to make our data output dynamic.

## How to Use React Props

Before we go deeper, it is important to note that React uses a one-way data flow. This means that data can only be transferred from the parent component to the child components. Also, all the data passed from the parent can't be changed by the child component. 

This means that our data will be passed from `App.js` which is the parent component to `Product.js` which is the child component (and never the other way).

### How to Send Props into a Component

How props are passed into a component is similar to how attributes work in HTML elements. 

For example, when you want to pass attributes into an input element in HTML, you will write the attribute and attach the value of the attribute to it, just like this:

```html
<input type="text" placeholder="Cyxus" />
```

Also, when sending props (which are also properties and can be likened to attributes), you attach your values to them. 

Below is the syntax:

```javascript
<ComponentName property1="value" property2="value" property3="value" />
```

Within the component tag, after writing the component name we will assign a value to each property. 

Now let's use the syntax above to pass data into the `App.js` component:

```javascript
<Product
  img="https://ng.jumia.is/unsafe/fitin/300x300/filters:fill(white)/product/82/6142201/1.jpg?2933"
  name="Cyxus"
  desc="Non-Slip Fitness Leisure Running Sneakers"
  price="$29"
/>
```

In the code above, the component name within the tag is `Product`, and the first property or prop is `img` with its value `[https://m.media amazon.com/images/W/WEBP_402378T1/images/I/71TR1WrqqJL](https://m.media-amazon.com/images/W/WEBP_402378T1/images/I/71TR1WrqqJL)._AC_UL320_.jpg` attached to it. Then we have `name` which is the second property and `desc` which is the third property (these are also assigned values).

When we structure the `App.js` component properly, it will now look like this:

```javascript
import Product from "./Product";

function App() {
  return (
    <div>
      <h1>PRODUCTS</h1>
      <div className="App">
        <Product
          img="https://ng.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/82/6142201/1.jpg?2933"
          name="Cyxus"
          desc="Non-Slip Fitness Leisure Running Sneakers"
          price="$29"
        />
      </div>
    </div>
  );
}

export default App;
```

There's a slight difference between writing HTML attributes and passing in props: while HTML attributes are special keywords already provided for you, you customize and define props in React. 

For example, I created the properties; 'img', 'name', 'desc', and 'price' above. Then, I attached the values of the props alongside them.

### How to Access and Use Props in React

The component receives `props` as a function parameter. It uses the value of props by defining the parameter as props objects. 

Below is the syntax:

```javascript
//the function receives 'props' as a parameter function
function Product(props) {
    return (
      <div>
//it uses the value of props by defining the parameter as props objects
        <img src={props.objectName} alt="products" />
        <h4>{props.objectName}</h4>
        <p>{props.objectName}</p>
        <h4>{props.objectName}</h4>
      </div>
    );
}

export default Product
```

Let's relate the syntax above to our `Product.js` by receiving `props` as a parameter function and by defining props as object:

```javascript
//the function receives 'props' as a parameter function
function Product(props) {
    return (
      <div>
//it uses the value of props by defining the parameter as props objects
        <img src={props.img} alt="products" />
        <h4>{props.name}</h4>
        <p>{props.description}</p>
        <h4>{props.price}</h4>
      </div>
    );
}

export default Product
```

We have successfully made the data we passed into the Product.js component dynamic. 

To reuse the 'Product.js' component to show the data of other products, all we need to do is to attach the new data or values when re-rendering the component. 

Below is the syntax for this:

```javascript

<ComponentName property1="valueA" property2="valueB" property3="valueC" />
<ComponentName property1="valueD" property2="valueE" property3="valueF" />
<ComponentName property1="valueG" property2="valueH" property3="valueI" />
```

Now let's relate the syntax above to our `App.js`:

```javascript
import Product from "./Product";

function App() {
  return (
    <div>
      <h1>PRODUCTS</h1>
      <div className="App">
        <Product
          img="https://ng.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/82/6142201/1.jpg?2933"
          name="Cyxus"
          desc="Non-Slip Fitness Leisure Running Sneakers"
          price="$29"
        />
        <Product
          img="https://ng.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/01/241417/1.jpg?6747"
          name="Vitike"
          desc="Latest Men Sneakers -Black"
          price="$100"
        />
        <Product
          img="https://ng.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/06/4410121/1.jpg?4437"
          name="Aomei"
          desc="Men's Trend Casual Sports Shoe"
          price="$40"
        />
      </div>
    </div>
  );
}

export default App;
```

The live output of the code above now displays image, name, and description peculiar to each product. 

Here is the live output:

![Image](https://www.freecodecamp.org/news/content/images/2022/09/props-final-output.PNG)
_[See live output here](https://ekezwh.csb.app/)_

[Here](https://codesandbox.io/s/ekezwh?file=/src/App.js) is the code used for the project in this article, feel free to compare it with your code.

## Destructuring Props in React

Now that we’ve achieved the functionality we aimed for, let’s format our `Product.js` by making use of destructuring. This is a feature of JavaScript that involves assigning pieces of data from an object or array to a separate variable so that the variable can hold the data coming from the array or object.

Props are objects. So to destructure objects in React, the first step is to group your properties within a set of curly braces. Then you can either store it into a variable called `props` within the body of the function or pass it directly as the function’s parameter.

The second step is to receive the properties where you need them by stating the names of the properties without attaching the prefix ‘props’.

Below is an example of the two ways you can destructure in React:

```javascript

function Product = (props) => {
//First Step: Destructuring within the body of the function
    const { img, name, desc, price} = props ;
    return (
      <div>
  		<img src={img} alt="products" />
//Second Step: receive the properties where you need them by stating the names of the properties without attaching the prefix ‘props.’
        <h4>{name}</h4>
        <p>{description}</p>
        <h4>{price}</h4>
      </div>
    );
}

export default Product
```

```javascript
//First Step: Destructuring within function's parameter
function Product = ({ img, name, desc, price}) => {
    return (
      <div>
  		<img src={img} alt="products" />
//Second Step: receive the properties where you need them by stating the names of the properties without attaching the prefix ‘props.’
        <h4>{name}</h4>
        <p>{description}</p>
        <h4>{price}</h4>
      </div>
    );
}

export default Product
```

Destructuring in React makes our code more readable and more concise. Note that the two ways of destructuring that I demonstrated above will always have the same output.

## Conclusion

This article has explained how props work in React which will help you write web pages with dynamic data outputs. 

Leverage this knowledge to build cool stuff! Connect with me on Twitter [@JoyPaces](https://twitter.com/JoyPaces).

