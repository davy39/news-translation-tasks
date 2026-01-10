---
title: How point-free composition will make you a better functional programmer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-14T22:32:33.000Z'
originalURL: https://freecodecamp.org/news/how-point-free-composition-will-make-you-a-better-functional-programmer-33dcb910303a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*a5N4vokpfnlmUnnJMou9zw.jpeg
tags:
- name: coding
  slug: coding
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!


  "Point-free style — aims to reduce some of the visual clutter by removing unnecessary
  parameter-argument mapping." - Kyl...'
---

By Cristian Salcescu

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

> "Point-free style — aims to reduce some of the visual clutter by removing unnecessary parameter-argument mapping." - Kyle Simpson in [Functional-Light JavaScript](https://www.amazon.com/Functional-Light-JavaScript-Pragmatic-Balanced-FP-ebook/dp/B0787DBFKH/ref=sr_1_1?ie=UTF8&qid=1519405569&sr=8-1&keywords=kyle+simpson+functional&dpID=41de4aNCSQL&preST=_SX342_QL70_&dpSrc=srch)

Consider the flowing code:

```
let newBooks = books.filter(point => isTechnology(point))
```

Now look at the same code after eliminating points (parameters/arguments):

```
let newBooks = books.filter(isTechnology)
```

### Point-free in List Operations

Let’s do list operations in a point-free style.

Say we need to find the technology titles in a list of books, prepare the book object with all information for the view, and sort the books by the author’s name.

[Here](https://jsfiddle.net/cristi_salcescu/j2mzyvau/) is how the code would look:

```
function getBooks(){
  return books.filter(isTechnology)
              .map(toBookView)
              .sort(ascByAuthor);
}

//Small functions with points
function isTechnology(book){
   return book.type === "T";
}

function toBookView(book){
  return Object.freeze({
    title : book.title,
    author : authors[book.authorID].name
  });
}
  
function ascByAuthor(book1, book2){
  if(book1.author < book2.author) return -1;
  if(book1.author > book2.author) return 1;
  return 0;
}
```

The callbacks `isTechnology()`, `toBookView()`, `ascByAuthor()` are small functions with intention-revealing names. They are not built in a point-free style.

The code assembling all these functions in `getBooks()` is point-free.

#### Decomposition and composition

Our natural way of dealing with a problem is to break it into smaller pieces and then put everything back together.

We break the bigger task up into several functions doing smaller tasks. Then we re-combine these smaller functions to solve the initial problem.

Let’s read the requirements again:

> We need to find the technology titles in a list of books, prepare the book object with all information for the view, and sort the books by the author’s name.

We created:

* `isTechnology()` predicate to check if it’s a technology book
* `toViewBook()` to build an object with all the information for the view
* `ascByAuthorname()` to sort two books ascending by the author’s name
* `getBooks()` to combine all these small functions together in a point-free style

```
function getBooks(){
  return books.filter(isTechnology)
              .map(toBookView)
              .sort(ascByAuthor);
}
```

### Steps towards point-free composition

There is no additional anonymous callback when doing point-free composition. No `function` keyword, no arrow syntax `=&`gt; . All we see are function names.

* In most cases, extract out the callbacks in named functions.
* In simple cases, just use an utility function from the toolbox to create the callback on the fly. [Look at](#2428) the `prop()` function, for example.
* Write the coordinator function in a point-free style.

#### Small functions

The consequence of writing code this way is a lot of small functions with intention revealing names. Naming these small functions requires time, but if it’s done well, it will make the code easier to read.

There will be two kinds of functions:

* Functions doing one task: they are pure or closure functions. Usually they are not built in a point-free style, but instead have good names.
* Functions coordinating a lot of tasks: joining these small tasks in a point-free style makes it easier to read.

#### Not everything is point-free

I’m not aiming at having everything point-free. I’m aiming for point-free in specific places, especially when composing functions.

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**For more on applying functional programming techniques in React take a look at** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Learn **functional React**, in a project-based way, with [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Follow on Twitter](https://twitter.com/cristi_salcescu)

