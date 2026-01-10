---
title: How to get a new access token using Redux observables and the refresh token
  API
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-22T16:21:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-a-new-access-token-using-redux-observables-and-the-refresh-token-api-d38d875a8add
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0nvsQXICkyKVMAq4hbYRPg.jpeg
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Sachin Kumar

  This article is about how I handled a 401 status code on an API response. I will
  show you how to get a new access token using the refresh token with Redux Observable
  in a React project.

  However before we begin, we should understand so...'
---

By Sachin Kumar

This article is about how I handled a 401 status code on an API response. I will show you how to get a new access token using the refresh token with [**Redux Observable**](https://redux-observable.js.org/) in a [React](https://reactjs.org/) project.

However before we begin, we should understand some of the prerequisite concepts that will help up understand the solution better. This is a general architectural solution to a common problem, so you don’t need to know [**Redux**](https://redux.js.org/) to read further. Let us begin!

### **Access token**

> Access Token is a credential that can be used by an application to access an API. When an access token expires, it throws **401** status code in error response.  
> The below flowchart shows, how an access token works with the server. — [auth0.com](https://auth0.com/docs/tokens/access-token)

![Image](https://cdn-media-1.freecodecamp.org/images/1*SSh_IFE-CEs5dUV2UGleNg.png)
_API receive access token from auth server._

This is how an auth service works when the user successfully logs in and retrieves an access token and refreshes the token on successful authentication.

### **Refresh Token**

> A Refresh Token is a special kind of token that can be used to obtain a renewed access token — that allows accessing a protected resource — at any time. You can request new access tokens until the refresh token is blacklisted. Refresh tokens must be stored securely by an application because they essentially allow a user to remain authenticated forever. — [auth0.com](https://auth0.com/docs/tokens/access-token)

We need to get a new access token using that refresh token, then again hit the same API with the new access token. We want to do this without the user knowing that their session has expired or the API throwing an error.

Let’s understand how the refresh token works with the server. We retrieve a new access token when the API throws a 401 status code.

![Image](https://cdn-media-1.freecodecamp.org/images/1*G0SuCVnu90Q5suy0qQiJaA.png)
_This is how a refresh token receives a new token using the access token_

The refresh token API call receives a new access token from the auth server using the refresh token saved on the first authentication.

We can better understand this whole process via this simple flow chart.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5vWZxAH-ffLyThTCwTp9ww.png)

### **Observables**

You can think of an observable as an array whose items arrive asynchronously over time. **Observables help you manage asynchronous data**, such as data coming from a backend service.

In RxJS, this can become pretty complex when playing with observable streams. Don’t worry — we are going to simplify this with simple code chunks.

Let’s start with a simple API call in redux-observable. This is what a simple function for a fetch API looks like :

### Solution

Now we are armed with the basic concepts. Let us see how we can handle a 401 (invalid_token or session expired) status code on an API response. We’ll also see how we can get the new access token using the refresh token in Redux Observable.

We have to make two changes in the above function:

1. Wrap our API call in Observables.defer(). We want to get ahold of that function to call again when the new valid access token is received.
2. When we get a 401 status in catch error. We need to make an API call to get the new access token. We use the refresh token stored in the first successful authentication.

Let’s see the differences between the two functions:

1. The catch function always gives the **source** of the parent stream. We can use that to start the stream again which failed due to an invalid access token.
2. Now start a new stream of events to listen for refresh token success events. We stop when the refresh token API fails (use takeUntil for this).
3. Now make sure you use the **take** operator to always get the first event of the stream. If you have multiple streams, your output stream can be compromised.
4. If the new access token has been received, then use mergeMap to merge the source of the previous stream. We merge it again to the parent stream, and it will call the get data function with the new access token.
5. Now you might be wondering how merge is working. So, merge independently invokes and will start its own stream to fetch the new access token using the refresh token (check out the next function). When the refresh token success appears, it will get to **step 2** and so on.

We can use this approach to handle more special cases for different status code as well like 500, 403.

**ProTip**: make sure to check for infinite loop condition if the refresh token API gives a 401. You can maintain a counter on every refresh token call. If the number exceeds, stop the stream. Then do any error handling on it, for example showing a message that there was an error, and logout the user.

### Conclusion

We have implemented an invalid token handler using a refresh token API with Redux-observables in React. This approach can be used to handle other special API cases as well.

_I hope you enjoyed the post, if you like it follow me on [Twitter](https://twitter.com/_i_am_sachin) and [Github](https://github.com/sachinKumarGautam) for more JavaScript tips and articles. ?_

### Some helpful resources

1. [https://redux-observable.js.org/](https://redux-observable.js.org/)
2. [https://rxjs-dev.firebaseapp.com/api](https://rxjs-dev.firebaseapp.com/api)
3. [https://rxjs-dev.firebaseapp.com/api/index/function/defer](https://rxjs-dev.firebaseapp.com/api/index/function/defer)
4. [https://rxjs-dev.firebaseapp.com/api/index/function/merge](https://rxjs-dev.firebaseapp.com/api/index/function/merge)

