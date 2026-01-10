---
title: Iterate Through Nested Object in React.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:17:00.000Z'
originalURL: https://freecodecamp.org/news/iterate-through-nested-object-in-react-js
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9aa2740569d1a4ca26c5.jpg
tags:
- name: object
  slug: object
- name: React
  slug: react
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: "If you've ever worked with APIs, you'll know that the structure of the\
  \ data they return can get complicated quickly.\nImagine you call an API from your\
  \ React project and the response looks something like this:\nObject1 {\n     Object2\
  \ {\n           prope..."
---

If you've ever worked with APIs, you'll know that the structure of the data they return can get complicated quickly.

Imagine you call an API from your React project and the response looks something like this:

```json
Object1 {
     Object2 {
           propertyIWantToAcess:
           anotherpropertyIWantToAcess:
      }
}
```

You've stored the data within your component's state as `this.state.myPosts`, and can access the elements of the outer object with the following:

```jsx
render() {
    console.log(this.state.myPosts);

    const data = this.state.myPosts;

    const display = Object.keys(data).map((d, key) => {
    return (
      <div className="my-posts">
        <li key={key}>
          {data.current_route}
        </li>
      </div>
      );
    });

    return(
      <div>
        <ul>
          { display }
        </ul>
      </div>
    );
  }
```

But the problem is that you aren't able to access any of the inner objects.

The values of the inner objects will always change, so you aren't able to hardcode their keys and iterate through those to get the proper values.

## Possible solutions

It can be difficult to work directly with complex API responses, so let's take a step back and simplify:

```jsx
const visit = (obj, fn) => {
    const values = Object.values(obj)

    values.forEach(val => 
        val && typeof val === "object" ? visit(val, fn) : fn(val))
}

// Quick test
const print = (val) => console.log(val)

const person = {
    name: {
        first: "John",
        last: "Doe"
    },
    age: 15,
    secret: {
        secret2: {
            secret3: {
                val: "I ate your cookie"
            }
        }
    }
}

visit(person, print)
/* Output
John
Doe
15
I ate your cookie
*/
```

The `lodash` library has simple methods to accomplish the same thing, but this is a quick and dirty way to do the same thing in vanilla JS.

But say you want to simplify further, something like:

```jsx
render() {
    // Logs data
    console.log(this.state.myPosts);

    const data = this.state.myPosts;

    // Stores nested object I want to access in posts variable
    const posts = data.content;

    // Successfully logs nested object I want to access
    console.log(posts);

    // Error, this will not allow me to pass posts variable to Object.keys
    const display = Object.keys(posts).map(key =>
      <option value={key}>{posts[key]}</option>
    )


    return(
      <div>
        {display}
      </div>
    );
 }
```

But you get an error, `TypeError: can't convert undefined to object error` whenever you try to pass `posts` to `Object.keys`.

Keep in mind that this error has nothing to do with React. It's illegal to pass an object as a child of a component.

`Object.keys()` only returns the keys of the object that's passed in as a parameter. You'll need to call it multiple times to iterate through all the nested keys.

If you need to display the whole nested object, one option is to use a function to convert each object into a React component and pass it as an array:

```jsx
let data= []

visit(obj, (val) => {
    data.push(<p>{val}</p>)  // wraps any non-object type inside <p>
})
...
return <SomeComponent> {data} </SomeComponent>
```

## Useful packages

Another option is to use a package like [json-query](https://www.npmjs.com/package/json-query) to help iterate through the nested JSON data.

Here's a modified version of the `render` function above using `json-query`:

```jsx
 render() {
   const utopian = Object.keys(this.state.utopianCash);
   console.log(this.state.utopianCash);

   var author = jsonQuery('[*][author]', { data: this.state.utopianCash }).value
   var title = jsonQuery('[*][title]', { data: this.state.utopianCash }).value
   var payout = jsonQuery('[*][total_payout_value]', { data: this.state.utopianCash }).value
   var postLink = jsonQuery('[*][url]', { data: this.state.utopianCash }).value
   var pendingPayout = jsonQuery('[*][pending_payout_value]', { data: this.state.utopianCash }).value
   var netVotes = jsonQuery('[*][net_votes]', { data: this.state.utopianCash }).value


   let display = utopian.map((post, i) => {
     return (
       <div className="utopian-items">
        <p>
          <strong>Author: </strong>
          {author[i]}
        </p>
        <p>
          <strong>Title: </strong>
            <a href={`https://www.steemit.com` + postLink[i]}>{title[i]}</a>
        </p>
        <p>
          <strong>Pending Payout: </strong>
            {pendingPayout[i]}
        </p>
        <p>
          <strong>Votes: </strong>
          {netVotes[i]}
        </p>
       </div>
     );
   });

    return (
      <div className="utopian-container">
        {display}
        <User />
      </div>
    );
  }
}
```

