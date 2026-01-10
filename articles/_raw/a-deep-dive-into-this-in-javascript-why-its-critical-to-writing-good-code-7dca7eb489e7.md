---
title: 'A deep dive into this in JavaScript: why it’s critical to writing good code.'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-09T18:19:50.000Z'
originalURL: https://freecodecamp.org/news/a-deep-dive-into-this-in-javascript-why-its-critical-to-writing-good-code-7dca7eb489e7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hVnCdEtqlQvHS1GTXbo5Xw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Austin Tackaberry

  Using simple terminology and a real world example, this post explains what this
  is and why it is useful.

  Is this for you

  I have noticed that many explanations for this in JavaScript are taught assuming
  you are coming from some ob...'
---

By Austin Tackaberry

Using simple terminology and a real world example, this post explains what `this` is and why it is useful.

### Is this for you

I have noticed that many explanations for `this` in JavaScript are taught assuming you are coming from some object-oriented programming language like Java, C++, or Python. This post is geared towards those of you who have no preconceptions of what you think `this` is or what it should be. I will try to explain **what** `this` is and **why** it is helpful in a simple manner without unnecessary jargon.

Maybe you procrastinated diving into `this` because it looked weird and scary. Or maybe you only use it because StackOverflow says you need it in order to do certain things in React.

Before we dive into what `this` really is and why you would use it, we first need to understand the difference between **functional** programming and **object-oriented** programming.

### Functional vs Object-Oriented Programming

You may or may not know that JavaScript has both functional and object-oriented constructs, so you can choose to focus on one or the other or use both.

I embraced functional programming early in my JavaScript journey and avoided object-oriented programming like the plague. I didn’t know or understand object-oriented keywords such as `this`. I think one reason I didn’t understand it was because I didn’t really get why it was necessary. It seemed like I could do everything I needed to do without relying on `this`.

And I was right.

Sort of. You can maybe get by only focusing on one paradigm and never learning about the other, but you will be limited as a JavaScript developer. To illustrate the differences between functional and object-oriented programming, I am going to use an array of Facebook friend data as an example.

Let’s say you’re building a web app where the user signs in with Facebook, and you show some data regarding their Facebook friends. You will need to hit a Facebook endpoint to get their friends’ data. It might have some information such as `firstName`, `lastName`,`username`, `numFriends`, `friendData`, `birthday`, and `lastTenPosts`.

```js
const data = [
  {
    firstName: 'Bob',
    lastName: 'Ross',
    username: 'bob.ross',    
    numFriends: 125,
    birthday: '2/23/1985',
    lastTenPosts: ['What a nice day', 'I love Kanye West', ...],
  },
  ...
]
```

The data above is what you get from the (fake, imaginary) Facebook API. Now you need to transform it, so that it is in a format that is useful to you and your project. Let’s say you want to show the following for each of the user’s friends:

* Their name in the format ``${firstName} ${lastName}``
* Three random posts
* Number of days until their birthday

### Functional Approach

A functional approach would be passing the whole array or each element of an array into a function that returns the manipulated data that you need:

```
const fullNames = getFullNames(data)
// ['Ross, Bob', 'Smith, Joanna', ...]
```

You start with raw data (from the Facebook API). In order to get it to transform into data that is useful to you, you pass the data into a function and the output is or includes the manipulated data that you can use in your app to display to the user.

You could imagine doing something similar for getting the three random posts and calculating the number of days until that friend’s birthday.

**The functional approach is taking your raw data, passing it through a function or multiple functions, and outputting data that is useful to you and your project.**

### Object-Oriented Approach

The object-oriented approach might be a little more difficult to grasp for those who are new to programming and learning JavaScript. The idea here is that you transform each friend **into** an object that has everything it needs to generate what **you** as the developer need.

You might create objects that have a `fullName` property, and two functions `getThreeRandomPosts` and `getDaysUntilBirthday` that are specific to that friend.

```js
function initializeFriend(data) {
  return {
    fullName: `${data.firstName} ${data.lastName}`,
    getThreeRandomPosts: function() {
      // get three random posts from data.lastTenPosts
    },
    getDaysUntilBirthday: function() {
      // use data.birthday to get the num days until birthday
    }
  };
}
const objectFriends = data.map(initializeFriend)
objectFriends[0].getThreeRandomPosts() 
// Gets three of Bob Ross's posts
```

**The object-oriented approach is creating objects for your data which have state and include all the information they need in order to generate the data that is useful to you and your project.**

### What does this have to do with this?

You might not have ever thought to write something like `initializeFriend` above, and you might think something like that could be pretty useful. You might also notice, however, that it is not **truly** object-oriented.

The only reason that the methods `getThreeRandomPosts` or `getDaysUntilBirthday` would even work in the example above is because of closure. They still have access to `data` after `initializeFriend` returns because of closure. For more information about closure, check out [You Don’t Know JS: Scope & Closures](https://github.com/getify/You-Dont-Know-JS/blob/master/scope%20%26%20closures/ch5.md).

What if you had another method, let’s call it `greeting`. Note that a method (in regards to an object in JavaScript) is just an attribute whose value is a function. We want `greeting` to do something like this:

```js
function initializeFriend(data) {
  return {
    fullName: `${data.firstName} ${data.lastName}`,
    getThreeRandomPosts: function() {
      // get three random posts from data.lastTenPosts
    },
    getDaysUntilBirthday: function() {
      // use data.birthday to get the num days until birthday
    },
    greeting: function() {
      return `Hello, this is ${fullName}'s data!`
    }
  };
}
```

Will that work?

No!

Everything in our newly created object has access to all the variables in `initializeFriend` but NOT any of the attributes or methods within the object itself. Certainly, you’ll ask the question:

> Couldn’t you just use `data.firstName` and `data.lastName` to return your greeting?

Yes, you absolutely could. But what if we also wanted to include in the greeting how many days until that friend’s birthday? We would have to somehow find a way to call `getDaysUntilBirthday` from within `greeting`.

IT’S TIME FOR `this` !

![Image](https://cdn-media-1.freecodecamp.org/images/CjfAp0G6O8yFJPu4aKOV8tvPjs2kt0eCaWct)
_Photo by [Unsplash](https://unsplash.com/photos/geM5lzDj4Iw?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">sydney Rae</a> on <a href="https://unsplash.com/search/photos/this?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Finally, what is this

`this` can refer to different things under different circumstances. By default, `this` refers to the global object (in the browser, this is the `window` object), which isn’t all that helpful. The `this` rule that is helpful for us right now is the following:

**If `this` is used in an object method and the method is called within the context of that object, `this` refers to the object itself.**

> You say “called within the context of that object”…what does that even mean?

Don’t worry, we will get to that later!

So if we wanted to call `getDaysUntilBirthday` from within `greeting` we can just call `this.getDaysUntilBirthday` because `this` in that scenario just refers to the object itself.

SIDE NOTE: Don’t use `this` in a regular ole function in the global scope or in the scope of another function! `this` is an object-oriented construct. Therefore, it only has meaning within the context of an object (or class)!

Let’s refactor `initializeFriend` to use `this`:

```js
function initializeFriend(data) {
  return {
    lastTenPosts: data.lastTenPosts,
    birthday: data.birthday,    
    fullName: `${data.firstName} ${data.lastName}`,
    getThreeRandomPosts: function() {
      // get three random posts from this.lastTenPosts
    },
    getDaysUntilBirthday: function() {
      // use this.birthday to get the num days until birthday
    },
    greeting: function() {
      const numDays = this.getDaysUntilBirthday()      
      return `Hello, this is ${this.fullName}'s data! It is ${numDays} until ${this.fullName}'s birthday!`
    }
  };
}
```

Now, everything that this object needs is scoped to the object itself once `intializeFriend` is executed. Our methods no longer rely on closure. They only use information contained within the object itself.

> Ok, so that is one way to use `this` , but you said that `this` can be many different things depending on the context. What does that mean? Why wouldn’t it always refer to the object itself?

There are some times where you want to force `this` to be something in particular. A good example is for event handlers. Let’s say we wanted to open up a friend’s Facebook page when the user clicks on them. We might add an `onClick` method to our object:

```js
function initializeFriend(data) {
  return {
    lastTenPosts: data.lastTenPosts,
    birthday: data.birthday,
    username: data.username,    
    fullName: `${data.firstName} ${data.lastName}`,
    getThreeRandomPosts: function() {
      // get three random posts from this.lastTenPosts
    },
    getDaysUntilBirthday: function() {
      // use this.birthday to get the num days until birthday
    },
    greeting: function() {
      const numDays = this.getDaysUntilBirthday()      
      return `Hello, this is ${this.fullName}'s data! It is ${numDays} until ${this.fullName}'s birthday!`
    },
    onFriendClick: function() {
      window.open(`https://facebook.com/${this.username}`)
    }
  };
}
```

Notice that we added `username` to our object, so that `onFriendClick` had access to it, so that we can open a new window with the Facebook page of that friend. Now we just need to write the HTML:

```html
<button id="Bob_Ross">
  <!-- A bunch of info associated with Bob Ross -->
</button> 
```

And now the JavaScript:

```js
const bobRossObj = initializeFriend(data[0])
const bobRossDOMEl = document.getElementById('Bob_Ross')
bobRossDOMEl.addEventListener("onclick", bobRossObj.onFriendClick)
```

In the code above, we create an object for Bob Ross. We get the DOM element associated with Bob Ross. And now we want to execute the `onFriendClick` method to open up Bob’s Facebook page. Should work as expected, right?

Nope!

What went wrong?

Notice that the function we chose for the onclick handler was `bobRossObj.onFriendClick` . See the problem yet? What if we re-wrote it like this:

```js
bobRossDOMEl.addEventListener("onclick", function() {  window.open(`https://facebook.com/${this.username}`)})bobRossDOMEl.addEventListener("onclick", function() {
  window.open(`https://facebook.com/${this.username}`)
})
```

Now do you see the problem? When we set the onclick handler to be `bobRossObj.onFriendClick` what we are actually doing is grabbing the function that is stored in `bobRossObj.onFriendClick` and passing it in as an argument. It is no longer “attached” to `bobRossObj` which means `this` no longer refers to `bobRossObj` . It actually refers to the global object, which means that `this.username` is undefined. It seems as though we are out of luck at this point.

IT’S TIME for `bind`!

![Image](https://cdn-media-1.freecodecamp.org/images/o36QYF-UudyA0jO8JbooQYneFJo5jeA2oAtS)
_Photo by [Unsplash](https://unsplash.com/photos/KiAZ61Sh17k?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Ksenia Makagonova</a> on <a href="https://unsplash.com/search/photos/rope?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Explicitly binding this

What we need to do is explicitly bind `this` to `bobRossObj`. We can do that by using `bind`:

```js
const bobRossObj = initializeFriend(data[0])
const bobRossDOMEl = document.getElementById('Bob_Ross')
bobRossObj.onFriendClick = bobRossObj.onFriendClick.bind(bobRossObj)
bobRossDOMEl.addEventListener("onclick", bobRossObj.onFriendClick)
```

Earlier, `this` was being set based on the default rule. With the use of `bind`, we explicitly set the value of `this` in `bobRossObj.onFriendClick` to be the object itself, or `bobRossObj`.

Up to this point, we have seen why `this` is helpful and why you might want to explicitly bind `this`. The last topic we will cover regarding `this` is arrow functions.

### Arrow functions

You might have noticed that arrow functions are the hip new thing. People seem to like them because they are concise and elegant. You might know that they are a little different from normal functions but maybe you don’t quite know what the difference is.

Perhaps the simplest way to describe how arrow functions are different is this:

**Whatever `this` refers to where an arrow function is declared, `this` refers to the same thing inside that arrow function.**

> Ok…that’s not helpful…I thought that was the behavior of a normal function?

Let’s explain with our `initializeFriend` example. Let’s say we wanted to add a little helper function within `greeting` :

```js
function initializeFriend(data) {
  return {
    lastTenPosts: data.lastTenPosts,
    birthday: data.birthday,
    username: data.username,    
    fullName: `${data.firstName} ${data.lastName}`,
    getThreeRandomPosts: function() {
      // get three random posts from this.lastTenPosts
    },
    getDaysUntilBirthday: function() {
      // use this.birthday to get the num days until birthday
    },
    greeting: function() {
      function getLastPost() {
        return this.lastTenPosts[0]
      }
      const lastPost = getLastPost()           
      return `Hello, this is ${this.fullName}'s data!
             ${this.fullName}'s last post was ${lastPost}.`
    },
    onFriendClick: function() {
      window.open(`https://facebook.com/${this.username}`)
    }
  };
}
```

Would this work? If not, how could we change it to make it work?

No, it will not work. Because `getLastPost` is not called within the context of an object, `this` inside `getLastPost` falls back to the default rule which is the global object.

> You say that it isn’t called “within the context of an object”…don’t you know that it is called inside the object that is returned from `initializeFriend`? If that isn’t called “within the context of an object” then I don’t know what is.

I know that “within the context of an object” is vague terminology. Perhaps a good way to determine if a function is called “within the context of an object” is to talk yourself through how the function is called and determine if an object is “attached” to the function.

Let’s talk through what happens when we execute `bobRossObj.onFriendClick()`. “Grab me the object `bobRossObj`, look for the attribute `onFriendClick` and **call the function assigned to that attribute**.”

Now let’s talk through what happens when we execute `getLastPost()`. “Grab me the function with the name `getLastPost` and call it.” Notice how there was no mention of an object?

Ok, here’s a tricky one to test your knowledge. Let’s say there is a function `functionCaller` where all it does is call functions:

```js
functionCaller(fn) {
  fn()
}
```

What if we did this: `functionCaller(bobRossObj.onFriendClick)`? Would you say that `onFriendClick` was called “within the context of an object”? Would `this.username` be defined?

Let’s talk through it: “Grab the object `bobRossObj` and look for the attribute `onFriendClick`. Grab its value (which happens to be a function), pass it into `functionCaller`, and name it `fn`. Now, execute the function named `fn`.” Notice that the function gets “detached” from `bobRossObj` before it is called and is therefore not called “within the context of the object `bobRossObj`” which means that `this.username` will be undefined.

Arrow functions to the rescue:

```js
function initializeFriend(data) {
  return {
    lastTenPosts: data.lastTenPosts,
    birthday: data.birthday,
    username: data.username,    
    fullName: `${data.firstName} ${data.lastName}`,
    getThreeRandomPosts: function() {
      // get three random posts from this.lastTenPosts
    },
    getDaysUntilBirthday: function() {
      // use this.birthday to get the num days until birthday
    },
    greeting: function() {
      const getLastPost = () => {
        return this.lastTenPosts[0]
      }
      const lastPost = getLastPost()           
      return `Hello, this is ${this.fullName}'s data!
             ${this.fullName}'s last post was ${lastPost}.`
    },
    onFriendClick: function() {
      window.open(`https://facebook.com/${this.username}`)
    }
  };
}
```

Our rule from above:

**Whatever `this` refers to where an arrow function is declared, `this` refers to the same thing inside that arrow function.**

The arrow function is declared inside of `greeting` . We know that when we use `this` in `greeting` it is referring to the object itself. Therefore, `this` inside the arrow function is referring to the object itself which is what we want.

### Conclusion

`this` is a sometimes-confusing but helpful tool for developing JavaScript apps. This is definitely not all there is to `this`. Some topics that were not covered are:

* `call` and `apply`
* how `this` changes when `new` is involved
* how `this` changes with the ES6`class`

I encourage you to ask yourself questions about what you think `this` should be in certain situations, and then test yourself by running that code in the browser. If you want to learn more about `this` , check out [You Don’t Know JS: this & Object Prototypes](https://github.com/getify/You-Dont-Know-JS/tree/master/this%20%26%20object%20prototypes).

And if you want to test yourself, check out [YDKJS Exercises: this & Object Prototypes](https://ydkjs-exercises.com/this-object-prototypes).

![Image](https://cdn-media-1.freecodecamp.org/images/6MubkHTI9p32BuBFH5wqv-Sqp2DQBxLPhdDj)
_Photo by [Unsplash](https://unsplash.com/photos/0FRJ2SCuY4k?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Jonas Jacobsson</a> on <a href="https://unsplash.com/search/photos/books?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

