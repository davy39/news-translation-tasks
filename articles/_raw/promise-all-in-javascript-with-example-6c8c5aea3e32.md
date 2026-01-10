---
title: All you need to know about Promise.all
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-05T20:47:50.000Z'
originalURL: https://freecodecamp.org/news/promise-all-in-javascript-with-example-6c8c5aea3e32
coverImage: https://cdn-media-1.freecodecamp.org/images/1*oPnpG64cvwTL8DHiaYSFew.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Srebalaji Thirumalai

  Promises in JavaScript are one of the powerful APIs that help us to do Async operations.

  Promise.all takes Async operations to the next new level as it helps you to aggregate
  a group of promises.

  In other words, I can say that...'
---

By Srebalaji Thirumalai

Promises in JavaScript are one of the powerful APIs that help us to do Async operations.

Promise.all takes Async operations to the next new level as it helps you to aggregate a group of promises.

In other words, I can say that it helps you to do concurrent operations (sometimes for free).

#### Prerequisites:

You have to know what is a **Promise** in JavaScript.

#### What is Promise.all?

Promise.all is actually a promise that takes an array of promises as an input (an iterable). Then it gets resolved when all the promises get resolved or any one of them gets rejected.

For example, assume that you have ten promises (Async operation to perform a network call or a database connection). You have to know when all the promises get resolved or you have to wait till all the promises resolve. So you are passing all ten promises to Promise.all. Then, Promise.all itself as a promise will get resolved once all the ten promises get resolved or any of the ten promises get rejected with an error.

**Let’s see it in code:**

```
Promise.all([Promise1, Promise2, Promise3])
 .then(result) => {
   console.log(result)
 })
 .catch(error => console.log(`Error in promises ${error}`))
```

As you can see, we are passing an array to Promise.all. And when all three promises get resolved, Promise.all resolves and the output is consoled.

**Let’s see an example:**

```js
// A simple promise that resolves after a given time
const timeOut = (t) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(`Completed in ${t}`)
    }, t)
  })
}

// Resolving a normal promise.
timeOut(1000)
 .then(result => console.log(result)) // Completed in 1000

// Promise.all
Promise.all([timeOut(1000), timeOut(2000)])
 .then(result => console.log(result)) // ["Completed in 1000", "Completed in 2000"]
```

In the above example, Promise.all resolves after 2000 ms and the output is consoled as an array.

One interesting thing about Promise.all is that the order of the promises is maintained. The first promise in the array will get resolved to the first element of the output array, the second promise will be a second element in the output array and so on.

**Let’s see another example:**

```js
// A simple promise that resolves after a given time
const timeOut = (t) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(`Completed in ${t}`)
    }, t)
  })
}

const durations = [1000, 2000, 3000]

const promises = []

durations.map((duration) => {
  // In the below line, two things happen.
  // 1. We are calling the async function (timeout()). So at this point the async function has started and enters the 'pending' state.
  // 2. We are pushing the pending promise to an array.
  promises.push(timeOut(duration)) 
})

console.log(promises) // [ Promise { "pending" }, Promise { "pending" }, Promise { "pending" } ]

// We are passing an array of pending promises to Promise.all
// Promise.all will wait till all the promises get resolves and then the same gets resolved.
Promise.all(promises)
.then(response => console.log(response)) // ["Completed in 1000", "Completed in 2000", "Completed in 3000"]

```

From the above example, it’s clear that Promise.all waits till all the promises resolve.

Let’s see what happens if any one of the promises are rejected.

```js
// A simple promise that resolves after a given time
const timeOut = (t) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (t === 2000) {
        reject(`Rejected in ${t}`)
      } else {
        resolve(`Completed in ${t}`)
      }
    }, t)
  })
}

const durations = [1000, 2000, 3000]

const promises = []

durations.map((duration) => {
  promises.push(timeOut(duration)) 
})

// We are passing an array of pending promises to Promise.all
Promise.all(promises)
.then(response => console.log(response)) // Promise.all cannot be resolved, as one of the promises passed got rejected.
.catch(error => console.log(`Error in executing ${error}`)) // Promise.all throws an error.

```

As you can see, if one of the promises fails, then all the rest of the promises fail. Then Promise.all gets rejected.

For some use cases, you don’t need that. You need to execute all the promises even if some have failed, or maybe you can handle the failed promises later.

Let’s see how to handle that.

```js
const durations = [1000, 2000, 3000]

promises = durations.map((duration) => {
  return timeOut(duration).catch(e => e) // Handling the error for each promise.
})

Promise.all(promises)
  .then(response => console.log(response)) // ["Completed in 1000", "Rejected in 2000", "Completed in 3000"]
  .catch(error => console.log(`Error in executing ${error}`))
view raw
```

#### Use cases of Promise.all

Assume that you have to perform a huge number of Async operations like sending bulk marketing emails to thousands of users.

Simple pseudo code would be:

```
for (let i=0;i<50000; i += 1) {
 sendMailForUser(user[i]) // Async operation to send a email
}
```

The above example is straightforward. But it’s not very performant. The stack will become too heavy and at one point of time, JavaScript will have a huge number of open HTTP connection which may kill the server.

A simple performant approach would be to do it in batches. Take first 500 users, trigger the mail and wait till all the HTTP connections are closed. And then take the next batch to process it and so on.

Let’s see an example:

```js
// Async function to send mail to a list of users.
const sendMailForUsers = async (users) => {
  const usersLength = users.length
  
  for (let i = 0; i < usersLength; i += 100) { 
    const requests = users.slice(i, i + 100).map((user) => { // The batch size is 100. We are processing in a set of 100 users.
      return triggerMailForUser(user) // Async function to send the mail.
       .catch(e => console.log(`Error in sending email for ${user} - ${e}`)) // Catch the error if something goes wrong. So that it won't block the loop.
    })
    
    // requests will have 100 or less pending promises. 
    // Promise.all will wait till all the promises got resolves and then take the next 100.
    await Promise.all(requests)
     .catch(e => console.log(`Error in sending email for the batch ${i} - ${e}`)) // Catch the error.
  }
}


sendMailForUsers(userLists)
```

Let’s consider another scenario: You have to build an API that gets information from multiple third-party APIs and aggregates all the responses from the APIs.

Promise.all is the perfect way of doing that. Let’s see how.

```js
// Function to fetch Github info of a user.
const fetchGithubInfo = async (url) => {
  console.log(`Fetching ${url}`)
  const githubInfo = await axios(url) // API call to get user info from Github.
  return {
    name: githubInfo.data.name,
    bio: githubInfo.data.bio,
    repos: githubInfo.data.public_repos
  }
}

// Iterates all users and returns their Github info.
const fetchUserInfo = async (names) => {
  const requests = names.map((name) => {
    const url = `https://api.github.com/users/${name}`
    return fetchGithubInfo(url) // Async function that fetches the user info.
     .then((a) => {
      return a // Returns the user info.
      })
  })
  return Promise.all(requests) // Waiting for all the requests to get resolved.
}


fetchUserInfo(['sindresorhus', 'yyx990803', 'gaearon'])
 .then(a => console.log(JSON.stringify(a)))

/*
Output:
[{
  "name": "Sindre Sorhus",
  "bio": "Full-Time Open-Sourcerer ·· Maker ·· Into Swift and Node.js ",
  "repos": 996
}, {
  "name": "Evan You",
  "bio": "Creator of @vuejs, previously @meteor & @google",
  "repos": 151
}, {
  "name": "Dan Abramov",
  "bio": "Working on @reactjs. Co-author of Redux and Create React App. Building tools for humans.",
  "repos": 232
}]
*/

```

To conclude, Promise.all is the best way to aggregate a group of promises to a single promise. This is one of the ways of achieving concurrency in JavaScript.

Hope you liked this article. If you did, please clap and share it.

Even if you didn’t, that’s fine you can do it anyway :P

