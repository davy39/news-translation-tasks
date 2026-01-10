---
title: How to Render Lists in React using array.map()
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-10T21:39:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-render-lists-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Lists-in-React.png
tags:
- name: React
  slug: react
seo_title: null
seo_desc: 'By Mwendwa Bundi Emma

  When you''re working with React, you will often times need to render lists of items.
  With the map() method, you can create new results from your current lists or even
  showcase all the items in your lists.

  In this tutorial, you wi...'
---

By Mwendwa Bundi Emma

When you're working with React, you will often times need to render lists of items. With the `map()` method, you can create new results from your current lists or even showcase all the items in your lists.

In this tutorial, you will learn how to use this method to access array contents in React. We'll also explore how to pass a list of items into multiple React components using React `props`.

## What is array.prototype.map()?

The JavaScript `map()` method works by creating a new array that consists of outcomes from calling a function on the items in your array. 

Below is the array you'll be working with. It contains info about applicants to a mentorship workshop. The array is stored in `applicants` variable.

```js
const applicants = [ {
  name: 'Joe', work: 'freelance-developer', 
  blogs: '54', websites: '32', 
  hackathons: 'none', location: 'Morocco', id: '0',
    
},
 {
  name: 'Janet', work: 'fullstack-developer', 
  blogs: '34', websites: '12', 
  hackathons: '6', location: 'Mozambique', id: '1',
    
},

];
```

## How `array.prototype.map()` Works in React

Now, you need to return JSX that renders every applicant name as presented from the array.

To get the names of the applicants, you can easily do that with JavaScript's `array.map` method. Below is how you can map every applicant's name:



```react
import React from 'react';


  const applicants = [ {
    name: 'Joe', work: 'freelance-developer',
    blogs: '54', websites: '32',
    hackathons: '6', location: 'morocco', id: '0',
  },
  {
    name: 'janet', work: 'fullstack-developer', 
    blogs: '34', websites: '12', 
    hackathons: '8', location: 'Mozambique', id: '1',
  },

];

function App() {
  return (
    <>
    {applicants.map(function(data) {
      return (
        <div>
          Applicant name:  {data.name}
        </div>
      )
    })}
    </>

  )
}
export default App;
```

Here's the expected code output:

```react
Applicant name: Joe
Applicant name: janet
```

Unfortunately, a quick inspection of our current webpage throws this error about keys:

> react-jsx-dev-runtime.development.js:87 Warning: Each child in a list should have a unique "key" prop.  
>   
> Check the render method of `App`. See [https://reactjs.org/link/warning-keys](https://reactjs.org/link/warning-keys) for more information.  
> at div  
> at App  
> printWarning @ react-jsx-dev-runtime.development.js:87

## Why You Need Keys in Lists

While the above code works just fine, a key attribute when handling lists in React is key. The key attribute is very important in uniquely identifying each particular item in the array. 

React assigns every item a unique key attribute and so is able to keep track of them despite any changes. This helps in ensuring that you do not end up messing up your code when changes occur in your lists.

With the key attribute any changes such as re-ordering, adding, or removing items from the array be can tracked. This is a best practice.

Here is a code demo showing the key attribute at work:

```react
import React from 'react';


  const applicants = [ {
    name: 'Joe', work: 'freelance-developer',
    blogs: '54', websites: '32',
    hackathons: '6', location: 'morocco', id: '0',
  },
  {
    name: 'janet', work: 'fullstack-developer', 
    blogs: '34', websites: '12', 
    hackathons: '8', location: 'Mozambique', id: '1',
  },

];

function App() {
  return (
    <>
    {applicants.map(function(applicant) {
      return (
        <div key={applicant.id}>
          <p>Applicant Name: {applicant.name}</p>
          <p>Applicant location: {applicant.location}</p>
          <p>Hackathons participated: {applicant.hackathons}</p>

        </div>
      )
    })}
    </>
  );
};


        
  
export default App;
```

As you can see, a large set of applicants is smoothly mapped and displayed using a few lines of code.

At the same time, if you were to delete applicants who did not meet some qualifications, the key attribute would help keep track of the remaining applicants using the unique assigned  key.

This is the expected code output:

```react
Applicant Name: Joe

Applicant location: Morocco

Hackathons participated: none

Applicant Name: Janet

Applicant location: Mozambique

Hackathons participated: 6
```

In the above examples, you're only dealing with a single variable. 

Now, there will be cases in your work where you will have different files and more than one variable in different React components. 

This is where React `props` come in. 

## What are Props in React?

The word 'props' stands for properties and they are used to pass data from one component to another. Props are useful in passing data and help you write clean and lightweight code.

The array we're using has a variable named `applicants`. You have a new component that showcases the applicants' names, number of websites built, and their respective locations. 

How then do you pass the list to this new component?

`<ShowcaseApplicants applicants={applicants} />`

You can easily get the applicants data from the `props` object as shown below:

```react
import React from 'react';

const App = () => {
  const applicants = [ {
    name: 'Joe', work: 'freelance-developer',
    blogs: '54', websites: '32',
    hackathons: '6', location: 'morocco', id: '0',
  },
  {
    name: 'janet', work: 'fullstack-developer', 
    blogs: '34', websites: '12', 
    hackathons: '8', location: 'Mozambique', id: '1',
  },

]


return (
  <div>
    <h1>Oh! Hello World</h1>

    <ShowcaseApplicants applicants={applicants} />

  </div>
)

function ShowcaseApplicants(props) {
  const applicants = props.applicants

  return (

    <div>
    {applicants.map((applicant) => (

      <div key={applicant.id}>
        <p>
          Applicant Name: <span>{applicant.name}</span>
        </p>
        <p>
          Websites built: <span>{applicant.websites}</span>
        </p>
        <p>Applicant location: <span>{applicant.location}</span>
        </p>
      </div>  

    ))}
    </div>
  );
}
}

        
  
export default App;
```

Inside the the `App` component, we included `applicants` as a local variable. With that we don't pollute the global scope. We then returned a `div` with an `h1` tag.

Next, we want to pass the data in the array to a new component that showcases further data about each applicant. With the `ShowcaseApplicants` instantiation, the component accesses the array using the `applicants` props. 

After that was done, we used `array.map()` to map the applicants' name, number of websites built, and location which was rendered as JSX. And we didn't forget the important key attribute.

Here is the expected code output:

```react
Oh! Hello World
Applicant name: Joe

Websites built: 32

Applicant location: Morocco

Applicant name: Janet

Websites built: 12

Applicant location: Mozambique
```

## Conclusion

In this article you have learned how to use the JavaScript `map()` method to render a list of items in React. You also learned how to use React `props` to pass the lists data into other components as well. 

