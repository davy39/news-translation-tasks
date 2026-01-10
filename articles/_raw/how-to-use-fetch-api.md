---
title: How to Use Fetch to Make AJAX Calls in JavaScript
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2020-06-26T17:43:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-fetch-api
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a08740569d1a4ca231d.jpg
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: beginner
  slug: beginner
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'I will be sharing bite sized learnings about JavaScript regularly in this
  series. We''ll cover JS fundamentals, browsers, DOM, system design, domain architecture
  and frameworks.

  Fetch is an interface for making an AJAX request in JavaScript. It is imp...'
---

I will be sharing bite sized learnings about JavaScript regularly in this series. We'll cover JS fundamentals, browsers, DOM, system design, domain architecture and frameworks.


Fetch is an interface for making an AJAX request in JavaScript. It is implemented widely by modern browsers and is used to call an API. 


````javascript
const promise = fetch(url, [options])

````

Calling fetch returns a promise, with a Response object. The promise is rejected if there is a network error, and it's resolved if there is no problem connecting to the server and the server responded a status code. This status code could be 200s, 400s or 500s.

A sample FETCH request - 
```javascript

fetch(url)
  .then(response => response.json())
  .catch(err => console.log(err))

```

The request is sent as a GET by default. To send a POST / PATCH / DELETE / PUT you can use the method property as part of `options` parameter. Some other possible values `options` can take - 

- `method`:  such as GET, POST, PATCH
- `headers`: Headers object
- `mode`:  such as `cors`, `no-cors`, `same-origin`
- `cache`: cache mode for request
- `credentials`
- `body`

[Check out the full list of available options here]('https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/fetch')


Example usage:
This example demonstrates the usage of fetch to call an API and to get a list of git repositories.
``` javascript
const url = 'https://api.github.com/users/shrutikapoor08/repos';

fetch(url)
  .then(response => response.json())
  .then(repos => {
    const reposList = repos.map(repo => repo.name);
    console.log(reposList);
  })
.catch(err => console.log(err))

```


To send a POST request, here's how the method parameter can be used with async / await syntax.

```javascript
const params = {
  id: 123
}

const response = await fetch('url', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(params)
});

const data = await response.json();
```

---
### Interested in more JSBytes? [ Sign up for the newsletter](https://tinyletter.com/shrutikapoor )


