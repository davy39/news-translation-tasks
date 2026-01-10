---
title: Here’s how to optimize the state shape of your React app with Redux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-19T12:19:37.000Z'
originalURL: https://freecodecamp.org/news/optimising-the-state-shape-of-your-react-app-with-redux-3a280e6ef436
coverImage: https://cdn-media-1.freecodecamp.org/images/1*MYp1pEZVIvemp_Af2P34FQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ivan Pilot

  Using Redux to manage the entire state of you app is one thing. But making sure
  the structure of your state is optimal so that your code is maintainable and efficient
  is an entirely new ball game!


  _Photo by [Unsplash](https://unsplash....'
---

By Ivan Pilot

Using Redux to manage the entire state of you app is one thing. But making sure the structure of your state is optimal so that your code is maintainable and efficient is an entirely new ball game!

![Image](https://cdn-media-1.freecodecamp.org/images/1*MYp1pEZVIvemp_Af2P34FQ.jpeg)
_Photo by [Unsplash](https://unsplash.com/photos/JuFcQxgCXwA?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Samuel Zeller</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Managing the state shape of your app is absolutely fundamental. As your app grows, if your state shape is not well organized, managing it can quickly become messy and even slow down your app’s responsiveness.

If you use React as a front-end framework, chances are you might use Redux to manage the state of your app. In that case, you will implement one or several reducers to modify the state of your app each time an action is dispatched in response to users’ actions. Let’s see below how to move from an initial inefficient state shape structure to one that’s a top-performer.

### Initial state shape approach

Let’s assume we are writing an app where users can publish tweets, and each tweet has comments. Let’s also assume that tweets can be organized by topics or threads. A basic and inefficient state shape would be the following:

As you can see above, we have a complex nested structure. This state shape turns out to be quite inefficient for several reasons:

* It is deeply nested, so modifying the state to update a property of a tweet requires the developer to write an extensive amount of code in the reducer.
* The `tweets` array is doing two things: it is holding the data (i.e. individual `tweet` object), and ordering the tweets since the tweets are inside an array.
* In that situation, arrays are inefficient. Imagine that you have 50,000 tweets in a thread. Finding the appropriate tweet inside the array will take time. Search time inside an array is O(n) as the computer needs to go through the entire list of items until it finds the right one.
* Note that for the sake of the example, I didn’t even include the comments related to each `tweet` in this above structure, as it would have been even messier.

Don’t use arrays to hold complex objects. As we will see later, the only point of using arrays in our state is for ordering elements. This is because, unlike with arrays, we can’t rely on objects for ordering the elements they contain.

### Replace arrays by objects

An easy and first improvement would be to use objects instead of arrays. Using our previous example and focusing, for now, on the `tweets` array only, we could easily modify it like this:

We modified the previous `tweets` array and separated the work it had to do by

1. Creating a `byId` object whose job is only to hold individual tweets
2. Creating an `allIds` array whose job is to sort the tweets — but here we can just put the id of each tweet instead of the whole `tweet`.

The current structure is already much more efficient than the first one. To find a tweet, we will now search it through an object instead of an array. Search time through an object is constant time, i.e. O(1), which is a big improvement compared to O(n). In addition, we don’t care anymore about the position of each tweet inside the `byId` object. The `allIds` array is here to sort the tweets, and it is now much simpler to work with a basic array like `allIds`.

### Including comments for each tweet

Without making our code messier, we can now add the comments that would belong to each tweet. One method of implementation would be the following:

Shaping our state that way turns out to be much more efficient compared to the first example we used. Inside each tweet object, we only reference the comments that belong to it through an array of comment ids. Somewhere else we have a `comments` object inside which we can retrieve information about each comment.

We now have a more “flattened” structure on which we can work efficiently. Updating this state shape would require a small amount of code inside our reducers. Our code is now easily maintainable, and we reduced the chances of making mistakes.

### Putting it all together

Let’s see what would be the end result compared to our initial approach.

Unlike the first approach, where we were mixing arrays and objects making the state hard and painful to modify and maintain, this final approach is now easy to work with. Our code is easily maintainable and our search operations are super fast. It is clearly a win!

Let’s consider a few situations to see what should be done when modifying some items:

#### Add a tweet

* Create a new `tweet` object in the `byId` object of the `tweets` object
* Add the id of the new tweet to the `allIds` array of the `tweets` object
* Add the id of the new tweet to the `tweets` array inside the appropriate `thread` object

#### Edit a tweet

* Find the selected `tweet` object by its id inside the `byId` object of the `tweets` object and update it

#### Delete a tweet

* Find the selected `tweet` object by its id inside the `byId` object of the `tweets` object and delete it
* Delete the tweet id inside the `allIds` array of the `tweets` object
* Delete the tweet id inside the `tweets` array of the appropriate `thread` object

#### Add a comment

* Create a new `comment` object in the `byId` object of the `comments` object
* Add the id of the new comment to the `allIds` array of the `comments` object
* Add the id of the new comment to the `comments` array inside the appropriate `tweet` object

#### Edit a comment

* Find the selected `comment` object by its id inside the `byId` object of the `comments` object and update it

### Selectors

One way to think about selectors is to draw a parallel with getter and setter. Dispatch is like a setter since it modifies the state, while a selector is like a getter since it retrieves data.

You will generally use selectors within your container components when mapping the state to props with `mapStateToProps`. Suppose (as indicated in our example) that each tweet has a `isEditable` property that is either `true` or `false` , and that only one tweet at a time can be editable. If you want to retrieve the editable tweet you can write a selector like the one below:

I just provided one example but you can write as many selectors as you need depending on the data you wish to retrieve.

Also, and as recommended by Dan Abramov, it is best to write your selectors in the same file as your reducer. This makes sense especially if you think of them as getters/setters. Additionally, you can also refer to the Redux [documentation](https://redux.js.org/docs/recipes/StructuringReducers.html) which provides detailed information.

Have fun implementing Redux!

Cheers!

