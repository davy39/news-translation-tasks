---
title: GraphQL VS REST – Benefits and Code Example Comparisons
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-18T23:26:50.000Z'
originalURL: https://freecodecamp.org/news/graphql-vs-rest-benefits-and-code-example-comparisons
coverImage: https://cdn-media-2.freecodecamp.org/w1280/60524e9d28094f59be25788f.jpg
tags:
- name: api
  slug: api
- name: GraphQL
  slug: graphql
- name: REST API
  slug: rest-api
seo_title: null
seo_desc: "By Veronica Stork\nREST was not the first protocol for sending information\
  \ over the web. But for over a decade, it has dominated the API landscape. \nMore\
  \ recently, GraphQL, a newcomer designed by Facebook, has become more and more popular.\
  \ It is inten..."
---

By Veronica Stork

REST was not the first protocol for sending information over the web. But for over a decade, it has dominated the API landscape. 

More recently, GraphQL, a newcomer designed by Facebook, has become more and more popular. It is intended to correct some of REST’s weaknesses, but no technology is perfect. 

What are the benefits of GraphQL over REST, and why would you use one over the other in your project?

## Issues with REST APIs

First, let’s discuss some of REST’s weaknesses and how GraphQL attempts to solve them. There are three main ones: excessive trips to the server, over/under fetching, and a general lack of flexibility.

### Too Many Trips to the Server with REST APIs

Let’s say we're creating a social media app. The feed might display the most recent posts from all users, along with the usernames and profile pics. 

In REST, you would, for example, need to send a GET request to _/api/posts_ to get the posts, which would probably return a JSON object containing the post title, content, tags, date, and maybe the user ID. 

Then, you might need to send a GET request to _/api/users/:id/_ for each post in order to get information about the users' usernames, avatars, and any other relevant information. 

When you consider that you are possibly making a GET request for every user, that's a lot of back and forth for one page!

With GraphQL, you can make one trip to the server and get everything you need:

```js
query {
    posts {
        title,
        content,
        tags,
        date,
        user {
        	username,
            avatar,
            catchphrase,
            favorite_dog
        }
    }
}
```

On a small scale, multiple trips to the server are not a big deal. But once you're working with a ton of data, you'll obviously benefit from reducing API calls to a minimum. GraphQL makes that easy to accomplish.

### Over- and Under- Fetching in REST APIs

A related issue is that of over and under fetching. In a REST API, when you hit an endpoint, you will always get the same data back, regardless of whether you need it all. 

Say we just need someone's username and avatar. If  _/user/:id_ returns their username, avatar, catchphrase, and favorite breed of dog, you are going to get all of that info, whether you want it or not. 

On the other end of the spectrum, you can end up _under_-fetching, which necessitates going back to the server for more information, as described in the previous section. 

To display a single user’s posts, we need both the user info and the contents of the posts. If I fetch the user from the user endpoint, I still need to then hit the posts endpoint, and, using the userid, retrieve the posts. 

```js
// First we get the user's info
GET /api/users/42

{
    "username": "Mr. T",
    "avatar": "http://example.com/users/42/pic.jpg",
    "catchphrase": "I pity the fool",
    "favorite_dog": "beagle"
}

// Then we get their posts
GET /api/users/42/posts

{
    "posts": [{
        "title": "Hello World",
        "content": "Hi everyone!"
        "tags": "first post"
        "date": "July 1, 2020"
    }]
    // etc.
}

        
        
    
```

As we saw in the previous example, GraphQL solves this issue by allowing the user to use one endpoint and only fetch exactly what they need. 

### Lack of Flexibility in REST APIs

Expanding on the previous point, REST relies on creating APIs that match the needs of the frontend. If you can anticipate what the frontend will need when it hits a particular endpoint, you can precisely tailor the data retrieved to match that view. 

This works well when the view is relatively static. But if your frontend changes frequently, you will want an API with more flexibility in what data it returns. 

Similarly, if your API is used by a variety of different clients with different needs, the inflexibility of a REST API will not suit your purposes. 

GraphQL provides that flexibility by allowing for the retrieval of different configurations of data.

```js
// If I just need the username and avatar:

query {
	users {
    	username,
        avatar
    }
}

// If I need their favorite dog breed, too.

query {
    users {
        username,
        avatar,
        favorite_dog
    }
}
    
```

## Should You Use Rest or GraphQL?

It may seem from this article that GraphQL is always better than REST, but that’s not necessarily the case. Every architectural decision you make when building your app has its pros and cons, and this is no exception. 

Here are some things to consider:

### If you need something easy to use, choose GraphQL.

Doing REST right has a learning curve, and if you don’t know it already, you will have an easier time creating a great API if you use GraphQL. 

> By going with GraphQL, you will generally end up with a much better API than if you would attempt to build a REST API without understanding its concepts. -[Zdenek “Z” Nemec](https://goodapi.co/blog/rest-vs-graphql)

### If you use GraphQL, decide how you will handle errors

REST APIs are better able to leverage the error reporting features of HTTP. If you don’t want to get back a 200 OK status for client-side errors (as is common in GraphQL), you’ll need to think a bit more about error handling.

### REST may be better for microservices

If you use microservices on the backend, REST might work better for your purposes, as it is made to keep concerns separate. 

GraphQL’s unified “graph” of data is great if you don’t need to use different, disparate resources that are possibly written in different programming languages, but not as useful if you have a more distributed backend.

### Consider caching

Caching is something that is built-in with REST, but that you will have to manage yourself with GraphQL. All of that increased efficiency you may get from GraphQL’s more targeted fetching could be erased if you don’t build in caching where appropriate.

## Conclusion

As with everything, there are some trade-offs to consider when deciding between REST and GraphQL. Which you choose for your project will depend on your needs and resources.

  

