---
title: How to Destructure Object Properties Using array.map() in React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-11-02T17:07:58.000Z'
originalURL: https://freecodecamp.org/news/destructure-object-properties-using-array-map-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/pexels-pixabay-276502.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: null
seo_desc: "By Caleb Olojo\nOne of the methods frontend developers use the most in\
  \ JavaScript is the Array.prototype.map() method. \nFrom having to render a list\
  \ of items in the DOM to looping through a series of blog posts – and many more\
  \ – the usefulness goes on..."
---

By Caleb Olojo

One of the methods frontend developers use the most in JavaScript is the `Array.prototype.map()` method. 

From having to render a list of items in the DOM to looping through a series of blog posts – and many more – the usefulness goes on and on.

Say you have a list of items in an array that needs to be rendered as a React component onto a web page. The ideal way to map a series of items in an array looks like this:

```js
const shoppingList = ['Oranges', 'Cassava', 'Garri', 'Ewa', 'Dodo', 'Books']

export default function List() {
  return (
    <>
      {shoppingList.map((item, index) => {
        return (
          <ol>
            <li key={index}>{item}</li>
          </ol>
        )
      })}
    </>
  )
}

```

The snippet above pretty much fulfills its purpose. But what if you have to map through an array of objects with multiple properties? Say, an array like the one below?

```js
const employees = [
  {
    name: 'Saka Manje',
    address: '14, cassava-garri-ewa street',
    gender: 'Male',
  },
  {
    name: 'Wawawa Warisii',
    address: '406, highway street',
    gender: 'Male',
  },
]
```

To be concise, let's stick with two items in the array. Now, let's use the same approach that we used in the previous snippet.

```js
export default function EmployeesList() {
  return (
    <>
      {employees.map((employee, index) => {
        return (
          <div key={index}>
            <p>{employee.name}</p>
            <p>{employee.address}</p>
            <p>{employee.gender}</p>
          </div>
        )
      })}
    </>
  )
}
```

While the approach in the snippet above looks perfectly okay, you might wonder – "What happens when I get deeply nested objects as data from an endpoint?" 

## How to Destructure Object Properties

In the previous section, we went through the conventional way of rendering data from an API endpoint on a web page with JavaScript's `.map()` method. 

In this section, we'll take a look at how we can achieve the same result without using dot notation to access the properties in the array.

But, before we do that, what exactly does it mean to destructure object properties? Well, the purpose of destructuring is to be able to access variables within arrays or objects and then proceed by assigning them to a variable. You can see an example below.

```js
const person = {
  name: 'Adrian Tojubole',
  role: 'Lead Engineer',
  salary: '$130k/year',
}

let { name, role, salary } = person

console.log(name); // Adrian Tojubole
console.log(role); // Lead Engineer
console.log(salary); // $130k/year    
```

You'll notice that we were able to access the properties – `name`, `role`, and `salary` – of the `person` object. This was instead of using the dot notation to access them, like it is in the snippet below, which makes the process repetitive for us.

```js
console.log(person.name);
console.log(person.role);
console.log(person.salary);
```

With that out of the way, we'll take this pattern and use it whenever we want to use the `.map()` method in React. Take the array of objects below, for example:

```js
const employeesData = [
  {
    name: 'Saka manje',
    address: '14, cassava-garri-ewa street',
    attributes: {
      height: '6ft',
      hairColor: 'Brown',
      eye: 'Black',
    },
    gender: 'Male',
  },
  {
    name: 'Adrian Toromagbe',
    address: '14, kogbagidi street',
    attributes: {
      height: '5ft',
      hairColor: 'Black',
      eye: 'Red',
    },
    gender: 'Male',
  },
]
```

In the snippet above, you'll notice that we have an object nested inside another object, as a property. Now, the initial way you might access the properties in that nested object would look like this:

```js
employeesData.map(data => data.attributes.height);
```

But, when you destructure the properties in that object, the syntax looks somewhat like this:

```js
employeesData.map(
  ({ name, address, attributes: { height, hairColor, eye }, gender }, index) => {
    return name, address, height, hairColor, eye
  }
)
```

The snippet above eliminates the process of doing this: `employee.name`, `employee.attributes.height`, and so on.

Now, that you have an idea of how it works, it is time to place this `.map()` into a React component, then return the corresponding properties.

```js
export default function Employees() {
  return (
    <div>
      {employeesData.map(
        (
          { name, address, gender, attributes: { height, hairColor, eye } },
          index
        ) => {
          return (
            <div className="employees" key={index}>
              <p>{name}</p>
              <p>{address}</p>
              <p>{gender}</p>
              <p>{height}</p>
              <p>{eye}</p>
              <p>{hairColor}</p>
            </div>
          )
        }
      )}
    </div>
  )
}

```

## Wrapping Up

With this approach you can save a lot of time you spend using dot notation to access object properties. This is useful as time goes on, because you may begin to interface with GraphQL APIs, and some of these APIs are commonly known to have deeply nested objects being returned as data.

You can also destructure array properties, too. A great example is the way we destructure a `value` and the callback function `setValue` when we're using one of the popular React hooks – `useState`

```js
const [count, setCount] = React.useState(0)
```

Thank you for reading this tutorial. I hope you found it helpful.

