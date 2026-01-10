---
title: How to make your code better with intention-revealing function names
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-24T00:13:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-code-better-with-intention-revealing-function-names-6c8b5271693e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*C0YINGVSuF-kLTCynyBwCw.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  Code is a way to communicate with developers reading it. Functions with intention-revealing
  names are easier to read. We ...'
---

By Cristian Salcescu

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

Code is a way to communicate with developers reading it. Functions with intention-revealing names are easier to read. We read the function name and can understand its purpose. The function name is our tool for expressing intent on a piece of code.

Let’s look at a [list of operations done in a functional style](https://jsfiddle.net/cristi_salcescu/pujuve88/) with the use of anonymous functions.

```
function getTodos(users){
  return todos
    .filter(todo => !todo.completed && todo.type === "RE")
    .map(todo => ({
      title : todo.title,
      userName : users[todo.userId].name
    }))
    .sort((todo1, todo2) =>  
      todo1.userName.localeCompare(todo2.userName));
}
```

Now check the same functionality refactored using functions with intention-revealing names.

```
function isTopPriority(todo){
  return !todo.completed && todo.type === "RE";
}

function ascByUserName(todo1, todo2){
  return todo1.userName.localeCompare(todo2.userName);
}
  
function getTodos(users){
  function toViewModel(todo){
    return {
      title : todo.title,
      userName : users[todo.userId].name
    }
  }
  return todos.filter(isTopPriority)
              .map(toViewModel).sort(ascByUserName);
}
```

Function names give clarity to the code. With a good function name, you just have to read the name — you don’t need to analyze its code to understand what it does.

> _It’s widely estimated that developers spend 70% of code maintenance time on reading to understand it._

> _Kyle Simpson in [Functional-Light JavaScript](https://www.amazon.com/Functional-Light-JavaScript-Pragmatic-Balanced-FP-ebook/dp/B0787DBFKH/ref=sr_1_1?ie=UTF8&qid=1519405569&sr=8-1&keywords=kyle+simpson+functional&dpID=41de4aNCSQL&preST=_SX342_QL70_&dpSrc=srch)_

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**For more on applying functional programming techniques in React take a look at** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Learn **functional React**, in a project-based way, with [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Follow on Twitter](https://twitter.com/cristi_salcescu)

